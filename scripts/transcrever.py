"""Transcreve audio (pedido da chefia ou locucao do video) em portugues, com timecode.

Uso:
  py transcrever.py ARQUIVO SAIDA.txt [--modelo small]

Aceita audio (ogg/opus do WhatsApp, m4a, mp3, wav) ou video (usa a trilha de audio).
Usa faster-whisper. Se nao estiver instalado, avisa como instalar (uma vez so):
  py -m pip install faster-whisper
Na primeira execucao o modelo e baixado (~460 MB no "small").
"""
import argparse
import os
import subprocess
import sys
import tempfile


def tc(t):
    m, s = divmod(t, 60)
    return f"{int(m):02d}:{s:04.1f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entrada")
    ap.add_argument("saida")
    ap.add_argument("--modelo", default="small")
    a = ap.parse_args()

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("FALTA_WHISPER: faster-whisper nao esta instalado.")
        print("Peca ao usuario para autorizar: py -m pip install faster-whisper")
        return 2

    # normaliza para wav mono 16 kHz (evita problemas com opus/ogg do WhatsApp)
    tmp = os.path.join(tempfile.gettempdir(), "ajustes_entender_audio.wav")
    r = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", a.entrada, "-vn", "-ac", "1",
                        "-ar", "16000", tmp], capture_output=True)
    if r.returncode != 0 or not os.path.exists(tmp):
        print("Sem audio no arquivo ou ffmpeg falhou.")
        return 1

    model = WhisperModel(a.modelo, device="auto", compute_type="int8")
    segs, _ = model.transcribe(tmp, language="pt", vad_filter=True)
    linhas = [f"[{tc(s.start)}–{tc(s.end)}] {s.text.strip()}" for s in segs]
    os.makedirs(os.path.dirname(os.path.abspath(a.saida)), exist_ok=True)
    with open(a.saida, "w", encoding="utf-8") as fh:
        fh.write("\n".join(linhas))
    print("\n".join(linhas) or "(nada transcrito)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
