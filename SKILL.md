---
name: ajustes-entender
description: Transforma um pedido de ajuste da chefia (diretor, gestor, cliente) sobre uma peça de motion ou estática em uma lista de ajustes esmiuçada para o motion designer executar a V2. Cruza o pedido com a V1 real (quadros com timecode, folhas de contato, mapa de cenas, transcrição), localiza cada pedido no trecho certo, traduz pedidos vagos ("dá mais energia", "aquele texto lá no meio", "tá sem graça", "puxa mais pra frente") em ações concretas de motion com proposta, e separa dúvidas prontas para mandar à chefia. Use sempre que o usuário mandar uma V1 (vídeo ou imagem) junto com um pedido de ajuste, alteração, correção, feedback, comentário ou refação (texto de WhatsApp/e-mail/Frame.io, áudio, print rabiscado ou vídeo anotado), ou perguntar "o que eles querem que eu mude?", "me ajuda a entender esse ajuste", "monta a lista de ajustes", mesmo sem citar a skill. Não aplica os ajustes.
---

# Ajustes: entender o pedido e montar a lista da V2

O usuário é motion designer. Ele faz a V1, a chefia pede ajustes — quase sempre de forma vaga, picada, misturando opinião com ordem — e ele precisa saber exatamente o que mexer para fazer a V2 sem ida e volta. Seu trabalho é fazer o meio de campo: ver a peça de verdade, entender o que a chefia quis dizer e devolver uma lista que ele execute de olhos fechados. **Você não aplica os ajustes**; ele faz à mão.

O valor está em duas coisas: (1) amarrar cada frase do pedido a um ponto real da peça, com timecode, e (2) transformar o vago em concreto sem inventar. Quando der para interpretar com segurança, proponha. Quando houver mais de uma leitura razoável, pergunte — mas sempre trazendo a sua proposta junto, para ele poder só dizer "vai na sua".

## Entrada

- **V1**: vídeo (mp4/mov) ou peça estática (png/jpg). Às vezes várias telas soltas de um carrossel.
- **Pedido**, de um ou mais jeitos:
  - texto (WhatsApp, e-mail, comentário de Frame.io/Monday/Drive, print de conversa);
  - áudio (ogg/opus do WhatsApp, m4a) → transcrever;
  - print ou vídeo anotado com setas, círculos e rabiscos → achar esse quadro na V1;
  - várias rodadas: trate só o pedido mais recente, a não ser que ele peça o contrário.

Se faltar a V1 ou o pedido, peça antes de começar. Se o pedido citar uma tela/arquivo que não veio, não invente o conteúdo: registre como dúvida.

## Fluxo

Os scripts ficam em `scripts/` desta skill. Rode com `py` (Windows) ou `python3`. No Git Bash, passe caminhos de arquivo e de saída no formato Windows (`D:\...`), nunca `/d/...` — o Python do Windows não entende esse formato. Precisam de ffmpeg no PATH e Pillow/numpy. Salve tudo que gerar numa pasta de trabalho do projeto (`assets\claude-assets\ajustes-<nome>` se houver estrutura de projeto; senão uma pasta temporária). Nunca grave por cima dos arquivos do usuário.

### 1. Ler o pedido primeiro

Leia o pedido inteiro antes de abrir a peça. Anote cada frase que pede algo e o que ela aponta ("primeiro texto", "logo de entrada", "Tela 03", "a transição da abertura"). Isso diz onde olhar com mais cuidado.

- Áudio: `py scripts/transcrever.py AUDIO pedido.txt`. Se responder `FALTA_WHISPER`, peça ao usuário autorização para instalar (`py -m pip install faster-whisper`); não instale sem ok. Se ele preferir, ele cola o texto.
- Print/vídeo anotado: leia a imagem, descreva o que os rabiscos marcam e rode `py scripts/achar_quadro.py V1 PRINT pasta`. Confirme visualmente o candidato na folha gerada e diga no item o timecode do quadro do print (ex.: "o print é de 00:02.6"). Se o print tiver interface em volta, use `--recorte`.

### 2. Ler a V1

