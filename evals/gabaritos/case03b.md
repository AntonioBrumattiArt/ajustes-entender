# Case 03b — V2 → V3 (tamanho do logo de entrada)

## Pedido (entrada do teste)

Vídeo de entrada: `case 03\V2.mp4` (1080x1920, 24 fps, 28,5 s / 684 frames).

Pedido da chefia (verbatim):

> @Antonio Brumatti @Guilherme Santiago ajuste:
> o logo de entrada está muito grande, deixar ele do mesmo tamanho que o logo de fechamento do vídeo, por favor

## Gabarito

**Ajustes**

1. [00:00–00:05] Logo de abertura (símbolo com moldura + "App Banco Pine"): reduzir a escala até o símbolo ficar com o tamanho do símbolo isolado do fechamento.
   - Medir a referência: no fechamento, o símbolo isolado tem 334x302 px em 00:25.000 (f600; pico de 344 px em 00:24.750).
   - Medir a abertura: na V2 o símbolo tem ~440 px no pop (f8), cresce até 484x436 px (f33–f40, 00:01.375–00:01.667), encolhe para ~413–416 px em 00:02.4–00:03.0 e cresce devagar até 441 px em 00:05.2. Na V2, em 00:03.000 (f72) ele tem 416x374 px.
   - Reduzir o grupo inteiro ~78% (de 416 px para ~326 px de largura em 00:03.000; ~336 px em 00:04.000, igual ao fechamento) aplicando a escala num pai/null acima da animação, para não mexer nos keyframes de escala que já existem.
   - Reduzir junto o texto "App Banco Pine" (711 px → 557 px de largura em 00:03.000) e reaproximar do símbolo (topo do texto de y=1244 para y=1174), mantendo o centro do símbolo em y≈959.
   - Conferir no gráfico de velocidade que a curva da entrada (pop, hold, "batida" em f46, push lento) continua a mesma, só menor.

**Dúvidas para a chefia**

- "Logo de fechamento" é o símbolo isolado (334 px em 00:25.000) ou o símbolo dentro da assinatura final "BANCO PINE" (208x188 px a partir de 00:26.375)? A V3 usou o símbolo isolado.

**Observação**

- A animação de entrada tem uma "batida" de escala em f46 (00:01.917): se a escala for corrigida mexendo nos keyframes, em vez de num pai, a curva pode quebrar (foi o que gerou a reclamação da rodada seguinte).

## Notas de verificação

- Diferenças V2 × V3 só nos frames 6–129 (00:00.250–00:05.375). Do frame 130 em diante (transição para o celular e todo o resto) os vídeos são idênticos. O logo de fechamento é igual nas duas versões (334x302 px em f600; assinatura 536x188 px a partir de f633).
- Largura do símbolo (com moldura), V2 → V3:
  - pop f8 (00:00.333): 440 → 252 px
  - f33–f40 (00:01.375–00:01.667): 484 → 268–270 px (ali ele fica quase parado nas duas versões)
  - f48 (00:02.000): 423 → 319 px
  - f72 (00:03.000): 416x374 → 326x294 px
  - f96 (00:04.000): 426x384 → 336x302 px (= fechamento 334x302)
  - f120 (00:05.000): 438x396 → 348x314 px
- "App Banco Pine": 711x73 → 557x58 px (f72); 751 → 597 px (f120).
- Efeito colateral NÃO pedido: a curva de escala não foi só reduzida, mudou de forma. Na V2 o símbolo crescia até 484 px, ficava parado de f33 a f40 e na batida de f46 ENCOLHIA (470 → 435 px num frame) e assentava em ~413 px. Na V3 a primeira parte foi reduzida mais que a segunda: fica parado em ~270 px (f33–f41) e na batida CRESCE de repente (282 → 309 px num frame, f45→f46), indo para ~324 px. A diferença média entre frames em f46 é 3,0 (contra 0,01–0,06 durante a parada). É exatamente o "trava e depois vai pra frente" que o cliente apontou na rodada 3.
- Frames de trabalho: `claude-assets\work\case03\V2_sheet_01.png`, `V3_sheet_01.png`, `open_V2.png`, `open_V3.png`.
