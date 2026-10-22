# Case 01 — Language Angels Scotland (V1 → V2)

Entrada: `case 01/V1.mp4` (1:56.36, 2560x1440, 25 fps). Tour de plataforma (gravação de tela + personagem animado). Só existe o MP4 final, sem projeto editável.

## Pedido (entrada do teste)

> Oi! Esse vídeo vai virar a versão Scotland. Mantém tudo igual (locução, música, cortes, duração) e muda só estes 4 pontos:
>
> 1. Esconder o ícone vermelho na lista.
> 2. Trocar a tela de Worksheets pela versão Scotland (SEND → ASN).
> 3. Mostrar a tabela de E&O preenchida (clique em First Level).
> 4. Final: logo "Scotland", URL /scot e QR novo.
>
> Comentários que já vieram nas rodadas anteriores, pra não repetir:
> - "Glitch na aba"
> - "Tabela desconfigurada"
> - "Escala não encaixa, coluna azul e logo mudam de tamanho"
> - "Cursor pula na transição"
> - "O vídeo trava no final"
> - "A cena anterior trava"

## Gabarito

**Ajustes**

1. [00:42–00:48] e [01:07–01:08] Lista de unidades (card "Las verduras / Vegetables"): esconder o ícone vermelho (círculo vermelho com olho branco, canto superior direito do card).
   - Localizar as duas aparições: 0:42.6–0:48.0 (lista rolando, cursor passando) e 1:07.3–1:08.2 (mesma lista, em plano mais aberto, durante a transição).
   - Fazer patch quadro a quadro (clone/limpeza com o fundo branco do card) acompanhando o scroll da lista; o ícone muda de posição a cada quadro, então o patch precisa ser rastreado, não fixo.
   - Manter intactos os chapéus amarelos (3 ícones de nível) logo abaixo do ícone, a borda do card e o check verde do card "La fruta".
   - Não mexer no cursor nem no destaque azul de "Los instrumentos"; não alterar tempo.
2. [01:16–01:26] Tela Lesson Plans/Worksheets: substituir a gravação pela versão Scotland do site, com o filtro "SEND" virando "ASN" e os arquivos "Flash Cards (ASN)" e "Writing Task (ASN)".
   - Regravar o mesmo percurso no site Scotland e encaixar nos mesmos tempos da V1: dissolve da cena da harpa 1:16.0–1:16.7; aba Lesson Plans até ~1:18.8; clique em Worksheets 1:18.8–1:19.1; filtros Writing 1:19.6, Listening 1:20.6, Reading 1:22.2, ASN 1:23.2, Other 1:24.6; clique em Songs & Lyrics 1:25.6 e corte para a página de vídeo em 1:25.8 (essa página não muda).
   - Reaplicar por cima o cursor (um só, contínuo, sem pular na entrada do dissolve) e o contorno verde de destaque do painel (entra em ~1:19.7 e fica até o corte).
   - Igualar a escala da nova captura à da V1 casando em pixels um elemento fixo (abas, botão "Download All", coluna/menus) entre as cenas; não pode haver salto de tamanho.
   - Garantir que nada da gravação V1 vaze junto com o cursor na aba ("glitch na aba") e que a grade de cards não quebre em linhas diferentes.
   - Não mexer no áudio, nos tempos dos cortes nem na cena da harpa.
3. [01:39–01:40] Tela "Update Pupil E&O Data": mostrar o clique em "First Level" e a tabela E&O preenchida.
   - Nova captura da mesma tela: cursor sai da lateral, vai até o botão "First Level" (~1:39.6–1:40.0), clique em ~1:40.0 e a tabela aparece preenchida (blocos "First Level / Listening and Talking / Reading / Writing" com as células verdes 1-01a, 1-01b...).
   - Segurar a tabela preenchida ~1 s a mais (na V2 a cena vai de 1:39.2 a 1:41.2, dissolve 1:41.2–1:41.6; na V1 o dissolve era 1:40.2–1:40.5).
   - Tirar esse tempo das cenas seguintes (tela de documentos e entrada da cena de jogos), para que a sincronia com a V1 volte em ~1:43.7 e a duração total do miolo não mude.
   - O dissolve de saída tem que acontecer com a cena ainda animada, não sobre frame congelado.
   - Não mexer no áudio; a tabela não pode aparecer desconfigurada (linhas quebradas).