**Vídeo:** `py scripts/ler_video.py V1 pasta`. Gera `info.txt`, `cortes.txt`, folhas de contato com o timecode impresso (cortes de cena + intervalo fixo) e `movimento.txt` do vídeo inteiro. Olhe todas as folhas. Animação com transições suaves muitas vezes não tem "corte" detectado — o intervalo fixo cobre isso.

O topo do `movimento.txt` lista **suspeitas de travada/pulo**: paradas curtas no meio de um movimento, arrancadas sem ease-in e picos isolados (um quadro que muda muito mais que os vizinhos = pulo de escala/posição). Um pico isolado depois de uma parada curta é a assinatura clássica do "trava e depois vai". Em gravação de tela ou edição com cortes secos a lista fica longa e vira só pista.

Quando o pedido for sobre tempo, ritmo, transição, travada, "tá rápido", "fica mais um pouco": rode também `--trecho INI FIM` no trecho em questão (todos os quadros + `movimento.txt` só daquele trecho). Use para medir em segundos e quadros (ex.: "o texto fica 1,4 s / 34 quadros na tela", "a imagem para 10 quadros em 00:04.6 e pula no quadro seguinte").

Se o pedido mencionar locução, fala, legenda ou trilha, transcreva o áudio do próprio vídeo com `transcrever.py`.

**Estática:** leia a imagem direto. Meça posições e tamanhos aproximados em px quando o ajuste for de layout/tamanho.

**Monte um mapa da peça** (para você, não precisa mostrar inteiro): cena a cena com timecode de entrada/saída, textos exatos na tela, elementos, cores dominantes, tipo de transição. É esse mapa que permite dizer "aquele texto lá no meio = 'Sem taxa de adesão', 00:07–00:14".

### 3. Interpretar

Para cada frase do pedido:

1. **Localizar**: em que trecho/tela/elemento ela cai. Use o mapa. Se "primeiro texto" puder ser duas coisas, é dúvida. Leia as palavras da chefia como leigo fala, não como termo técnico: "transição" pode ser qualquer animação (a montagem do logo, a entrada de um texto), não só a passagem entre cenas; "abertura" é o começo do vídeo, a partir do quadro 0. Antes de fechar o local, confira todos os candidatos — para travada, cruze o trecho citado com as suspeitas do `movimento.txt` e olhe quadro a quadro os mais fortes. Se dois lugares servirem, aponte os dois (ajuste no mais provável + dúvida). Quando o pedido é sobre um elemento ("o ícone vermelho", "o logo", "a palavra X"), procure **todas** as aparições dele no vídeo, não só a primeira — a chefia espera que suma/mude em todas, e cada aparição vira um timecode no item.
2. **Separar e juntar**: uma frase com dois pedidos vira dois itens; dois jeitos de pedir a mesma coisa viram um item.
3. **Traduzir em ação de motion**: trocar texto, mudar cor, mudar duração/ritmo, mudar easing ou transição, reposicionar, mudar escala, mudar hierarquia/destaque, trocar ou cortar trilha, corrigir falha técnica (glitch, quadro preto, pulo), etc.
4. **Pedido subjetivo** ("mais energia", "mais destacado", "tá estranho", "mais clean"): proponha a leitura concreta mais provável, marcada "(interpretação)", com valores. Consulte `references/vocabulario.md` — traz leituras comuns de frases vagas e como medir.
5. **Mais de uma leitura plausível**: não escolha sozinho em silêncio. Vai para **Dúvidas** com a pergunta pronta para a chefia **e** a sua proposta. No item da lista, deixe claro que depende da dúvida.
6. **Conferir com a peça real**: o pedido pode já estar atendido na V1 (texto já igual, elemento já no lugar), citar algo que não existe ou estar com erro de digitação (leia pelo sentido). Não crie um ajuste que não muda nada — explique na dúvida ou observação.

