# Case 06 (simulado) — print rabiscado

## Pedido (entrada do teste)
Vídeo de entrada: `case 03\V2.mp4`. Print: `claude-assets\simulados\case06-print-rabiscado.jpg` (quadro de 00:02.6 com círculo vermelho no símbolo do logo, seta e "MENOR!!").
Texto que acompanhou o print (WhatsApp):
> isso aqui ta mt grande, deixa igual o do final

## Gabarito

**Ajustes**
1. [00:00–00:05.4] Logo de abertura (símbolo + "App Banco Pine"): reduzir a escala até o símbolo ficar do tamanho do símbolo isolado do fechamento.
   - Print casa com ~00:02.6 (logo com "App Banco Pine" embaixo).
   - Referência: símbolo do fechamento ≈334×302 px em 00:25.0. Abertura hoje ≈416 px em 00:03.0 → alvo ≈326–336 px (≈78–80%).
   - Escalar o grupo num pai/null, sem mexer nos keyframes de escala existentes, para não quebrar a curva (pop, hold, batida em ~00:01.9).
   - Reduzir junto "App Banco Pine" e reaproximar do símbolo; manter o centro vertical.

**Dúvidas para a chefia**
- "O do final" é o símbolo sozinho (~334 px, 00:25) ou o da assinatura "BANCO PINE" (~208 px, a partir de 00:26.4)? Proposta: símbolo sozinho.
- (opcional) O texto "App Banco Pine" diminui junto?

## Critérios-chave
- Localiza o print no tempo certo (00:02–00:03.9, logo de abertura).
- Entende "isso aqui" = símbolo do logo de abertura e "o do final" = logo do fechamento.
- Dá valores em px (medidos) para atual e alvo.
- Levanta a ambiguidade entre os dois logos do final.
