"""Acha no video original o quadro de um print (rabiscado ou nao) mandado pela chefia.

Compara o print com o video inteiro em baixa resolucao e devolve os timecodes mais
parecidos, com uma folha mostrando print x candidatos. Rabiscos, setas e circulos
atrapalham pouco porque a comparacao usa a imagem toda reduzida.

Uso:
  py achar_quadro.py VIDEO PRINT.png SAIDA [--top 5]

Se o print tiver bordas de interface (WhatsApp, Frame.io, player), recorte a area do
video antes com --recorte X Y L A (em pixels do print).
"""
import argparse
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 96, 96  # comparacao em grade quadrada, independente do formato


def frames_video(path, fps_amostra):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-an", "-vf",
                          f"fps={fps_amostra},scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True)
    buf = np.frombuffer(out.stdout, dtype=np.uint8)
    n = len(buf) // (W * H)
    return buf[: n * W * H].reshape(n, H, W).astype(np.float32)


def normaliza(a):
    a = a - a.mean()
    return a / (a.std() + 1e-6)


def tc(t):
    m, s = divmod(t, 60)
    return f"{int(m):02d}:{s:05.2f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("print_img")
    ap.add_argument("saida")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--fps", type=float, default=8.0, help="quadros por segundo na busca")
    ap.add_argument("--recorte", nargs=4, type=int, metavar=("X", "Y", "L", "A"))
    a = ap.parse_args()
    os.makedirs(a.saida, exist_ok=True)

    img = Image.open(a.print_img).convert("L")
    if a.recorte:
        x, y, l, al = a.recorte
        img = img.crop((x, y, x + l, y + al))
    alvo = normaliza(np.asarray(img.resize((W, H)), dtype=np.float32))

    frames = frames_video(a.video, a.fps)
    # correlacao (robusta a brilho) e erro absoluto mediano (robusto a rabiscos)
    scores = []
    for i, f in enumerate(frames):
        fn = normaliza(f)
        corr = float((fn * alvo).mean())
        mad = float(np.median(np.abs(fn - alvo)))
        scores.append((corr - 0.5 * mad, i / a.fps))
    scores.sort(reverse=True)

    escolhidos = []
    for s, t in scores:
        if all(abs(t - t2) > 0.5 for _, t2 in escolhidos):
            escolhidos.append((s, t))
        if len(escolhidos) == a.top:
            break

    # folha: print + candidatos em resolucao legivel
    thumbs = [("PRINT", Image.open(a.print_img).convert("RGB"))]
    for s, t in escolhidos:
        p = os.path.join(a.saida, f"cand_{t:07.2f}.jpg")
        subprocess.run(["ffmpeg", "-hide_banner", "-y", "-ss", f"{t:.3f}", "-i", a.video,
                        "-frames:v", "1", "-vf", "scale=480:-2", p], capture_output=True)
        if os.path.exists(p):
            thumbs.append((f"{tc(t)}  nota {s:.2f}", Image.open(p).convert("RGB")))
    th = 420
    ims = [(r, i.resize((int(i.width * th / i.height), th))) for r, i in thumbs]
    folha = Image.new("RGB", (sum(i.width for _, i in ims) + 10 * len(ims), th + 36), "white")
    d = ImageDraw.Draw(folha)
    try:
        f = ImageFont.truetype("arialbd.ttf", 20)
    except OSError:
        f = ImageFont.load_default()
    x = 0
    for r, i in ims:
        folha.paste(i, (x, 36))
        d.text((x + 4, 6), r, fill="black", font=f)
        x += i.width + 10
    destino = os.path.join(a.saida, "achar_quadro.jpg")
    folha.save(destino, quality=85)

    print("Candidatos (maior nota = mais parecido):")
    for s, t in escolhidos:
        print(f"  {tc(t)}  nota {s:.2f}")
    print(f"Confira visualmente: {destino}")
    print("Depois refine com: py ler_video.py VIDEO SAIDA --trecho INI FIM")


if __name__ == "__main__":
    main()
