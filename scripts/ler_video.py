"""Le um video para a skill ajustes-entender.

Gera, numa pasta de saida:
  info.txt          duracao, resolucao, fps, se tem audio
  cortes.txt        timecodes dos cortes de cena detectados
  quadros/*.jpg     quadros nos cortes e em intervalos fixos, com o timecode no nome
  folha_NN.jpg      folhas de contato com o timecode impresso em cada quadro
  movimento.txt     (com --trecho) diferenca quadro a quadro, para achar travadas

Uso:
  py ler_video.py VIDEO SAIDA [--passo 1.0] [--limiar 0.3]
  py ler_video.py VIDEO SAIDA --trecho 0.0 3.0      # todos os quadros do trecho + movimento
  py ler_video.py IMAGEM.png SAIDA                   # peca estatica: so copia e mede

Precisa de ffmpeg/ffprobe no PATH e Pillow.
"""
import argparse
import json
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def tc(t, fps=None):
    """Segundos -> mm:ss.d (e o numero do quadro, se houver fps)."""
    m, s = divmod(max(t, 0), 60)
    txt = f"{int(m):02d}:{s:04.1f}"
    if fps:
        txt += f" (q{int(round(t * fps))})"
    return txt


def probe(path):
    out = run(["ffprobe", "-v", "error", "-show_entries",
               "format=duration:stream=codec_type,width,height,r_frame_rate",
               "-of", "json", path])
    data = json.loads(out.stdout or "{}")
    info = {"duracao": float(data.get("format", {}).get("duration", 0) or 0), "audio": False}
    for s in data.get("streams", []):
        if s.get("codec_type") == "video" and "width" not in info:
            info["width"], info["height"] = s["width"], s["height"]
            num, den = s.get("r_frame_rate", "0/1").split("/")
            info["fps"] = round(float(num) / float(den), 3) if float(den) else 0
        if s.get("codec_type") == "audio":
            info["audio"] = True
    return info


def detectar_cortes(path, limiar):
    out = run(["ffmpeg", "-hide_banner", "-i", path, "-an", "-vf",
               f"scale=320:-2,select='gt(scene,{limiar})',showinfo", "-f", "null", "-"])
    return [float(x) for x in re.findall(r"pts_time:([\d.]+)", out.stderr)]


def extrair(path, t, destino, largura=640):
    run(["ffmpeg", "-hide_banner", "-y", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1",
         "-vf", f"scale={largura}:-2", "-q:v", "3", destino])
    return os.path.exists(destino)


