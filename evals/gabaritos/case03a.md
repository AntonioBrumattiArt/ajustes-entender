# Case 03a — V1 → V2 (tempo do primeiro texto)

## Pedido (entrada do teste)

Vídeo de entrada: `case 03\V1.mp4` (1080x1920, 24 fps, 12,29 s / 295 frames).

Pedido da chefia (verbatim):

> esse primeiro texto pode ficar um segundo a mais?
> nem sei se 1 segundo ou 0,5, mas um tiquinho mais

## Gabarito

**Ajustes**

1. [00:00–00:01] Texto "Diversifique sua carteira de investimentos": aumentar o tempo de tela entre 0,5 s e 1 s (interpretação: "um tiquinho mais", entre +12 e +24 frames).
   - No V1 o texto está 100% legível de f0 a f12 (~0,5 s), faz fade-out de f12 a f20 e some em f21 (00:00:00.875); "com segurança" começa a digitar em f23.
   - Estender o hold do texto antes do fade-out: na V2 o trecho legível passou de ~12–13 frames para ~33 frames (f368–f401 na timeline da V2), ou seja, +21 frames (~0,875 s), dentro da faixa de 0,5–1 s pedida.
   - Empurrar em bloco tudo o que vem depois (fade-out, "com segurança", celular, CTA, logo), sem mudar a duração de nenhum outro trecho; o vídeo cresce o mesmo número de frames do hold adicionado.
   - Conferir que o fade-out (8 frames) e o intervalo vazio de 2 frames antes de "co" continuam iguais.

**Dúvidas para a chefia**

- 0,5 s ou 1 s? O pedido deixa aberto; sugerir ~+0,75 s (+18 frames) e mostrar, ou entregar as duas opções.

**Observação**

- O V1 começa com o texto já 100% na tela no frame 0, sem animação de entrada (o "com segurança" logo depois entra com type-on). Parece um corte no meio do texto: vale perguntar se falta a entrada (type-on) ou um trecho antes dele.

## Notas de verificação

- Durações: V1 = 295 frames (12,29 s); V2 = 684 frames (28,5 s). Mesmo formato e fps.
- **Por que a V1 tem 12,3 s e a V2 28,5 s:** a V1 é idêntica, frame a frame, aos frames 389–683 da V2 (diferença média de pixel ≤ 0,2/255 nos frames do texto e ≤ 0,02 no resto, só ruído de compressão; caixas delimitadoras do texto iguais pixel a pixel). Ou seja, a V1 era um render parcial/trecho final da peça, começando em 00:16.208 da timeline completa, no meio do hold do texto. A V2 é o render completo: os primeiros 16,2 s (389 frames) não existiam na V1 — logo de abertura com "App Banco Pine" (0–5,4 s), celular com tela de investimentos (5,4–7 s), texto "Invista em ativos de renda fixa com a solidez do Banco Pine." com lista CDB / CDB Renda Mensal / LCI / LCA / LF (7–14,8 s).
- Texto "Diversifique sua carteira de investimentos" na V2: type-on começa em f356 (00:14.833), termina em f368 (00:15.333), fica cheio até ~f401 (00:16.708), fade-out f401–f409, some em f410 (00:17.083); "co" aparece em f412 (00:17.167). Tempo total na tela: 54 frames (2,25 s) contra 21 frames (0,875 s) na V1 (+33 frames / +1,375 s); hold legível +~21 frames (~0,875 s).
- Do ponto em que a V1 começa (V2 f389) até o fim, a timing é idêntica: o fade-out do texto, "com segurança", celular, CTA "Baixe o App Banco Pine" e logo final caem exatamente nos mesmos frames (offset constante de 389). O "tempo a mais" do texto na V2 vem de frames que já existiam antes do ponto de corte da V1, não de um hold esticado depois dele.
- Mudança NÃO pedida: entrada de 16,2 s de conteúdo novo no início (ver acima). Se a V1 era só um recorte para aprovação, não é uma mudança de fato; se a V1 era a peça inteira, foi um acréscimo grande sem pedido.
- Na V2 o primeiro texto do vídeo passa a ser "App Banco Pine" / "Invista em ativos...", então "esse primeiro texto" só faz sentido em relação à V1.
- Frames de trabalho: `claude-assets\work\case03\V1_sheet_01.png`, `V2_sheet_01.png`, `V1_text.png`, `V2_text.png`.
