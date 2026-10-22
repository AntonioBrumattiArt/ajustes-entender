# Case 03c — V3 → V4 (transição de abertura travando)

## Pedido (entrada do teste)

Vídeo de entrada: `case 03\V3.mp4` (1080x1920, 24 fps, 28,5 s / 684 frames).

Pedido da chefia (verbatim):

> @Antonio Brumatti cliente -
>
> A transição ta meio estranha
> A transição do fim rola normal
> Mas a da abertura, parece que ela trava um pouco, depois vai pra frente.
> Antes era mais suave...
> Se o designer motion puder dar uma conferida....ver se está tudo ok

## Gabarito

**Ajustes**

1. [00:01–00:03] Logo de abertura (símbolo + "App Banco Pine"): tirar a parada e o salto da curva de escala, deixando um crescimento contínuo (interpretação: "trava um pouco, depois vai pra frente").
   - Diagnóstico no V3: o símbolo cresce devagar até 268 px (f29), fica praticamente parado em 268–271 px de f31 a f41 (00:01.292–00:01.708; ~10 frames com diferença entre frames de 0,01–0,06) e depois salta 282 → 309 px de um frame para o outro em f45→f46 (00:01.875→00:01.917; diferença entre frames de 3,0), assentando em ~324 px em f53.
   - Causa provável: na rodada anterior a escala foi reduzida nos keyframes, e a primeira parte ficou menor que a segunda. A "batida" que na V2 encolhia o logo virou um pulo para frente.
   - Correção (como na V4): refazer a escala como uma rampa contínua de ~258 px (f29) até ~310 px (f53), sem keyframe de hold nem degrau. Os incrementos ficam entre 0 e 4 px por frame, e a diferença máxima entre frames cai de 3,0 para 0,82.
   - Manter o flash/glow da batida (f46–f53) e a entrada do "App Banco Pine" (f46) no mesmo tempo; não mexer na transição para o celular (f114–f130) nem em nada depois de f129.
   - Conferir o tamanho final contra o logo de fechamento (334 px em 00:25.000): na V4 o símbolo fica com 336 px em 00:03.000, 352 px em 00:04.000 e 358 px em 00:05.000.

**Dúvidas para a chefia**

- Nenhuma.

**Observação**

- "Antes era mais suave" compara com a V2, que também tinha uma parada de ~8 frames (f33–f40). Lá, porém, a batida era para dentro (o logo encolhia e "assentava"), e isso não lia como trava. Se a chefia quiser exatamente o feel da V2, a alternativa é refazer a batida encolhendo, só que já no tamanho novo.

## Notas de verificação

- Diferenças V3 × V4 só nos frames 13–35, 40–60 e 63–128 (00:00.542–00:05.375). Do frame 129 em diante os vídeos são idênticos, inclusive a transição do fim (celular → logo, ~00:24.0–00:26.4), que o cliente disse estar ok.
- Largura do símbolo (com moldura), V3 → V4, frame a frame nos pontos-chave:
  - f8 (00:00.333): 252 → 248 px
  - f29 (00:01.208): 268 → 258 px
  - f36 (00:01.500): 270 → 266 px
  - f41 (00:01.708): 271 → 276 px
  - f45 (00:01.875): 282 → 287 px
  - f46 (00:01.917): 309 → 290 px (o salto de +27 px some; na V4 são +3 px)
  - f48 (00:02.000): 319 → 296 px
  - f53 (00:02.208): 324 → 310 px
  - f72 (00:03.000): 326x294 → 336x302 px
  - f96 (00:04.000): 336x302 → 352x316 px
  - f120 (00:05.000): 348x314 → 358x322 px
- Movimento (diferença média absoluta entre frames consecutivos, 0–255, frame em escala de cinza 1080x1920): V3 0,01–0,06 em f31–f40 e pico de 3,00 em f46; V4 0,10–0,82 de f29 a f53, sem pico isolado. V2 para comparação: 0,02–0,16 em f33–f40 e pico de 6,45 em f46 (a batida encolhendo).
- Mudanças NÃO pedidas (pequenas):
  - Na V4 o logo de abertura ficou ~3% maior que na V3 a partir de 00:02.5 (336 contra 326 px em 00:03.000), e o "App Banco Pine" acompanhou (575 contra 557 px de largura; topo do texto 8 px mais baixo). Continua próximo do fechamento (334–344 px).
  - No começo da V4 a moldura fica quase parada em 248 px de f8 a f12 (diferença entre frames de 0,01–0,02), antes das árvores entrarem. É curto e fica antes do momento reclamado.
- Frames de trabalho: `claude-assets\work\case03\open_V2.png`, `open_V3.png`, `open_V4.png` (todos os frames de f24 a f63, com timecode); `V3_sheet_01.png`, `V4_sheet_01.png`; script de medição `op.py`.