4. [01:51–01:56] Cena final: trocar logo, URL e QR — logo "LANGUAGE ANGELS SCOTLAND", URL "www.languageangels.com/scot" e QR novo.
   - Refazer o cartão final (nuvens, "Try a 6-week free trial today!", depois URL + QR + anjinho) com o logo "LANGUAGE ANGELS SCOTLAND", mantendo a mesma animação: entrada por dissolve da cena do escritório, troca do texto pela URL/QR em ~1:54.2–1:54.6 e leve push-in.
   - Dar tempo de leitura ao cartão URL/QR: na V2 ele fica de 1:54.6 a ~1:58.9 (~3 s a mais que a V1), com fade suave no fim (V2: fade para preto 1:58.9–1:59.6).
   - Manter a música/VO originais; o vídeo passa a ter ~3 s a mais só no final (V2: 1:59.6).
   - Não alterar as cenas anteriores.

**Dúvidas para a chefia**
- QR novo: qual é o arquivo ou o link de destino? O pedido não traz o asset.
- Logo "Scotland": existe arte oficial do logo (ou do cartão final em After) ou é para montar com a tipografia atual?
- Capturas Scotland (Worksheets e E&O): quem fornece o acesso/login à plataforma Scotland, ou as gravações?
- O pedido diz "manter duração", mas o final precisa de tempo de leitura: pode estender o vídeo uns 3 s no fim (com o áudio já encerrado), ou o tempo tem que sair de outra cena?

## Notas de verificação

Método: frames extraídos com ffmpeg nos trechos, contact sheets com timecode, e diferença quadro a quadro V1×V2 (64x36, cinza) para achar onde as versões divergem. Áudio comparado por amostras: idêntico nas duas (stream de áudio de 116.36 s em ambas).

Trechos onde V2 difere da V1 (timecode V1, mesmo alinhamento até 1:39):
- 0:42.60–0:48.04 e 1:07.32–1:08.20 — ícone vermelho com olho no card "Las verduras" presente na V1 (visto em 0:44.5, 0:46.5, 0:47.9, 1:07.4, 1:07.8, ainda visível no dissolve em 1:08.1) e ausente na V2 nos mesmos tempos. Resto do quadro igual.
- 1:16.16–1:25.56 — nova captura. V1 mostra filtro "SEND", "Flash Cards (SEND)", "Writing Task (SEND)"; V2 mostra "ASN", "Flash Cards (ASN)", "Writing Task (ASN)". Eventos nos mesmos tempos nas duas (clique Worksheets 1:18.8, contorno verde ~1:19.7, troca de filtros 1:19.6 / 1:20.6 / 1:22.2 / 1:23.2 / 1:24.6, Songs & Lyrics 1:25.6–1:25.8). Página de vídeo Songs & Lyrics igual.
- 1:39.20–1:43.72 (V1) — V1: tabela E&O vazia (só nomes), dissolve para a tela de documentos 1:40.16–1:40.52, documentos até ~1:41.9, entrada da cena de jogos ~1:41.9–1:42.1. V2: cursor vai a "First Level", corte para tabela preenchida em 1:40.04, segura até 1:41.16, dissolve 1:41.16–1:41.56, documentos até 1:42.36, entrada da cena de jogos 1:42.36–1:42.7. Sincronia com a V1 restabelecida em ~1:43.7; de 1:43.7 a 1:50.7 V1 e V2 são idênticas no mesmo timecode.
- 1:50.72–fim — V1: dissolve para o cartão final 1:51.28–1:52.0, "LANGUAGE ANGELS", "Try a 6-week free trial today!", troca para "www.languageangels.com" + QR em 1:54.2–1:54.5, fade para azul-claro/branco 1:55.8–1:56.36 (URL/QR legível só ~1.3 s). V2: dissolve 1:50.72–1:51.3, "LANGUAGE ANGELS SCOTLAND", mesma frase, troca para "www.languageangels.com/scot" + QR com padrão diferente em 1:54.2–1:54.6, segura até ~1:58.9, fade para preto 1:58.9–1:59.6.

Mudanças na V2 que não estavam pedidas explicitamente:
- O dissolve para o cartão final começa ~0.56 s antes (1:50.72 na V2 × 1:51.28 na V1).
- O fade final é para preto (V1 terminava em azul-claro).
- Os últimos ~3.24 s da V2 (1:56.36–1:59.6) não têm áudio, porque a trilha original termina em 1:56.36.
- Para encaixar o +1 s da tabela E&O, a tela de documentos ficou mais curta (~1.4 s na V1 → ~0.8 s na V2) e a entrada da cena de jogos atrasou ~0.6 s.
- Na nova captura de Worksheets, os ícones dos cards mudaram (V1: editar + alerta; V2: dois botões redondos) e o painel ficou levemente acinzentado — consequência da versão atual do site, não de pedido.
- A aba Lesson Plans (1:16.7–1:18.8) também veio da nova captura, embora o pedido citasse só Worksheets.