Regras que evitam retrabalho:
- **Não invente ajustes.** Só entra em Ajustes o que a chefia pediu (ou é consequência direta, ex.: se um texto fica mais tempo, o resto empurra). Erro óbvio que ninguém pediu (erro de português, glitch, corte seco, elemento vazando) vai em **Observação**.
- **Texto novo exatamente como a chefia escreveu**, entre aspas, com a pontuação dela. Se o texto dela tiver erro, mantenha e aponte na Observação.
- Preserve o que não foi pedido: diga nos passos o que **não** mexer quando houver risco (ex.: "manter VO, trilha e duração total").
- Prefira o caminho que não quebra o que já funciona: mudar escala/posição de um elemento animado num pai/null (ou pré-comp) em vez de reescrever os keyframes dele, para a curva continuar igual. Mexer nos keyframes costuma criar a próxima reclamação ("agora trava").
- Igualar a uma referência ("do tamanho do logo do final", "igual à tela 2"): meça a referência e o elemento atual em px e dê o alvo. Se a referência aparece em mais de um tamanho ou forma, é dúvida — proponha a ocorrência que mais se parece com o elemento a ajustar (mesma composição, mesmo papel na peça) e dê o alvo das duas.
- Texto, URL ou QR novo precisa de tempo de leitura (≈3–4 palavras/s + 0,5 s; QR ≥ 2–3 s parado). Se a cena atual não comporta, diga quanto falta e de onde tirar — e, se a chefia pediu "manter duração", leve o conflito para Dúvidas.
- Se a V1 parecer incompleta (começa no meio de uma animação, termina cortada, falta tela citada), diga em Observação ou Dúvidas — pode ser render parcial e mudar a leitura do pedido.
- Timecodes são da V1, formato `mm:ss` ou `mm:ss.d` quando precisão importar. Em carrossel/telas: `[Tela 02]` ou `[Tela 02 · 00:03–00:06]`. Ajuste que vale para a peça toda: `[Geral]`.

### 4. Entregar

Texto no chat, curto, em português. A primeira linha é `**Ajustes**` — sem frase de abertura; o contexto (ex.: "ele está falando da montagem do logo") vai dentro do item. Exatamente esta estrutura:

```
**Ajustes**
1. [00:03–00:06] Título "Bem-vindo": trocar para "Olá, seja bem-vindo".
   - Mesma fonte, tamanho e animação de entrada; ajustar a caixa se o texto quebrar linha.
2. [00:00–00:01.5] Abertura: suavizar a transição (interpretação).
   - Hoje a imagem para 10 quadros em 00:00.8 e depois anda. Tirar o hold e emendar o movimento: ease-out contínuo até a cena seguinte, mesma duração total.
3. [Geral] Trilha: trocar por algo mais calmo (interpretação).
   - Proposta: faixa de 80–95 BPM, sem bateria marcada; manter o volume sob a locução.

**Dúvidas**
1. Para a chefia: "Quando vocês falam do 'texto lá do meio', é o 'Conheça o plano' ou o 'Sem taxa de adesão'?"
   Minha proposta: "Sem taxa de adesão", que é o único no centro da tela.

**Observação**
- [00:12] "Garanta já a sua vaga" — letra "g" cortada pela máscara na saída; não foi pedido.

Dá ok ou me diz o que mudar.
```

Detalhes do formato:
- Cada item: uma linha com `[onde] Elemento: ação`, e logo abaixo de 1 a 4 subitens com os passos de execução — o que mexer, valores sugeridos (segundos, quadros, px, %, cor), o que manter. Escreva como um colega sênior explicaria, sem jargão desnecessário.
- Ordene pela ordem em que aparecem na peça; `[Geral]` no fim.
- **Dúvidas**: cada uma com a pergunta pronta para copiar e mandar ("Para a chefia: ...") e a sua proposta ("Minha proposta: ..."). Se a dúvida é algo que só o usuário sabe (arquivo que faltou, asset, qual versão segue), use "Para você: ...". Se não houver dúvida, escreva só "Nenhuma" — não escreva "Nenhuma" e depois liste uma.
- **Observação**: só se houver. Coisas que você viu mas ninguém pediu.
- Feche sempre com: `Dá ok ou me diz o que mudar.`

### 5. Depois do ok ou da correção

Se o usuário corrigir algo, reenvie a lista **inteira** atualizada (não só o trecho mudado). Se ele responder a uma dúvida, mova o item para Ajustes com a decisão. Se ele pedir, salve a lista final como `.md` na pasta de trabalho, sem sobrescrever versões anteriores.
