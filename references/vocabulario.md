# Vocabulário da chefia → ação de motion

Leituras comuns de frases vagas. Use como ponto de partida para a proposta, nunca como regra: confira sempre o que a peça realmente mostra. Se a frase couber em mais de uma linha desta tabela, é dúvida (com proposta).

## Tempo e ritmo

| Frase | Leitura mais provável | Como medir / propor |
|---|---|---|
| "fica mais um pouco na tela", "dá tempo de ler" | Aumentar o tempo de permanência do elemento na tela (hold), não a velocidade da animação | Medir o hold atual em s/quadros com `--trecho`. Propor +0,5 s a +1 s; para texto, regra de leitura ≈ 3–4 palavras/s + 0,5 s. Dizer que o resto empurra e a duração total cresce (ou de onde tirar o tempo, se a duração for fixa). |
| "tá rápido", "corrido" | Holds curtos ou animações de entrada/saída curtas demais | Ver qual dos dois. Propor duração concreta (ex.: entrada de 8 → 12 quadros). |
| "tá arrastado", "lento", "cansativo" | Holds longos, cenas sem movimento | Apontar os trechos mais parados (movimento.txt) e propor cortes em s. |
| "mais energia", "mais dinâmico", "mais vida" | Ritmo de cortes mais curto, entradas com overshoot/ease mais agressivo, movimento de câmera, cortes no beat | Escolher 1–2 alavancas concretas para os trechos mais parados; nunca "tudo". Se a trilha for calma, citar troca de trilha como dúvida. |
| "mais calmo", "mais elegante", "mais premium" | Easings mais suaves, menos elementos simultâneos, holds maiores, transições por fade/dissolve | Propor valores (ex.: ease in-out longo, 18–24 quadros). |

## Transição e movimento

| Frase | Leitura mais provável | Como medir / propor |
|---|---|---|
| "tá travando", "engasga", "dá uma parada" | Hold ou quadro congelado no meio de um movimento, ou keyframes com velocidade zero no meio (ease in-out entre keys seguidas) | `--trecho` + `movimento.txt`: achar quadros com diferença ~0 entre trechos com movimento. Propor tirar o hold / converter keys do meio em velocidade contínua / dissolve acontecer com a cena ainda animada. |
| "antes estava melhor" | Comparar com a versão anterior, se houver; senão, a mudança recente na transição | Se tiver a versão anterior, medir as duas. Senão, dúvida: "o que mudou?" + proposta. |
| "transição estranha" | Pode ser travada, pulo de posição/escala entre cenas, cursor/elemento que some e volta, corte fora do tempo | Ver quadro a quadro e nomear o problema concreto antes de propor. |
| "pula", "dá um salto" | Descontinuidade de posição/escala entre dois quadros | Achar o quadro exato com `--trecho`; propor igualar o elemento fixo em px entre as cenas. |
| "glitch", "piscada", "falha" | Quadro preto/branco, sobra de camada, elemento vazando, máscara errada | Achar o quadro; dizer o que aparece e propor a correção. |

## Tamanho, posição, destaque

| Frase | Leitura mais provável | Como medir / propor |
|---|---|---|
| "muito grande", "muito pequeno" | Escala do elemento | Medir em px; se a chefia der referência ("do tamanho do logo final"), medir a referência e dar o valor alvo. |
| "mais destacado", "dar destaque", "chamar mais atenção" | Hierarquia: tamanho, peso, cor/contraste, posição (centro/primeiro a aparecer), isolar com respiro, animar a entrada | Mais de uma alavanca possível → é quase sempre dúvida com proposta. Propor a de menor impacto no layout primeiro e uma alternativa. |
| "mais clean", "tá poluído" | Menos elementos simultâneos, mais respiro, menos efeitos | Listar o que sai ou espera. |
| "centraliza", "alinha" | Alinhamento à grade/centro óptico | Dizer o eixo e o valor. |
| "aquele texto lá no meio", "a parte do celular" | Referência vaga de lugar | Resolver pelo mapa (posição na tela e momento). Se casar com mais de um, dúvida. |

## Texto

| Frase | Leitura mais provável |
|---|---|
| "trocar o texto para …" | Texto exato entre aspas, como a chefia escreveu. Conferir se já não está igual na V1. |
| "corrigir X" | Ortografia/acentuação. Atenção a erros de digitação e homófonos da própria chefia: leia pelo sentido. |
| "deixar somente X" | Remover os outros itens da lista e manter só X, reorganizando o espaço. |
| "incluir X", "da maior pra menor" | Adicionar e reordenar; dizer a ordem final explícita. |

## Som

| Frase | Leitura mais provável |
|---|---|
| "trilha mais calma/animada" | Troca de trilha (BPM, instrumentação). Propor características, não faixa específica, a não ser que haja biblioteca definida. |
| "não dá pra ouvir a locução" | Ducking da trilha sob a VO (−6 a −12 dB). |
| "sincroniza com a música" | Cortes/entradas no beat; medir o BPM se possível. |
