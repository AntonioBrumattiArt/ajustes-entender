# ajustes-entender

Skill do Claude que transforma o pedido de ajuste da chefia (texto, áudio, print rabiscado) sobre uma peça de motion ou estática numa lista de ajustes esmiuçada para fazer a V2. Ela cruza o pedido com a V1 real (quadros com timecode, folhas de contato, medição de movimento) e devolve:

- **Ajustes**: `[timecode] Elemento: ação` + passos de execução;
- **Dúvidas**: pergunta pronta para a chefia + proposta;
- **Observação**: o que foi visto mas não pedido.

Não aplica os ajustes.

## Instalação

Copie esta pasta para `%USERPROFILE%\.claude\skills\ajustes-entender`.

Requisitos: `ffmpeg`/`ffprobe` no PATH, Python 3 com Pillow e numpy. Opcional para áudio: `py -m pip install faster-whisper`.

## Scripts

| Script | Para quê |
|---|---|
| `scripts/ler_video.py` | Quadros nos cortes e em intervalo fixo, folhas de contato com timecode; `--trecho` para quadro a quadro + medição de travadas |
| `scripts/achar_quadro.py` | Acha no vídeo o quadro de um print (com rabiscos) |
| `scripts/transcrever.py` | Transcreve áudio em português com timecode (faster-whisper) |

## Testes

`evals/gabaritos/` guarda os gabaritos em texto dos cases usados para calibrar a skill. Os vídeos e imagens dos clientes não ficam no repositório.