def fonte(tam):
    for f in ("arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(f, tam)
        except OSError:
            continue
    return ImageFont.load_default()


def folhas(itens, saida, colunas=4, por_folha=16):
    """itens = [(rotulo, caminho_jpg)]. Monta folhas de contato com o rotulo impresso."""
    nomes = []
    for n in range(0, len(itens), por_folha):
        lote = itens[n:n + por_folha]
        thumbs = [Image.open(p).convert("RGB") for _, p in lote]
        w = max(i.width for i in thumbs)
        h = max(i.height for i in thumbs)
        escala = min(1.0, (1900 / colunas) / w)
        tw, th = int(w * escala), int(h * escala)
        linhas = (len(lote) + colunas - 1) // colunas
        folha = Image.new("RGB", (colunas * tw, linhas * (th + 34)), "white")
        d = ImageDraw.Draw(folha)
        f = fonte(22)
        for k, ((rot, _), img) in enumerate(zip(lote, thumbs)):
            x, y = (k % colunas) * tw, (k // colunas) * (th + 34)
            folha.paste(img.resize((tw, th)), (x, y + 34))
            d.rectangle([x, y, x + tw, y + 33], fill="black")
            d.text((x + 6, y + 5), rot, fill="yellow", font=f)
        nome = os.path.join(saida, f"folha_{n // por_folha + 1:02d}.jpg")
        folha.save(nome, quality=85)
        nomes.append(nome)
    return nomes


PARADO = 0.06  # diferenca media abaixo disso = quadro congelado (so ruido de compressao)


def movimento(path, ini, fim, fps, destino):
    """Mede quanto a imagem muda a cada quadro (0-255) e aponta suspeitas de travada.

    Resumo no topo (o que a chefia costuma chamar de "trava", "engasga", "pula"):
      - parada curta no meio de um movimento (hold de 2 quadros a 1 s com movimento antes e depois)
      - arrancada brusca (movimento comeca forte logo depois de um quadro parado, sem ease-in)
      - pico isolado (um quadro muda muito mais que os vizinhos: pulo de escala/posicao)
    Paradas longas costumam ser tempo de leitura e aparecem separadas.
    """
    import numpy as np
    w, h = 160, 90
    cmd = ["ffmpeg", "-hide_banner"]
    if ini is not None:
        cmd += ["-ss", f"{ini:.3f}", "-to", f"{fim:.3f}"]
    cmd += ["-i", path, "-an", "-vf", f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"]
    out = subprocess.run(cmd, capture_output=True)
    buf = np.frombuffer(out.stdout, dtype=np.uint8)
    n = len(buf) // (w * h)
    frames = buf[: n * w * h].reshape(n, h, w).astype(np.int16)
    base = ini or 0.0
    dif = [0.0] + [float(np.abs(frames[i] - frames[i - 1]).mean()) for i in range(1, n)]
    t = lambda i: base + i / fps

    # trechos parados
    trechos, atual = [], []
    for i in range(1, n):
        if dif[i] < PARADO:
            atual.append(i)
        elif atual:
            trechos.append(atual)
            atual = []
    if atual:
        trechos.append(atual)

    curtas, longas = [], []
    for tr in trechos:
        if len(tr) < 3:
            continue
        antes = tr[0] - 1 >= 1 and dif[tr[0] - 1] >= PARADO
        depois = tr[-1] + 1 < n and dif[tr[-1] + 1] >= PARADO
        txt = f"{tc(t(tr[0]), fps)} a {tc(t(tr[-1]), fps)} = {len(tr)} quadros ({len(tr) / fps:.2f} s)"
        (curtas if antes and depois and len(tr) <= fps else longas).append((len(tr), txt))

    arrancadas, picos = [], []
    for i in range(2, n):
        if dif[i] >= 1.0 and dif[i - 1] < PARADO:
            arrancadas.append((dif[i], f"{tc(t(i), fps)}: diferenca {dif[i]:.2f} logo apos quadro parado"))
        viz = [dif[j] for j in range(max(1, i - 3), min(n, i + 4)) if j != i]
        med = sorted(viz)[len(viz) // 2] if viz else 0
        if viz and dif[i] > 1.0 and dif[i] > 4 * (med + 0.05):
            picos.append((dif[i] / (med + 0.05), f"{tc(t(i), fps)}: diferenca {dif[i]:.2f} (vizinhos ~{med:.2f})"))

    def bloco(titulo, itens, vazio, maximo=10):
        # mais fortes primeiro, na ordem do tempo; corta listas longas (cortes secos, gravacao de tela)
        top = sorted(itens, key=lambda x: -x[0])[:maximo]
        top = [txt for _, txt in sorted(top, key=lambda x: x[1])]
        extra = f" (mostrando {maximo} de {len(itens)})" if len(itens) > maximo else ""
        return [titulo + extra] + [f"  {x}" for x in top or [vazio]]

    linhas = ["SUSPEITAS DE TRAVADA / PULO",
              "Muitas suspeitas = video com cortes secos ou gravacao de tela; use so como pista no trecho citado."]
    linhas += bloco("Paradas curtas no meio de movimento:", curtas, "nenhuma")
    linhas += bloco("Arrancadas bruscas (sem ease-in):", arrancadas, "nenhuma")
    linhas += bloco("Picos isolados (pulo de 1 quadro):", picos, "nenhum")
    linhas += [""] + bloco("Paradas longas ou nas pontas (geralmente leitura/hold):", longas, "nenhuma", 20)
    linhas += ["", "quadro\ttimecode\tdiferenca\tbarra"]
    for i in range(1, n):
        linhas.append(f"{i}\t{tc(t(i), fps)}\t{dif[i]:6.2f}\t{'#' * min(60, int(dif[i] * 4))}")
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write("\n".join(linhas))
    return len(curtas) + len(arrancadas) + len(picos)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("saida")
    ap.add_argument("--passo", type=float, default=None, help="segundos entre quadros fixos")
    ap.add_argument("--limiar", type=float, default=0.3, help="sensibilidade do corte de cena (0-1)")
    ap.add_argument("--trecho", nargs=2, type=float, metavar=("INI", "FIM"))
    a = ap.parse_args()

    os.makedirs(a.saida, exist_ok=True)
    qdir = os.path.join(a.saida, "quadros" if not a.trecho else f"trecho_{a.trecho[0]:.1f}-{a.trecho[1]:.1f}")
    os.makedirs(qdir, exist_ok=True)

    if a.entrada.lower().endswith(IMG_EXT):
        img = Image.open(a.entrada)
        with open(os.path.join(a.saida, "info.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"peca estatica\narquivo: {a.entrada}\nresolucao: {img.width}x{img.height}\n")
        print(f"Peca estatica {img.width}x{img.height}. Leia a imagem direto.")
        return

    if not os.path.exists(a.entrada):
        print(f"ERRO: arquivo nao encontrado: {a.entrada}. No Git Bash, passe o caminho no formato Windows (D:\\...).")
        return 1
    info = probe(a.entrada)
    fps, dur = info.get("fps") or 25, info["duracao"]

    if a.trecho:
        ini, fim = a.trecho
        itens = []
        t = ini
        while t <= fim + 1e-6:
            p = os.path.join(qdir, f"t{t:08.3f}.jpg")
            if extrair(a.entrada, t, p, 480):
                itens.append((tc(t, fps), p))
            t += 1 / fps
        mov = os.path.join(qdir, "movimento.txt")
        movimento(a.entrada, ini, fim, fps, mov)
        nomes = folhas(itens, qdir, colunas=6, por_folha=36)
        print(f"{len(itens)} quadros de {tc(ini)} a {tc(fim)}. Folhas: {len(nomes)} em {qdir}")
        print(f"Movimento quadro a quadro: {mov}")
        return

    passo = a.passo or (1.0 if dur <= 60 else 2.0 if dur <= 180 else 4.0)
    cortes = detectar_cortes(a.entrada, a.limiar)
    tempos = {round(c + 0.04, 2) for c in cortes}  # um pouco depois do corte, ja na cena nova
    t = 0.0
    while t < dur:
        tempos.add(round(t, 2))
        t += passo
    tempos.add(round(max(dur - 0.1, 0), 2))
    tempos = sorted(x for x in tempos if x < dur)
    # remove quadros colados (menos de 0,3 s) priorizando os cortes
    final = []
    for x in tempos:
        if final and x - final[-1] < 0.3:
            continue
        final.append(x)

    itens = []
    for x in final:
        p = os.path.join(qdir, f"t{x:08.2f}.jpg")
        if extrair(a.entrada, x, p):
            marca = " CORTE" if any(abs(x - (c + 0.04)) < 0.01 for c in cortes) else ""
            itens.append((tc(x) + marca, p))
    nomes = folhas(itens, a.saida)

    with open(os.path.join(a.saida, "info.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"arquivo: {a.entrada}\nduracao: {tc(dur)} ({dur:.2f}s)\n"
                 f"resolucao: {info.get('width')}x{info.get('height')}\nfps: {fps}\n"
                 f"audio: {'sim' if info['audio'] else 'nao'}\npasso: {passo}s\n")
    with open(os.path.join(a.saida, "cortes.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(tc(c, fps) for c in cortes) or "nenhum corte detectado")
    print(f"{tc(dur)} | {info.get('width')}x{info.get('height')} | {fps} fps | audio: {info['audio']}")
    print(f"{len(cortes)} cortes, {len(itens)} quadros, {len(nomes)} folhas em {a.saida}")
    susp = movimento(a.entrada, None, None, fps, os.path.join(a.saida, "movimento.txt"))
    print(f"{susp} suspeitas de travada/pulo no video inteiro (ver topo de movimento.txt)")


if __name__ == "__main__":
    sys.exit(main())
