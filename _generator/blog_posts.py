# -*- coding: utf-8 -*-
"""
Artigos do blog da Bertoluchi.

Cada post tem: slug, title, meta_description, category, date, excerpt,
cta (label + href) e body. O body e uma lista de blocos; cada bloco pode
ter "h2" (subtitulo), "p" (lista de paragrafos) e "ul" (lista de itens).
O primeiro bloco, sem h2, e a introducao.

read_time_min e word_count sao calculados do texto real, no fim do arquivo.
Nenhum numero de mercado foi inventado: quando o texto cita dado da
agencia, ele vem de common.py (SITE, INFLUENCERS, SOCIAL_MEDIA_CLIENTS).
"""

GESTAO = "Gestão de Influenciadoras"
SOCIAL = "Social Media"
BRANDING = "Branding"
CONSULTORIA = "Consultoria"
MENTORIA = "Mentoria"

CTA_GESTAO = {"label": "Conhecer a gestão de influenciadoras",
              "href": "/servicos/gestao-de-influenciadores.html"}
CTA_SOCIAL = {"label": "Ver o serviço de social media",
              "href": "/servicos/social-media.html"}
CTA_BRANDING = {"label": "Ver o serviço de branding",
                "href": "/servicos/branding.html"}
CTA_CONSULTORIA = {"label": "Ver os formatos de consultoria",
                   "href": "/servicos/consultoria.html"}
CTA_MENTORIA = {"label": "Conhecer a mentoria",
                "href": "/servicos/mentoria.html"}

BLOG_POSTS = [

{
"slug": "como-escolher-influenciador-para-marca",
"title": "Como escolher a influenciadora certa para sua marca",
"meta_description": "Critérios práticos para escolher influenciadora: fit de nicho, engajamento real, valores da marca e os erros de quem decide só pelo número de seguidores.",
"category": GESTAO,
"date": "2026-09-05",
"excerpt": "Seguidor não é audiência. Os critérios que realmente preveem se uma parceria vai funcionar, e o erro que quase todo mundo comete na primeira contratação.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "A pergunta chega sempre no mesmo formato: quanto custa fechar com uma influenciadora que tem cem mil seguidores. É a pergunta errada, e ela explica boa parte das campanhas que não dão retorno.",
    "Escolher influenciadora é decisão de encaixe, não de tamanho. Uma criadora com público menor e muito bem definido costuma vender mais do que um perfil grande e genérico, porque quem a segue confia nela sobre um assunto específico. Abaixo estão os critérios que a gente usa na prática, na ordem em que eles importam."]},

  {"h2": "Nicho antes de alcance",
   "p": [
    "Comece descrevendo quem você quer atingir, com detalhe. Não vale dizer mulheres de 25 a 45 anos. Vale dizer quem faz depilação a laser pela primeira vez e tem medo de doer, ou quem procura clínica odontológica perto do trabalho no centro da cidade.",
    "Com essa descrição na mão, procure criadoras cujo conteúdo já conversa com aquela pessoa. Se o perfil precisa forçar a barra para encaixar seu produto, o público vai perceber. Conteúdo que soa deslocado não converte, e ainda queima a criadora com a audiência dela."]},

  {"h2": "Engajamento: o que olhar de verdade",
   "p": [
    "Curtida é o indicador mais fácil de inflar e o menos informativo. O que diz mais sobre uma audiência viva:"],
   "ul": [
    "Comentários com frase inteira, não só emoji, e principalmente perguntas sobre o produto ou o serviço",
    "Respostas da própria criadora nos comentários e no direct, sinal de relação real com quem segue",
    "Salvamentos e compartilhamentos, que mostram conteúdo com utilidade e não só entretenimento",
    "Constância: um perfil que publica toda semana há meses tem audiência mais previsível que um pico isolado",
    "Proporção entre visualizações de stories e número de seguidores, que revela quantos de fato acompanham"]},

  {"h2": "Perfil grande e perfil pequeno resolvem coisas diferentes",
   "p": [
    "Não existe tamanho melhor, existe tamanho adequado ao objetivo. Perfis grandes entregam alcance e servem quando o problema é que ninguém conhece sua marca. O custo é maior, a relação com a audiência costuma ser mais distante e a margem de negociação é menor.",
    "Perfis menores, com público bem delimitado, costumam entregar conversa. A audiência responde, pergunta e compra por indicação. Para negócio local que precisa de agenda cheia no mês seguinte, essa segunda opção quase sempre rende mais por real investido.",
    "Uma estratégia que funciona bem é combinar os dois: um perfil maior para dar visibilidade e alguns perfis menores da mesma região sustentando presença ao longo das semanas. O reconhecimento vem de um lado, a conversão do outro."]},

  {"h2": "Peça os números na fonte",
   "p": [
    "Antes de fechar, peça print do painel de métricas do perfil, com recorte de período. Você quer ver alcance, distribuição por cidade e faixa etária do público. Se o seu negócio atende só uma região, uma audiência espalhada pelo país inteiro vale muito menos do que o número bruto sugere.",
    "Criadora organizada entrega isso sem drama, geralmente dentro do mídia kit. Resistência para mostrar dado costuma ser o primeiro sinal amarelo da negociação.",
    "Olhe também a proporção entre seguidores e alcance médio das últimas publicações. Perfil que cresceu rápido por sorteio ou conteúdo viral solto costuma ter alcance muito abaixo do que o número de seguidores promete, porque a audiência veio pelo prêmio e não pelo assunto."]},

  {"h2": "Valores da marca e risco de imagem",
   "p": [
    "Sua marca vai aparecer ao lado de tudo o que aquele perfil publica, antes e depois da campanha. Olhe o histórico, o tipo de humor, as posições públicas, as outras marcas que a pessoa já representou.",
    "Um caso hipotético que ilustra bem: uma clínica que trabalha com discurso de autoestima e cuidado fecha com um perfil que faz piada com a aparência de outras pessoas. O alcance até vem, mas o público certo não compra, e parte dele passa a associar a clínica ao tom da piada.",
    "Vale conferir também se a criadora já divulgou concorrente direto seu nos últimos meses, e combinar exclusividade por categoria e prazo quando isso for relevante."]},

  {"h2": "Um checklist antes de assinar",
   "p": ["Antes de fechar qualquer parceria, tenha resposta clara para estes pontos:"],
   "ul": [
    "Qual é o objetivo da campanha, em uma frase: reconhecimento, consideração ou venda direta",
    "O que exatamente vai ser entregue, em número de peças, formato e prazo",
    "Quem aprova o conteúdo antes de publicar, e quantas rodadas de ajuste estão incluídas",
    "Por quanto tempo a publicação fica no ar e se a marca pode impulsionar ou reutilizar a peça",
    "Como o resultado vai ser medido: cupom, link rastreado, formulário ou aumento de procura direta"]},

  {"p": [
    "A parte mais cara de uma campanha malfeita não é o cachê. É o tempo que a equipe gasta produzindo, aprovando e depois tentando explicar por que não veio retorno.",
    "Se você prefere não tocar essa etapa sozinho, é exatamente o que fazemos: cuidamos da parte comercial de um grupo de criadoras e conectamos elas às marcas quando o encaixe existe de verdade."]},
],
},

{
"slug": "social-media-pequenos-negocios-por-onde-comecar",
"title": "Social media para pequenos negócios: por onde começar",
"meta_description": "Um roteiro de prioridades para quem tem pouco tempo e pouco orçamento: o que resolver primeiro nas redes sociais antes de pensar em contratar agência.",
"category": SOCIAL,
"date": "2026-08-28",
"excerpt": "Antes de aumentar a frequência de post ou contratar alguém, existe uma lista curta de coisas que quase todo pequeno negócio deixou pela metade.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "Quem toca um negócio pequeno não tem o problema de falta de ideia para post. Tem o problema de falta de tempo, e de não saber qual esforço traz retorno primeiro.",
    "A boa notícia é que existe uma ordem. As tarefas abaixo custam pouco, resolvem em poucas horas e melhoram o resultado de tudo o que vier depois. Fazer post novo antes de resolver essa base é jogar alcance fora."]},

  {"h2": "Primeiro: arrume o perfil, não o feed",
   "p": [
    "O perfil é a página de vendas que todo mundo visita antes de decidir. Ele precisa responder em cinco segundos o que você faz, para quem, onde fica e como comprar.",
    "Na prática, isso significa:"],
   "ul": [
    "Nome de usuário e campo de nome com a palavra que as pessoas de fato buscam, por exemplo o serviço mais a cidade",
    "Bio que diz o que você resolve, não adjetivos sobre sua empresa",
    "Endereço e horário atualizados, com link que abre o WhatsApp já com mensagem pronta",
    "Destaques organizados por dúvida real: preço, como funciona, antes e depois, perguntas frequentes"]},

  {"h2": "Segundo: decida quem você quer atrair",
   "p": [
    "Escolher o público parece etapa de empresa grande, mas é o que evita o conteúdo genérico que não fala com ninguém. Escreva em uma frase quem é o cliente que você mais quer, e o que passa pela cabeça dele antes de comprar.",
    "Quase toda dúvida boa de conteúdo sai daí: quanto custa, dói, quanto tempo dura, funciona no meu caso, vocês atendem no meu bairro. Cada uma dessas é um post."]},

  {"h2": "Terceiro: escolha uma rede só",
   "p": [
    "Estar em quatro redes fazendo o mínimo é pior do que estar em uma fazendo bem feito. Escolha a rede onde seu cliente já está e onde você consegue manter o ritmo.",
    "Para a maioria dos negócios locais de serviço, isso é o Instagram somado ao perfil no Google, que é o que aparece quando alguém busca pelo serviço mais o nome da cidade. Esse segundo costuma ser esquecido e responde por muita procura direta."]},

  {"h2": "Quarto: produza em bloco, publique aos poucos",
   "p": [
    "O erro que mais derruba consistência é tentar criar conteúdo no dia da publicação. Separe uma tarde por mês, grave e fotografe várias coisas de uma vez, e vá publicando ao longo das semanas.",
    "Um formato simples que funciona: para cada semana, um post que ensina algo, um que mostra o trabalho sendo feito e um que fala diretamente da oferta. Não precisa ser mais sofisticado que isso no começo."]},

  {"h2": "Quinto: registre o que traz cliente",
   "p": [
    "Sem isso, você fica refém de curtida. Basta perguntar a cada pessoa que chega como ela ouviu falar de você, e anotar. Em um mês você já sabe se o esforço nas redes está virando conversa, e qual tipo de post puxa mais.",
    "Esse registro simples vale mais do que qualquer painel de métricas no começo, porque conecta conteúdo a dinheiro."]},

  {"h2": "O que não vale a pena no começo",
   "p": [
    "Tão importante quanto a lista do que fazer é a lista do que adiar. No início, estas coisas consomem tempo e devolvem pouco:"],
   "ul": [
    "Perseguir número de seguidores, que sobe com sorteio e desce com a mesma facilidade, sem virar cliente",
    "Produção cara de vídeo antes de saber qual assunto interessa ao seu público",
    "Copiar o conteúdo de uma marca nacional, que fala com outra realidade e outro volume",
    "Abrir perfil em rede nova só porque apareceu, antes de dar conta da primeira",
    "Impulsionar post aleatório sem saber o que você quer que a pessoa faça depois de clicar"]},

  {"h2": "Quando faz sentido contratar alguém",
   "p": [
    "Contratar ajuda quando a base já está de pé e o gargalo virou tempo ou repertório, não estratégia. Se o perfil ainda não explica o que você vende, terceirizar produção só vai gerar mais post confuso, com mais custo.",
    "Um bom teste é olhar para o motivo real. Se a resposta for que você não tem tempo de executar algo que já sabe que funciona, contratar resolve. Se a resposta for que você não sabe o que postar, o que falta é direcionamento, e isso se resolve antes e mais barato.",
    "Hoje cuidamos das redes de dezoito negócios, cada um com estratégia própria. O que separa os que crescem dos que travam quase nunca é orçamento, é ter resolvido essa base antes."]},
],
},

{
"slug": "o-que-e-branding",
"title": "O que é branding e por que sua empresa precisa de um",
"meta_description": "A diferença entre ter uma logo e ter uma marca, e o momento em que branding deixa de ser questão de estética e vira decisão de negócio.",
"category": BRANDING,
"date": "2026-08-20",
"excerpt": "Logo é um desenho. Marca é o que as pessoas esperam de você antes de te conhecer. Confundir os dois custa caro na hora de crescer.",
"cta": CTA_BRANDING,
"body": [
  {"p": [
    "Branding é uma dessas palavras que aparecem em toda proposta comercial e quase nunca vêm explicadas. Vale desarmar o termo, porque a confusão em torno dele leva empresa a gastar com a coisa errada.",
    "Resumindo sem rodeio: logo é um desenho, identidade visual é o conjunto de elementos gráficos, e branding é o trabalho de definir o que sua empresa significa para quem compra. O desenho é consequência, não ponto de partida.",
    "A confusão tem uma consequência prática. Empresa que acha que branding é arte contrata um logotipo bonito, aplica em tudo e continua com o mesmo problema de antes: cliente que não entende o que ela faz, vendedor que explica de um jeito diferente a cada conversa, e disputa de preço com quem cobra menos."]},

  {"h2": "O teste de uma frase",
   "p": [
    "Pergunte a três pessoas da sua equipe o que a empresa faz e por que alguém deveria escolher vocês. Se vierem três respostas diferentes, o problema não está no logotipo.",
    "Marca é justamente essa resposta, repetida de forma consistente em todo lugar onde alguém encontra você: a vitrine, o atendimento no WhatsApp, a legenda do post, a embalagem, o jeito de resolver reclamação."]},

  {"h2": "O que um trabalho de branding define",
   "p": ["Antes de qualquer arte, o trabalho precisa fechar quatro pontos:"],
   "ul": [
    "Posicionamento: qual lugar você quer ocupar na cabeça do cliente, e contra quem você está sendo comparado",
    "Público: quem você atende de fato, e quem você prefere não atender",
    "Personalidade e voz: como a marca fala, o que ela nunca diria, o nível de formalidade",
    "Promessa: o que o cliente pode esperar sempre, em qualquer ponto de contato"]},

  {"h2": "Só então vem a parte visual",
   "p": [
    "Com essas decisões tomadas, a identidade visual vira execução com critério: logotipo, paleta, tipografia, elementos de apoio e um manual que diz como aplicar tudo isso.",
    "O manual é a peça que mais se ignora e de que mais se sente falta depois. Sem ele, cada pessoa que produz material faz uma versão diferente da marca, e em um ano você tem cinco tons de laranja circulando."]},

  {"h2": "Quando branding vira decisão de negócio",
   "p": [
    "Existem momentos em que adiar sai mais caro do que fazer. Os mais comuns:"],
   "ul": [
    "Você compete com quem cobra mais barato e só consegue argumentar preço",
    "A empresa mudou de produto, de público ou de porte e a comunicação ficou no estágio anterior",
    "Vai abrir segunda unidade, franquear ou entrar em outra cidade e precisa que a experiência seja igual",
    "Você contratou equipe e cada pessoa comunica a empresa de um jeito",
    "Vai investir em tráfego pago, quando marca fraca faz o custo por resultado subir"]},

  {"h2": "Como é o processo, do começo ao fim",
   "p": [
    "Um projeto de branding costuma seguir quatro etapas, e nenhuma delas começa no computador de desenho.",
    "A primeira é diagnóstico: entender o negócio, ouvir quem vende, olhar o que os concorrentes comunicam e mapear como a marca aparece hoje. A segunda é estratégia, onde se fecham posicionamento, público, voz e promessa. É a etapa que mais gera desconforto, porque obriga a escolher e a abrir mão de agradar todo mundo.",
    "A terceira é a construção visual e verbal, que traduz essas decisões em logotipo, paleta, tipografia, elementos de apoio e jeito de escrever. A quarta é a aplicação, que leva tudo isso para os lugares onde o cliente encontra a marca, com o manual dizendo como manter a coerência."]},

  {"h2": "Rebranding não é começar do zero",
   "p": [
    "Empresa com anos de história tem patrimônio acumulado, mesmo quando a comunicação está desatualizada. Jogar fora tudo o que o público já reconhece é destruir valor sem necessidade.",
    "O trabalho, nesses casos, é decidir o que preserva e o que atualiza. Muitas vezes a cor e o símbolo ficam, e o que muda é o modo de aplicar, a tipografia e o discurso. A mudança pode ser gradual, com o público sendo levado junto, em vez de acordar um dia com outra empresa na frente dele."]},

  {"h2": "O sinal de que funcionou",
   "p": [
    "Branding bem feito não se mede por elogio ao logotipo novo. Mede-se por conversa de venda mais curta, por cliente que chega já sabendo o que você faz, e por conseguir sustentar preço sem precisar justificar tanto.",
    "Já entregamos mais de duzentos brandings, e o padrão se repete: as marcas que sentem mudança real são as que trataram o projeto como decisão de negócio, não como troca de arte."]},
],
},

{
"slug": "quantas-vezes-postar-redes-sociais",
"title": "Quantas vezes por semana postar nas redes sociais",
"meta_description": "Frequência não é o que decide o resultado nas redes sociais. Como definir uma cadência que você consegue manter, e o que importa mais do que volume.",
"category": SOCIAL,
"date": "2026-08-13",
"excerpt": "A pergunta sobre frequência esconde outra, mais útil: qual ritmo você consegue sustentar por seis meses sem baixar a qualidade.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "Poucas perguntas geram tanta ansiedade quanto essa, e poucas têm resposta tão pouco universal. A verdade desconfortável é que não existe número certo, existe número sustentável.",
    "Quem publica todo dia por três semanas e some por dois meses tem resultado pior do que quem publica duas vezes por semana o ano inteiro. Vale entender por quê, e depois definir a sua cadência.",
    "Vale dizer também de onde vem a ansiedade. Ela costuma nascer de comparação com perfil que tem estrutura diferente da sua: equipe de conteúdo, orçamento de produção e alguém dedicado só a isso. Comparar sua cadência com a de quem tem outra realidade produz culpa, não resultado."]},

  {"h2": "Por que consistência ganha de volume",
   "p": [
    "As redes distribuem conteúdo com base em sinal recente. Um perfil que some perde a referência que o algoritmo tinha sobre quem gosta daquele conteúdo, e a retomada custa semanas.",
    "Tem também o lado humano: audiência é hábito. Quem aparece com regularidade vira parte da rotina de quem segue. Quem aparece em rajada vira ruído, e depois esquecimento.",
    "E existe o efeito acumulado. Conteúdo bom continua sendo encontrado depois de publicado, principalmente o que responde dúvida. Um acervo construído devagar rende mais do que um pico."]},

  {"h2": "Como achar sua cadência",
   "p": [
    "Faça a conta pelo pior mês do ano, não pelo melhor. Pense na semana mais cheia, aquela com viagem, imprevisto e equipe reduzida. Quanto você consegue publicar naquela semana, mantendo qualidade?",
    "Esse é o seu piso, e é o número que você promete. Tudo acima disso é bônus. É muito melhor combinar dois posts por semana e às vezes entregar quatro do que prometer diário e falhar na terceira semana."]},

  {"h2": "Pontos de partida realistas",
   "p": ["Se você precisa de um número para começar, use estes como referência e ajuste depois de um mês:"],
   "ul": [
    "Negócio local com uma pessoa cuidando de tudo: dois posts por semana no feed e stories nos dias de atendimento",
    "Negócio com alguém dedicado a conteúdo: três a quatro posts por semana e stories quase diários",
    "Equipe ou agência cuidando: quatro a cinco posts por semana, com formatos variados e produção em bloco",
    "Perfil pessoal de criadora: ritmo maior, porque a presença é o próprio produto"]},

  {"h2": "O que importa mais do que a frequência",
   "p": [
    "Antes de aumentar o número de publicações, verifique se estes pontos estão resolvidos. Eles mudam mais o resultado do que dobrar o volume:"],
   "ul": [
    "Os primeiros três segundos do vídeo, ou a primeira linha da legenda, que decidem se alguém para",
    "Clareza sobre o que a pessoa deve fazer depois de ver o post",
    "Variedade de formato, para não cansar quem já segue",
    "Resposta a comentário e direct, que é conteúdo tanto quanto o post"]},

  {"h2": "Feed e stories têm ritmos diferentes",
   "p": [
    "Misturar os dois na mesma conta atrapalha a decisão. O feed é acervo: fica, é encontrado depois, sustenta a impressão de quem visita seu perfil pela primeira vez. Por isso ele pede menos volume e mais cuidado.",
    "Stories são presença do dia. Somem em vinte e quatro horas, falam com quem já segue e servem para bastidor, aviso, enquete e resposta a dúvida. Ali a frequência pode ser bem maior sem exigir produção pesada, porque a expectativa de acabamento é outra.",
    "Uma divisão que costuma funcionar: poucos posts bem feitos no feed e presença frequente nos stories. Muita gente faz o contrário, gasta a energia toda no feed e some do dia a dia de quem já demonstrou interesse."]},

  {"h2": "Quando faz sentido pausar",
   "p": [
    "Existe hora de reduzir de propósito, e isso não é fracasso. Período de operação sobrecarregada, mudança de posicionamento em andamento ou equipe reduzida são motivos legítimos para baixar o ritmo.",
    "O que não funciona é sumir sem avisar. Reduza a cadência de forma explícita, mantenha ao menos um ponto de contato por semana, e avise nos stories que a rotina de conteúdo vai mudar por um tempo. Audiência entende pausa combinada, mas não entende abandono."]},

  {"h2": "Ajuste com dado, não com sensação",
   "p": [
    "Depois de trinta dias, olhe quais publicações trouxeram salvamento, compartilhamento e conversa no direct. Faça mais daquilo e corte o que só gerou curtida.",
    "Frequência é uma alavanca, e nem sempre é a que está travando. Quando assumimos as redes de um cliente, quase sempre o primeiro ganho vem de arrumar formato e clareza, não de publicar mais."]},
],
},

{
"slug": "marketing-de-influencia-como-funciona",
"title": "Marketing de influência: como funciona e vale a pena?",
"meta_description": "Como uma parceria com influenciadora é estruturada de verdade, do briefing à medição, e como avaliar se o investimento faz sentido para o seu negócio.",
"category": GESTAO,
"date": "2026-08-06",
"excerpt": "Entre o primeiro contato e a publicação existe um processo com etapas bem definidas. Conhecer esse processo é o que separa parceria de aposta.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "Marketing de influência costuma ser explicado de um jeito que não ajuda: pagar alguém com audiência para falar do seu produto. Descrito assim, parece loteria, e muita gente contrata como tal.",
    "Uma parceria bem estruturada tem etapas, entregas escritas e forma de medição combinada antes. É isso que faz a diferença entre investimento e aposta.",
    "O que sustenta esse tipo de campanha é simples de entender: as pessoas confiam mais na indicação de alguém que acompanham do que em um anúncio. A criadora empresta credibilidade construída ao longo de anos. Por isso mesmo, o cuidado com quem representa a marca precisa ser proporcional ao que está sendo emprestado."]},

  {"h2": "Como funciona na prática",
   "p": ["Uma campanha bem conduzida passa por estas fases:"],
   "ul": [
    "Objetivo: definir se a meta é reconhecimento, consideração ou venda, porque isso muda quem contratar e o que pedir",
    "Seleção: buscar perfis com encaixe de público e checar métricas na fonte, não pelo número de seguidores",
    "Briefing: passar o que não pode faltar, o que não pode ser dito, e deixar o formato com quem conhece a audiência",
    "Negociação: fechar entregas, prazo, exclusividade, direito de uso da peça e valor",
    "Produção e aprovação: revisar antes de publicar, com número de ajustes combinado",
    "Publicação e medição: acompanhar com link rastreado ou cupom e comparar com o objetivo inicial"]},

  {"h2": "O erro de escrever o roteiro inteiro",
   "p": [
    "A tentação é mandar o texto pronto para a criadora ler. É justamente o que destrói o resultado, porque o público reconhece na hora quando a fala não é dela.",
    "O que funciona é entregar o essencial e soltar a forma: o que o produto resolve, os pontos que precisam aparecer, o que não pode ser prometido, e o que a pessoa deve fazer depois. O jeito de dizer é o que você está contratando."]},

  {"h2": "Vale a pena para o seu caso?",
   "p": [
    "Costuma valer quando o produto se explica melhor sendo mostrado do que descrito, quando existe barreira de confiança que uma recomendação derruba, ou quando você precisa alcançar um público específico difícil de comprar por anúncio.",
    "Costuma não valer quando não há estrutura para receber a demanda. Campanha boa em operação despreparada gera cliente irritado. Antes de contratar alcance, garanta que o WhatsApp é respondido, que a agenda comporta e que o estoque existe."]},

  {"h2": "Os formatos mais comuns de acordo",
   "p": [
    "Nem toda parceria é cachê fixo por publicação. Vale conhecer os formatos, porque cada um serve a um momento diferente:"],
   "ul": [
    "Cachê por entrega, o mais direto: valor combinado por um conjunto definido de peças e prazo",
    "Permuta, quando o produto tem valor percebido alto, funciona melhor com perfis em crescimento e produto que a pessoa usaria de verdade",
    "Contrato por período, com presença recorrente ao longo de meses, que constrói associação entre marca e criadora",
    "Comissão por venda, com cupom ou link próprio, que costuma complementar o cachê e raramente o substitui bem",
    "Embaixadora, formato mais longo e com exclusividade de categoria, para marcas que já validaram o encaixe"]},

  {"h2": "Como saber se deu certo",
   "p": [
    "Defina a medição antes de publicar, nunca depois. Cupom exclusivo por criadora, link com parâmetro de rastreio, ou pergunta no atendimento sobre como a pessoa chegou.",
    "E compare com o objetivo que você escreveu no começo. Campanha de reconhecimento cobrada por venda imediata sempre vai parecer fracasso, mesmo tendo funcionado. Uma coisa é constância de presença, outra é conversão em sete dias.",
    "Vale ainda considerar o prazo. Uma publicação isolada raramente muda o jogo. Presença repetida com o mesmo perfil ao longo de meses constrói associação, e é aí que o retorno costuma aparecer."]},

  {"h2": "O que costuma dar errado",
   "p": [
    "Os problemas se repetem, e quase todos nascem antes da publicação. Vale conhecer para evitar:"],
   "ul": [
    "Aprovar em cima da hora, o que empurra a criadora a publicar sem revisão ou a atrasar a campanha",
    "Não combinar direito de uso e depois querer usar a peça em anúncio pago sem ter previsto isso",
    "Concentrar tudo em um único perfil, o que transforma a campanha inteira em aposta num só resultado",
    "Pedir número de vendas de uma campanha pensada para apresentar a marca a quem nunca ouviu falar dela",
    "Sumir depois da publicação, sem acompanhar comentário e direct, que é onde a dúvida de compra aparece"]},

  {"p": [
    "É essa estrutura que colocamos de pé quando fazemos a ponte entre marca e criadora: briefing claro, entregas escritas, medição combinada e acompanhamento depois da publicação."]},
],
},

{
"slug": "erros-comuns-instagram-empresas-locais",
"title": "5 erros comuns no Instagram de empresas locais",
"meta_description": "Cinco falhas que aparecem no Instagram da maioria dos negócios locais, e como corrigir cada uma sem precisar produzir mais conteúdo.",
"category": SOCIAL,
"date": "2026-07-30",
"excerpt": "Nenhum deles tem a ver com falta de conteúdo. São falhas de base que fazem o esforço de publicação render menos do que poderia.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "Quando olhamos o perfil de um negócio local pela primeira vez, os mesmos problemas aparecem quase sempre. Não são erros de gosto, e nenhum deles se resolve postando mais.",
    "A lista abaixo é a que costuma dar mais retorno em menos tempo, porque cada item melhora o desempenho de todo conteúdo que já existe e de tudo o que vier depois."]},

  {"h2": "1. A bio não diz o que a empresa faz",
   "p": [
    "É o erro mais frequente e o mais caro. Bios cheias de frase de efeito, emoji e adjetivo, sem dizer qual serviço a empresa presta e em que cidade ela atende.",
    "Quem chega no seu perfil vindo de uma indicação ou de uma busca tem poucos segundos de paciência. Se em cinco segundos a pessoa não entende o que você vende e se você atende a região dela, ela sai.",
    "A correção é direta: primeira linha com o serviço e a cidade, segunda linha com o que diferencia, terceira com a instrução de contato. Guarde a poesia para as legendas."]},

  {"h2": "2. Direct e comentário sem resposta",
   "p": [
    "Muita empresa trata rede social como vitrine e esquece que ela também é balcão. A pessoa pergunta o preço no comentário, ninguém responde, e ela vai perguntar para o concorrente.",
    "Responder rápido não é só educação, é conversão. E responder em público, quando a pergunta é comum, ainda economiza tempo, porque a próxima pessoa com a mesma dúvida já encontra a resposta ali.",
    "Se o volume de mensagem passou do que você dá conta, use respostas rápidas salvas para as perguntas repetidas e reserve dois momentos fixos do dia para limpar a caixa."]},

  {"h2": "3. Feed sem identidade visual",
   "p": [
    "Cada post com uma fonte, uma cor de fundo e um estilo de foto diferente. O conteúdo pode até ser bom, mas o conjunto passa impressão de improviso, e impressão de improviso encarece a venda.",
    "Não é preciso um manual de marca completo para melhorar isso. Escolha duas ou três cores, uma fonte para título e uma para texto, e um tratamento padrão de foto. Repita. A repetição é o que faz alguém reconhecer seu post no meio da rolagem, antes de ler o nome do perfil."]},

  {"h2": "4. Só falar de si mesmo",
   "p": [
    "Perfil que só publica promoção, foto de produto e aviso de horário cansa. A pessoa segue por interesse no assunto, não por interesse em ser vendida todo dia.",
    "A proporção que funciona bem para negócio local é maioria de conteúdo que ajuda ou mostra bastidor, e uma parte menor de oferta direta. Conteúdo que responde dúvida antes da compra faz o trabalho de venda sozinho, sem parecer venda.",
    "Bastidor rende mais do que parece: como o serviço é feito, o cuidado com o material, a equipe trabalhando. É o que constrói a confiança que a foto de produto sozinha não constrói."]},

  {"h2": "5. Nenhuma instrução clara do que fazer",
   "p": [
    "O post termina, a pessoa gostou, e não fica claro qual é o próximo passo. Sem instrução, ela rola para o próximo conteúdo e a intenção se perde.",
    "Toda publicação deve terminar dizendo o que fazer: chamar no WhatsApp, salvar para depois, comentar uma palavra, visitar a loja. Uma instrução por post, sempre a mais relevante para aquele conteúdo.",
    "Vale conferir também se o caminho que você indica funciona. Link quebrado na bio, WhatsApp que ninguém acompanha e endereço desatualizado desperdiçam todo o esforço anterior."]},

  {"h2": "Um erro extra que vale citar: ignorar a busca local",
   "p": [
    "Muita empresa capricha no Instagram e esquece que boa parte das pessoas procura serviço digitando o que precisa mais o nome da cidade. Quem não aparece nessa busca perde cliente que já estava decidido a comprar.",
    "Manter o perfil da empresa no Google atualizado, com endereço, horário, telefone, fotos recentes e respostas às avaliações, costuma trazer procura direta com esforço muito menor do que produzir conteúdo novo.",
    "Os dois se reforçam: quem encontra a empresa na busca frequentemente confere o Instagram antes de ligar. Um perfil organizado fecha o que a busca abriu."]},

  {"h2": "Como priorizar a correção",
   "p": [
    "Corrigir tudo de uma vez costuma não acontecer. Uma ordem que funciona bem, do que dá retorno mais rápido para o que exige mais trabalho:"],
   "ul": [
    "Bio e link de contato, que levam minutos e afetam todo visitante novo",
    "Fila de mensagens e comentários sem resposta, onde há intenção de compra parada",
    "Perfil no Google atualizado, com horário e fotos recentes",
    "Destaques reorganizados por dúvida real, aproveitando conteúdo que já existe",
    "Padrão visual dos próximos posts, sem refazer o que já foi publicado"]},

  {"h2": "Por onde começar",
   "p": [
    "Se você só tiver uma hora nesta semana, use na bio e nas respostas pendentes. São os dois itens que transformam interesse existente em conversa, sem exigir produção nova.",
    "O resto pode ser feito ao longo do mês, um item por semana. Corrigir esses cinco pontos costuma render mais do que dobrar a quantidade de publicações.",
    "Vale repetir a checagem a cada trimestre. Horário muda, serviço novo entra, link quebra, e o perfil volta a desalinhar sem ninguém perceber."]},
],
},

{
"slug": "como-criar-calendario-editorial",
"title": "Como criar um calendário editorial eficiente",
"meta_description": "Passo a passo para montar um calendário editorial que você consegue manter: pilares de conteúdo, cadência, datas do negócio e produção em bloco.",
"category": SOCIAL,
"date": "2026-07-23",
"excerpt": "Calendário editorial não é planilha bonita. É a decisão, tomada antes, sobre o que publicar, para não decidir isso no dia com pressa.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "A maior parte do desgaste com redes sociais não vem de produzir conteúdo. Vem de decidir o que produzir, toda vez, do zero, geralmente em cima da hora.",
    "O calendário editorial existe para tirar essa decisão do dia a dia. Bem montado, ele responde antes o que vai ao ar, em qual formato e com qual objetivo, e libera sua energia para a execução."]},

  {"h2": "Passo 1: defina seus pilares de conteúdo",
   "p": [
    "Pilar é um assunto recorrente que sua marca trata. Três ou quatro bastam, e eles precisam sair do cruzamento entre o que você vende e o que seu público quer saber.",
    "Uma clínica de estética, por exemplo, poderia trabalhar com procedimentos explicados, cuidados em casa, bastidor do atendimento e resultados. Um restaurante poderia usar pratos, origem dos ingredientes, equipe e rotina da casa.",
    "Com os pilares definidos, a pergunta deixa de ser o que postar hoje e passa a ser qual pilar toca agora. É uma pergunta muito mais fácil de responder."]},

  {"h2": "Passo 2: estabeleça a cadência que você sustenta",
   "p": [
    "Defina quantas publicações por semana, em quais dias, e em quais formatos. Use como base a sua semana mais cheia do ano, não a mais tranquila.",
    "Distribua os pilares nessa grade de modo que nenhum domine. Se a oferta direta aparece em todos os dias, o perfil vira panfleto. Se ela nunca aparece, o público não sabe que você vende."]},

  {"h2": "Passo 3: marque as datas que são do seu negócio",
   "p": [
    "Antes de olhar calendário de datas comemorativas genéricas, marque o que é seu: início de temporada, mês de maior movimento, aniversário da empresa, lançamento, período de férias, promoção que você já sabe que vai fazer.",
    "Datas comemorativas genéricas só entram se tiverem ligação real com o negócio. Post de data que não tem nada a ver com o que você faz ocupa espaço e não constrói nada."]},

  {"h2": "Passo 4: produza em bloco",
   "p": [
    "Com o calendário preenchido, agrupe o que é parecido. Grave todos os vídeos do mês no mesmo dia, fotografe tudo de uma vez, escreva as legendas em sequência.",
    "Trocar de tipo de tarefa custa tempo e energia. Uma tarde de gravação rende mais do que quatro gravações soltas de trinta minutos, e a qualidade fica mais uniforme porque a luz, a roupa e o cenário são os mesmos."]},

  {"h2": "Ferramentas: as mais simples bastam",
   "p": [
    "Não é preciso software especializado. O que importa é que a ferramenta esteja onde você já trabalha e que a equipe consiga abrir:"],
   "ul": [
    "Uma planilha com colunas de data, pilar, formato, status, legenda e responsável resolve a maioria dos casos",
    "Um quadro de tarefas funciona bem quando mais de uma pessoa produz e é preciso ver o que está travado",
    "O próprio calendário do celular serve para o negócio de uma pessoa só, com lembrete no dia da produção",
    "Uma pasta na nuvem com os arquivos separados por mês evita o retrabalho de procurar foto antiga"]},

  {"h2": "Equilibre conteúdo institucional e oferta",
   "p": [
    "Essa é a decisão que mais gera dúvida na hora de preencher a grade. Publicar só oferta cansa e derruba alcance. Publicar só conteúdo útil constrói audiência que não sabe que você vende.",
    "Uma divisão que funciona para a maioria dos negócios: a maior parte das publicações ajudando, ensinando ou mostrando bastidor, uma parte menor falando diretamente da oferta, e um espaço para prova social, que é o cliente satisfeito, o resultado, o depoimento.",
    "A prova social é a ponte entre os dois. Ela vende sem parecer venda, porque quem fala não é a empresa. Se você tem clientes dispostos a dar depoimento, esse é o conteúdo mais subaproveitado que existe."]},

  {"h2": "Quem faz o quê",
   "p": [
    "Calendário sem responsável definido não sai do papel. Mesmo em operação de uma pessoa só, vale separar os papéis por tarefa, porque isso muda o tipo de atenção exigido.",
    "Quem decide o tema, quem grava ou fotografa, quem escreve a legenda, quem aprova e quem publica. Quando essas funções não estão claras, o conteúdo trava na etapa de aprovação, que é onde a maioria dos calendários morre.",
    "Combine também o prazo de aprovação. Sem prazo, a revisão vira gargalo e o calendário perde a data que justificava a publicação."]},

  {"h2": "Deixe espaço para o improviso",
   "p": [
    "Calendário rígido demais quebra na primeira semana. Reserve um espaço por semana para o que surgir: um cliente satisfeito, um bastidor inesperado, uma dúvida que apareceu no direct.",
    "Esse conteúdo não planejado costuma ser o que mais engaja, justamente porque é atual. O calendário garante o piso, e o improviso é o que acrescenta.",
    "Revise a grade uma vez por mês, olhando o que teve melhor desempenho. O calendário do mês seguinte deve refletir o que você aprendeu, não repetir o anterior por inércia."]},
],
},

{
"slug": "identidade-visual-vs-branding",
"title": "Identidade visual vs. branding: qual a diferença",
"meta_description": "Identidade visual e branding não são a mesma coisa. O que cada um resolve, por que a ordem entre eles importa e como saber do que sua empresa precisa agora.",
"category": BRANDING,
"date": "2026-07-16",
"excerpt": "Os dois termos são usados como sinônimo em quase toda proposta comercial. Não são, e a confusão faz empresa comprar a coisa errada.",
"cta": CTA_BRANDING,
"body": [
  {"p": [
    "Identidade visual e branding aparecem juntos com tanta frequência que viraram quase a mesma palavra. Separar os dois ajuda a contratar melhor e a cobrar a entrega certa.",
    "A forma mais curta de dizer: branding é a estratégia que define o que a marca significa. Identidade visual é a parte gráfica que traduz essa decisão em algo que se vê."]},

  {"h2": "O que a identidade visual entrega",
   "p": [
    "Identidade visual é o sistema gráfico da marca. Ela é tangível, se vê e se aplica:"],
   "ul": [
    "Logotipo e suas versões para diferentes usos e fundos",
    "Paleta de cores, com os códigos exatos para tela e impressão",
    "Tipografia, com as fontes de título e de texto e como combiná-las",
    "Elementos de apoio: grafismos, ícones, tratamento de foto",
    "Manual com as regras de aplicação, incluindo o que não se pode fazer"]},

  {"h2": "O que o branding entrega",
   "p": [
    "Branding é anterior e menos visível. Ele responde perguntas que não têm resposta gráfica:"],
   "ul": [
    "Para quem essa marca existe, e para quem ela não existe",
    "Que lugar ela quer ocupar na cabeça de quem compara opções",
    "O que ela promete entregar sempre, em qualquer ponto de contato",
    "Como ela fala, que tom usa e o que nunca diria",
    "O que a torna diferente de forma sustentável, além de preço"]},

  {"h2": "Por que a ordem importa",
   "p": [
    "Fazer identidade visual sem branding é escolher roupa sem saber para onde se vai. O resultado pode até ficar bonito, mas as escolhas ficam sem critério, e discussão sem critério vira discussão de gosto pessoal.",
    "Quando a estratégia existe antes, cada decisão gráfica tem uma justificativa que não depende de opinião. A cor não é escolhida por ser bonita, é escolhida porque a marca precisa transmitir seriedade e se diferenciar de dois concorrentes que já usam verde.",
    "Isso também encurta a aprovação. Em vez de rodadas infinitas de ajuste por preferência, a conversa passa a ser se a peça cumpre o que a estratégia definiu."]},

  {"h2": "Uma comparação que ajuda",
   "p": [
    "Pense em uma pessoa que você conhece bem. O branding dela é o caráter: o que ela valoriza, como trata os outros, o que ela jamais faria, aquilo que faz você confiar nela. A identidade visual é a aparência: o corte de cabelo, a roupa, o jeito de se apresentar.",
    "A aparência ajuda a reconhecer e comunica algo real sobre a pessoa. Mas ninguém constrói confiança de longo prazo só com aparência, e ninguém muda de caráter trocando de roupa.",
    "Com marca é igual. A identidade visual faz você ser reconhecido e transmite uma primeira impressão coerente. O branding é o que faz alguém continuar escolhendo você depois da primeira compra."]},

  {"h2": "O que acontece quando só o visual é resolvido",
   "p": [
    "É a situação mais comum do mercado, porque o visual é o que se vê e o que se vende como projeto. A empresa investe em logotipo novo, aplica em tudo, e alguns meses depois percebe que nada mudou na operação.",
    "Os sintomas são reconhecíveis: o time comercial continua improvisando a explicação do que a empresa faz, cada campanha comunica uma promessa diferente, e a disputa com concorrente segue sendo por preço.",
    "Nada disso é culpa do designer. São perguntas que o projeto gráfico não tinha como responder, porque não são perguntas gráficas."]},

  {"h2": "Dá para fazer só um dos dois?",
   "p": [
    "Dá, e às vezes é o certo. Uma empresa com posicionamento claro, discurso alinhado e equipe que sabe explicar o que vende pode precisar apenas de atualização visual.",
    "O inverso também acontece: empresa com visual resolvido e recente, mas que não consegue explicar por que alguém deveria escolhê-la. Aí o trabalho é de estratégia, e mexer no logotipo seria desperdício."]},

  {"h2": "Como saber do que você precisa",
   "p": [
    "Um teste rápido: peça a três pessoas da equipe que expliquem, em uma frase, o que a empresa faz e por que escolher vocês. Depois olhe cinco materiais recentes lado a lado.",
    "Se as respostas divergem, o que falta é branding. Se as respostas batem mas os materiais parecem de empresas diferentes, o que falta é identidade visual e um manual que garanta a aplicação.",
    "Se os dois problemas aparecem, comece pela estratégia. Ela é mais barata de refazer no papel do que depois de aplicada em fachada, embalagem e uniforme."]},
],
},

{
"slug": "como-medir-resultado-campanha-influenciador",
"title": "Como mensurar resultado de campanha com influenciador",
"meta_description": "Além de curtida: quais métricas acompanhar em campanha com influenciadora, como rastrear conversão com cupom e link, e em que prazo avaliar.",
"category": GESTAO,
"date": "2026-07-08",
"excerpt": "Curtida é a métrica mais fácil de ver e a que menos diz. O que acompanhar em cada etapa, e como montar o rastreio antes de publicar.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "A conversa sobre resultado de campanha com influenciadora costuma travar no mesmo ponto: a marca olha o número de curtidas, acha pouco ou acha muito, e não consegue dizer se valeu.",
    "O problema não é falta de dado, é falta de combinação prévia. Medição se monta antes da publicação, e a métrica certa depende do objetivo que você definiu no começo."]},

  {"h2": "Primeiro, o objetivo",
   "p": [
    "Existem três objetivos possíveis, e eles não se medem do mesmo jeito. Reconhecimento quer que mais gente saiba que você existe. Consideração quer que quem já conhece passe a considerar comprar. Conversão quer venda agora.",
    "Cobrar venda imediata de uma campanha de reconhecimento é o erro mais comum, e faz campanha boa parecer fracasso. Escreva o objetivo antes, em uma frase, e escolha as métricas a partir dele."]},

  {"h2": "Métricas de alcance",
   "p": [
    "Servem para objetivo de reconhecimento. Peça sempre o print do painel da criadora, com recorte do período:"],
   "ul": [
    "Alcance: quantas pessoas diferentes viram a publicação",
    "Impressões: quantas vezes ela foi exibida, incluindo repetições",
    "Visualizações de vídeo, e quantas passaram dos primeiros segundos",
    "Distribuição por cidade, essencial quando o negócio atende uma região"]},

  {"h2": "Métricas de interesse",
   "p": [
    "Mostram que o conteúdo fez alguém parar e considerar. São as mais subestimadas:"],
   "ul": [
    "Salvamentos, sinal de que a pessoa quer voltar ao conteúdo depois",
    "Compartilhamentos, que ampliam alcance para fora da audiência da criadora",
    "Comentários com pergunta sobre preço, disponibilidade ou como comprar",
    "Cliques no link e visitas ao seu perfil vindas da publicação",
    "Novos seguidores no seu perfil no período da campanha"]},

  {"h2": "Métricas de conversão",
   "p": [
    "Aqui é onde a campanha se paga, e onde o rastreio precisa estar montado antes. Três formas simples resolvem a maioria dos casos.",
    "Cupom exclusivo por criadora é o mais fácil de implementar e de ler. Cada perfil recebe um código diferente, e o uso do código diz exatamente de onde veio a venda.",
    "Link com parâmetro de rastreio funciona quando existe site ou loja online. O mesmo endereço com uma marcação diferente por campanha permite separar a origem no seu painel de análise.",
    "Para negócio que vende por WhatsApp, um link com mensagem pré-preenchida específica da campanha resolve. Quando a mensagem chega já escrita de um jeito diferente, você sabe a origem sem perguntar."]},

  {"h2": "Monte o rastreio antes, não depois",
   "p": [
    "Esse é o ponto onde a maioria das campanhas se perde. O cupom é criado às pressas no dia da publicação, o link vai sem marcação, e depois não há como separar o que veio de onde.",
    "Uma preparação simples resolve, e leva pouco tempo:"],
   "ul": [
    "Criar um cupom por criadora, com nome fácil de digitar e de lembrar",
    "Gerar um link marcado por campanha e testar se ele abre corretamente no celular",
    "Avisar a equipe de atendimento que a campanha vai ao ar e o que perguntar a quem chegar",
    "Registrar o desempenho do período anterior, para ter base de comparação",
    "Combinar com a criadora que ela envia os prints do painel em uma data definida"]},

  {"h2": "O que não vale como métrica",
   "p": [
    "Alguns números aparecem em relatório e não sustentam decisão. Número de seguidores da criadora não é resultado, é característica de quem você contratou. Curtida isolada diz pouco, porque é o gesto mais barato que existe na rede.",
    "Também não vale comparar campanhas com objetivos diferentes, nem comparar seu desempenho com o de uma marca de outro porte e outra frequência de investimento.",
    "E cuidado com o valor equivalente de mídia, aquele cálculo que estima quanto custaria comprar o mesmo alcance em anúncio. É um número que impressiona em apresentação e não corresponde a dinheiro que entrou."]},

  {"h2": "Perguntar continua funcionando",
   "p": [
    "Nem tudo se rastreia. Alguém vê a publicação, não clica, e procura você três semanas depois pelo nome. Isso é resultado real e não aparece em link nenhum.",
    "Por isso vale manter a pergunta no atendimento sobre como a pessoa conheceu a empresa, e anotar. Cruzar essa anotação com o período das campanhas costuma revelar efeito que o rastreio sozinho perde."]},

  {"h2": "O prazo certo de avaliar",
   "p": [
    "Avaliar no dia seguinte induz ao erro. Publicação continua sendo vista por dias, e a decisão de compra raramente é imediata, principalmente em serviço de valor mais alto.",
    "Combine uma janela de avaliação com a criadora, por exemplo trinta dias, e compare com o período anterior equivalente. Uma única publicação também raramente muda o jogo: presença repetida ao longo de meses é o que constrói associação, e é aí que o retorno aparece com mais clareza."]},
],
},

{
"slug": "guia-reels-para-empresas",
"title": "Guia rápido de Reels para empresas que ainda não postam vídeo",
"meta_description": "Como começar a publicar vídeo curto sem equipamento caro e sem medo de câmera: formatos simples, os primeiros segundos e o ritmo inicial.",
"category": SOCIAL,
"date": "2026-06-30",
"excerpt": "O obstáculo quase nunca é técnico. São formatos simples de gravar e um jeito de começar sem precisar aparecer falando para a câmera.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "Vídeo curto deixou de ser formato opcional e virou a principal forma de alcançar quem ainda não segue seu perfil. Mesmo assim, muita empresa segue publicando só foto.",
    "Na maioria das vezes o obstáculo não é equipamento nem edição. É não saber o que gravar e não querer aparecer. Os dois têm solução prática."]},

  {"h2": "Você não precisa aparecer falando",
   "p": [
    "A ideia de que vídeo exige alguém carismático olhando para a câmera trava muita gente. Boa parte dos formatos que funcionam não tem rosto nenhum.",
    "Mão trabalhando, processo sendo feito, antes e depois, produto sendo preparado, detalhe do material. Tudo isso é vídeo, e para negócio de serviço costuma render mais do que alguém falando, porque mostra a competência em vez de afirmá-la."]},

  {"h2": "Cinco formatos fáceis de começar",
   "p": ["Se você não sabe por onde começar, use estes. Todos podem ser gravados com celular, sem roteiro elaborado:"],
   "ul": [
    "O processo: o serviço sendo executado, acelerado, do início ao resultado",
    "Antes e depois: o estado inicial, um corte, o estado final",
    "Resposta a uma dúvida: a pergunta que mais chega no direct, respondida em trinta segundos",
    "Bastidor: preparação do dia, chegada do material, organização do espaço",
    "Erro comum: o que as pessoas fazem errado sobre o seu assunto e o que fazer no lugar"]},

  {"h2": "Os primeiros segundos decidem tudo",
   "p": [
    "É o único ponto técnico que vale obsessão. Se o começo não prende, o resto do vídeo não é visto, por melhor que seja.",
    "Evite abertura com apresentação e boas-vindas. Comece pelo movimento, pelo resultado ou pela frase que interessa. Se o vídeo mostra um antes e depois, mostre o depois primeiro e depois volte para o começo.",
    "Uma linha de texto na tela nos primeiros instantes ajuda, porque muita gente assiste sem som. Ela deve dizer do que se trata, não dar bom dia."]},

  {"h2": "Equipamento: o celular basta",
   "p": [
    "Não compre nada antes de publicar por três meses. O que muda a qualidade percebida, em ordem de importância:"],
   "ul": [
    "Luz: grave de frente para uma janela, nunca de costas para ela",
    "Estabilidade: apoie o celular em algo fixo em vez de segurar",
    "Som: se alguém fala, grave em ambiente silencioso e perto do microfone",
    "Legenda: adicione sempre, porque a maioria assiste sem áudio",
    "Enquadramento vertical, com espaço livre no topo e na base para não cobrir o texto"]},

  {"h2": "O que trava e como destravar",
   "p": [
    "O maior travamento é querer que o primeiro vídeo seja bom. Ele não vai ser, e não precisa ser. Os primeiros existem para você se acostumar com a câmera e descobrir o que seu público responde.",
    "Grave vários de uma vez, no mesmo dia, com a mesma roupa e a mesma luz. Publicar o que já está gravado é muito mais fácil do que decidir gravar toda semana.",
    "E resista à edição elaborada no começo. Corte, legenda e um áudio adequado resolvem. Produção excessiva costuma render menos que registro honesto do trabalho real."]},

  {"h2": "De onde tirar assunto sem esforço",
   "p": [
    "A pergunta que mais aparece depois de resolver o medo da câmera é o que gravar toda semana. A resposta quase sempre já está na sua operação, e não precisa ser inventada.",
    "As dúvidas que chegam no direct e no atendimento são a melhor fonte. Cada pergunta repetida é um vídeo, e o fato de ela se repetir prova que existe público para o assunto.",
    "Outras fontes que rendem: o motivo pelo qual alguém desistiu de comprar, o erro que você mais corrige em clientes, a comparação entre duas opções que as pessoas confundem, e o que muda de uma estação para outra no seu negócio."]},

  {"h2": "Reaproveite o que você já gravou",
   "p": [
    "Um único dia de gravação rende mais material do que parece. O vídeo publicado no feed vira corte para stories, o áudio vira citação em imagem, e o assunto vira legenda de um post futuro.",
    "Vídeo que teve bom desempenho pode ser republicado meses depois, com abertura diferente. A maior parte de quem segue não viu a primeira vez, e quem viu já esqueceu.",
    "Isso reduz muito a pressão de produzir do zero toda semana, que é o que faz a maioria das empresas desistir do formato no segundo mês."]},

  {"h2": "Ritmo para os primeiros meses",
   "p": [
    "Um vídeo por semana durante dois meses é suficiente para sair do zero e entender o que funciona no seu caso. Depois disso, aumente se der conta.",
    "Olhe retenção antes de olhar visualização: quantas pessoas passaram dos primeiros segundos e quantas chegaram ao fim. É esse número que diz se o começo está prendendo, e é ele que você deve tentar melhorar a cada nova gravação."]},
],
},

{
"slug": "quanto-cobrar-publicidade-influenciador",
"title": "Como precificar um contrato de publicidade com influenciador",
"meta_description": "Guia de precificação para quem cria conteúdo: o que compõe o valor de uma publi, como montar sua faixa de preço e como apresentar a proposta para a marca.",
"category": GESTAO,
"date": "2026-06-23",
"excerpt": "Não existe tabela oficial, e é justamente por isso que quem começa costuma cobrar errado. Os critérios que compõem o valor de uma publicação.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "Toda criadora passa por esse momento: a primeira marca chega, pergunta o valor, e vem o branco. Cobrar pouco desvaloriza o trabalho e cria referência ruim para as próximas. Cobrar muito sem justificativa afasta a negociação.",
    "Não existe tabela oficial, e desconfie de quem apresenta uma. O que existe são critérios objetivos que compõem o preço, e saber nomeá-los muda completamente a conversa comercial."]},

  {"h2": "O preço não é pelo post, é pelo pacote",
   "p": [
    "O erro que quase todo mundo comete no começo é precificar uma peça isolada. A marca não está comprando um vídeo, está comprando acesso à sua audiência, o seu tempo de produção e o uso da sua imagem.",
    "Quando você separa esses componentes, fica muito mais fácil justificar o valor e negociar sem simplesmente dar desconto. Cada item abaixo move o preço para cima ou para baixo, e todos devem estar escritos na proposta."]},

  {"h2": "Os componentes do valor",
   "p": ["Estes são os critérios que efetivamente compõem o preço de uma publicidade:"],
   "ul": [
    "Alcance real das últimas publicações, que é mais confiável do que o número de seguidores",
    "Quantidade e formato das entregas: vídeo no feed, sequência de stories, foto, participação em evento",
    "Complexidade de produção: roteiro, deslocamento, figurino, edição mais elaborada, gravação externa",
    "Exclusividade de categoria, ou seja, o compromisso de não divulgar concorrente por um período",
    "Direito de uso da peça pela marca, principalmente se ela quiser impulsionar ou usar em anúncio",
    "Tempo de permanência da publicação no ar",
    "Prazo de entrega, com urgência custando mais"]},

  {"h2": "Exclusividade e direito de uso mudam muito o valor",
   "p": [
    "São os dois itens que quem começa mais esquece de cobrar, e os que mais impactam a conta.",
    "Exclusividade tem custo porque limita seu faturamento. Se você aceita não falar de nenhuma outra marca da mesma categoria por três meses, está abrindo mão de outros contratos naquele período. Isso precisa estar no preço, e o prazo e a categoria precisam estar escritos com precisão.",
    "Direito de uso é a permissão para a marca usar seu conteúdo e sua imagem em outros lugares, como anúncio pago, site ou material de loja. É um uso diferente do combinado originalmente e deve ser cobrado à parte, com prazo e canais definidos."]},

  {"h2": "Como montar sua faixa de preço",
   "p": [
    "Comece pelo seu custo real. Some as horas de roteiro, gravação, edição, aprovação e resposta a comentário. Defina quanto vale a sua hora e chegue a um piso. Nenhum contrato deve ficar abaixo dele.",
    "A partir daí, componha por entrega. Um valor base para vídeo no feed, outro para sequência de stories, e acréscimos percentuais para exclusividade, direito de uso e urgência.",
    "Tenha também um valor de pacote mensal, com desconto em relação à soma das peças avulsas. Presença recorrente rende mais para a marca e dá previsibilidade para você, então é uma troca boa para os dois lados."]},

  {"h2": "Permuta: quando aceitar",
   "p": [
    "Permuta é pagamento em produto ou serviço, e não é automaticamente ruim. Ela faz sentido quando o produto tem valor real para você, quando você usaria de qualquer forma, e quando o valor equivale ao que você cobraria.",
    "Ela deixa de fazer sentido quando o valor do produto é muito menor que o do seu trabalho, quando a marca pede entregas de contrato pago em troca de brinde, ou quando você já tem histórico e audiência que sustentam cobrança em dinheiro.",
    "Uma regra simples: se a permuta não cobre o seu piso de custo, ela está te fazendo trabalhar de graça."]},

  {"h2": "Como apresentar a proposta",
   "p": [
    "Mande sempre por escrito, com as entregas listadas, o prazo, o que está incluído e o que não está, quantas rodadas de ajuste estão previstas e a forma de pagamento.",
    "Proposta escrita reduz mal-entendido e transmite profissionalismo, que por si só sustenta valor. Junte o mídia kit atualizado com os números do período recente.",
    "Se a marca pedir desconto, prefira reduzir entregas a reduzir preço. Manter o valor por peça protege a sua referência para as próximas negociações, inclusive com outras marcas que conversam entre si."]},

  {"h2": "Combine o pagamento por escrito",
   "p": [
    "Prazo e forma de pagamento precisam estar na proposta com a mesma clareza das entregas. Quando isso fica implícito, a cobrança vira desgaste e a relação com a marca azeda.",
    "Para contratos maiores ou com produção que exige deslocamento e custo, é comum trabalhar com parte na aprovação do roteiro e parte após a publicação. Isso protege os dois lados e é prática aceita no mercado."]},

  {"p": [
    "Boa parte do trabalho de assessoria é exatamente esse: estruturar proposta, negociar exclusividade e direito de uso, e manter o mídia kit atualizado, para que a criadora possa continuar focada em criar."]},
],
},

{
"slug": "branding-para-negocio-local",
"title": "Branding local: como pequenas marcas competem com grandes redes",
"meta_description": "As vantagens reais de um negócio local diante de uma grande rede, e como transformar proximidade e identidade de cidade em posicionamento de marca.",
"category": BRANDING,
"date": "2026-06-16",
"excerpt": "Competir com rede grande no terreno dela é perder. Existem vantagens que só o negócio local tem, e quase nenhuma delas aparece na comunicação.",
"cta": CTA_BRANDING,
"body": [
  {"p": [
    "Quando uma rede grande abre perto, a reação instintiva do negócio local é tentar responder no mesmo terreno: baixar preço, imitar a comunicação, copiar a promoção. É a disputa mais difícil de vencer, porque a estrutura do outro lado é maior.",
    "A saída não é competir melhor no jogo deles. É jogar um jogo onde a rede grande não consegue entrar, e isso é uma decisão de marca antes de ser uma decisão de marketing."]},

  {"h2": "A disputa que você não deve aceitar",
   "p": [
    "Rede grande ganha em escala: compra mais barato, dilui custo fixo e aguenta operar com margem menor por mais tempo. Disputa de preço puro contra esse tipo de estrutura raramente termina bem para o negócio local.",
    "Ela também ganha em previsibilidade e em reconhecimento nacional. O cliente já sabe o que esperar antes de entrar, o que reduz o risco percebido da compra.",
    "Aceitar essa disputa é escolher o campo onde suas desvantagens pesam mais. O trabalho de marca é mudar o critério pelo qual você está sendo comparado."]},

  {"h2": "O que só o negócio local tem",
   "p": ["Estas vantagens são estruturais, e a rede grande não consegue replicar de verdade:"],
   "ul": [
    "Conhecer o cliente pelo nome e lembrar do que ele comprou da última vez",
    "Resolver exceção sem pedir autorização para uma matriz em outro estado",
    "Mudar de oferta, produto ou horário na mesma semana, conforme o movimento do bairro",
    "Ter rosto e história conhecidos, com donos que aparecem e respondem",
    "Fazer parte da vida da cidade: patrocinar o time, apoiar a escola, estar no evento do bairro",
    "Indicar concorrente ou parceiro quando não é o melhor para o cliente, o que gera confiança rara"]},

  {"h2": "Proximidade precisa aparecer, não só existir",
   "p": [
    "O erro mais comum é ter todas essas vantagens e comunicar exatamente como uma rede: foto de banco de imagem, texto genérico, promoção impessoal.",
    "Se o dono atende, ele deveria aparecer. Se a equipe é a mesma há anos, isso é argumento. Se o produto é feito ali, o processo é conteúdo. Nada disso a rede grande consegue mostrar com verdade.",
    "Comunicação de negócio local que imita comunicação de rede joga fora a única vantagem que não pode ser comprada."]},

  {"h2": "Identidade de cidade como posicionamento",
   "p": [
    "Pertencer a um lugar é posicionamento legítimo e difícil de copiar. Isso não significa colocar o nome da cidade no logotipo, significa que a marca conversa com códigos que quem mora ali reconhece.",
    "Referências ao clima, à rotina do lugar, aos pontos que todo mundo conhece, ao vocabulário da região. Esses detalhes criam identificação imediata em quem é dali, e é justamente esse público que sustenta o negócio.",
    "Vale também considerar o inverso: quem vem de fora costuma procurar o que é típico do lugar. Marca que assume a origem atende os dois."]},

  {"h2": "Como traduzir isso em decisões de marca",
   "p": [
    "Três perguntas ajudam a transformar essas vantagens em posicionamento concreto.",
    "Primeira: o que a rede grande nunca vai conseguir dizer sobre si mesma? Segunda: qual problema o cliente da região tem e a solução padronizada não resolve? Terceira: o que as pessoas já falam de você quando indicam para um amigo?",
    "As respostas costumam ser o material bruto do posicionamento. A partir delas, a identidade visual, o tom de voz e a comunicação passam a ter critério, em vez de imitar o que a concorrência faz."]},

  {"h2": "Consistência é o que sustenta a vantagem",
   "p": [
    "Proximidade só vira marca quando é previsível. Se o atendimento é excelente com o dono presente e irregular quando ele não está, a vantagem não se sustenta e o cliente volta para a opção padronizada.",
    "É aqui que rede grande costuma ganhar sem esforço: ela entrega sempre a mesma coisa. O negócio local que combina proximidade com consistência fica em uma posição que nenhuma das duas pontas alcança sozinha.",
    "Na prática, isso significa combinar com a equipe o que nunca pode faltar no atendimento, independentemente de quem estiver na loja naquele dia."]},

  {"h2": "Onde não vale competir",
   "p": [
    "Nem toda disputa merece resposta. Variedade infinita de produto, preço mais baixo do mercado e presença em todas as cidades não são batalhas do negócio local.",
    "Assumir isso é libertador, porque concentra energia onde ela rende. Um negócio local com marca clara não precisa ser a opção mais barata, precisa ser a escolha óbvia para quem valoriza o que ele faz melhor.",
    "Atendemos clientes de vários segmentos em Joinville e São Paulo, e o padrão se repete: os que crescem são os que pararam de tentar parecer maiores do que são e passaram a mostrar o que os torna diferentes."]},
],
},

{
"slug": "midia-kit-influenciadora",
"title": "O papel do mídia kit na carreira de uma influenciadora",
"meta_description": "O que um mídia kit precisa ter, por que ele encurta negociação com marcas e com que frequência atualizar os números para não perder contrato.",
"category": GESTAO,
"date": "2026-06-09",
"excerpt": "É o documento que responde, antes da conversa, quem é o seu público e o que você entrega. Sem ele, cada negociação começa do zero.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "Mídia kit é o material que apresenta uma criadora para uma marca: quem ela é, quem a acompanha, o que ela já fez e o que ela entrega. Na prática, é o documento que decide se a conversa avança ou morre no primeiro contato.",
    "Muita criadora com bom conteúdo perde contrato por não ter esse material pronto. A marca precisa apresentar a proposta internamente, e sem números organizados ela vai apresentar outra pessoa.",
    "Vale dizer também o que ele não é. Mídia kit não é portfólio de fotos bonitas nem currículo com histórico completo. É um documento comercial, feito para quem vai decidir se investe, e por isso precisa ser objetivo e fácil de ler em poucos minutos."]},

  {"h2": "Por que ele encurta a negociação",
   "p": [
    "Do lado da marca, contratar criadora é uma decisão que quase sempre precisa ser justificada para alguém: um gestor, um cliente, um financeiro. Quem decide raramente é quem faz o primeiro contato.",
    "O mídia kit é o que essa pessoa consegue encaminhar. Se ele responde de antemão quem é o público, qual o alcance e quanto custa, o processo anda sem dez trocas de mensagem.",
    "Ele também posiciona. Uma criadora com material organizado passa a impressão de quem trata a atividade como negócio, e isso muda o valor que a marca aceita pagar."]},

  {"h2": "O que precisa ter",
   "p": ["Um mídia kit completo cabe em poucas páginas e cobre estes pontos:"],
   "ul": [
    "Apresentação curta: quem é você, seu nicho e o que a sua audiência espera de você",
    "Dados do público: faixa etária, distribuição por gênero e principalmente por cidade",
    "Números de desempenho recentes: alcance médio, visualizações, engajamento, com o período indicado",
    "Formatos que você entrega, com descrição do que está incluso em cada um",
    "Marcas com quem já trabalhou e exemplos de campanhas anteriores",
    "Depoimento de marca, quando houver, que funciona como prova social",
    "Contato comercial direto, ou o contato de quem faz a sua assessoria"]},

  {"h2": "Números honestos rendem mais",
   "p": [
    "A tentação de escolher o melhor mês de todos e apresentar como se fosse a média é grande, e é um tiro no pé. A marca vai comparar a promessa com o resultado, e a diferença destrói a chance de recontratação.",
    "Apresente média de um período recente e identificado, por exemplo os últimos noventa dias. Se houve um pico fora da curva, mostre separado e explique o motivo.",
    "Números modestos e verdadeiros com público bem definido vendem melhor do que números inflados. Marca experiente reconhece consistência, e consistência é o que ela está comprando."]},

  {"h2": "Mostre o trabalho, não só os dados",
   "p": [
    "Métrica sozinha não diz como você comunica. A parte visual do mídia kit precisa mostrar o seu conteúdo: capturas de publicações que funcionaram, prints de comentário real, fotos que representam seu estilo.",
    "Se você já fez campanha, conte o caso brevemente: qual era o objetivo, o que você entregou e o que aconteceu. Um exemplo concreto vale mais do que uma lista de logotipos de marcas.",
    "O material também precisa parecer com você. Um mídia kit genérico, feito em modelo pronto sem adaptação, contradiz a ideia de que você é uma criadora com identidade própria."]},

  {"h2": "Erros que derrubam a proposta",
   "p": ["Alguns problemas aparecem com frequência e custam contrato:"],
   "ul": [
    "Arquivo pesado demais, que não abre no celular de quem vai avaliar",
    "Números sem período indicado, que não permitem comparação e geram desconfiança",
    "Preço ausente, o que obriga uma troca de mensagens a mais e atrasa a decisão",
    "Excesso de páginas, quando o essencial cabe em poucas",
    "Print de métrica cortado ou ilegível, que passa impressão de improviso",
    "Contato desatualizado, o erro mais simples e mais frequente de todos"]},

  {"h2": "Por que atualizar por temporada",
   "p": [
    "Audiência muda. O alcance de seis meses atrás não descreve o perfil de hoje, e as plataformas alteram distribuição com frequência.",
    "Mídia kit desatualizado tem dois riscos. Se os números caíram, você promete o que não entrega. Se subiram, você está cobrando abaixo do que poderia, o que é mais comum do que parece.",
    "Uma atualização a cada temporada, com os dados do trimestre e as campanhas recentes, mantém o material vivo. É por isso que produzimos mídia kit atualizado por temporada para as criadoras que assessoramos, junto com o acompanhamento das métricas que sustentam cada negociação."]},
],
},

{
"slug": "quando-vale-a-pena-consultoria-marketing-digital",
"title": "Consultoria de marketing digital: quando vale a pena contratar",
"meta_description": "Os sinais de que uma empresa precisa de direcionamento externo em marketing digital e a diferença entre consultoria pontual e acompanhamento contínuo.",
"category": CONSULTORIA,
"date": "2026-06-02",
"excerpt": "Consultoria não é execução. Ela resolve o problema de quem não sabe o que fazer, não o de quem não tem tempo de fazer.",
"cta": CTA_CONSULTORIA,
"body": [
  {"p": [
    "Existe uma confusão frequente entre contratar consultoria e contratar execução. As duas resolvem problemas diferentes, e contratar a errada é dinheiro gasto sem retorno.",
    "Consultoria entrega direcionamento: diagnóstico, prioridades e um plano de o que fazer, em que ordem e por quê. Execução entrega o trabalho pronto. Quem não sabe o caminho precisa da primeira. Quem sabe mas não tem tempo precisa da segunda."]},

  {"h2": "Sinais de que falta direcionamento",
   "p": ["Alguns sintomas indicam com clareza que o problema é de estratégia, não de mão de obra:"],
   "ul": [
    "Você publica com constância, tem alcance razoável e mesmo assim não chega cliente novo",
    "Investe em anúncio sem saber dizer quanto cada cliente custou para ser adquirido",
    "Recebe propostas de fornecedores e não tem critério para avaliar qual faz sentido",
    "Já trocou de agência mais de uma vez e o problema continuou o mesmo",
    "A equipe interna produz bastante, mas cada pessoa segue uma direção diferente",
    "Você toma decisão de marketing por indicação de conhecido ou por imitar concorrente"]},

  {"h2": "O que uma consultoria faz na prática",
   "p": [
    "Começa por diagnóstico: olhar o que já existe, os números disponíveis, o posicionamento, os canais e a operação por trás. Muita coisa se resolve nessa etapa, porque problemas de marketing frequentemente são problemas de oferta ou de atendimento.",
    "Depois vem a priorização, que costuma ser a parte mais valiosa. Não é uma lista de tudo o que poderia ser feito, é a ordem do que deve ser feito primeiro, considerando o que você tem de tempo, verba e equipe.",
    "E por fim o plano, com responsáveis, prazos e forma de medir. Consultoria que termina em apresentação bonita sem plano executável não muda nada na segunda-feira."]},

  {"h2": "Pontual ou contínua",
   "p": [
    "Os dois formatos existem porque atendem momentos diferentes.",
    "A consultoria pontual funciona quando existe uma dúvida específica e delimitada: se vale investir em determinado canal, por que uma campanha não performou, como estruturar um lançamento. É um encontro objetivo, com foco em destravar aquela questão.",
    "A consultoria contínua faz sentido quando a empresa precisa de acompanhamento ao longo do tempo, com ajuste de rota conforme o resultado aparece. É o formato para quem tem operação rodando e quer otimização constante, não uma resposta única.",
    "Trabalhamos com esses dois formatos: um encontro de trinta minutos, direto ao ponto, para a dúvida urgente, e um acompanhamento estratégico permanente para quem busca crescimento sustentável."]},

  {"h2": "O que a consultoria não resolve",
   "p": [
    "Vale dizer com clareza, para evitar frustração. Consultoria não substitui execução: alguém ainda precisa produzir, publicar e atender.",
    "Ela também não compensa produto ruim, atendimento lento ou preço fora da realidade do mercado. Marketing bem feito acelera o que já funciona e expõe mais rápido o que não funciona.",
    "E não entrega resultado imediato. Direcionamento muda decisão, decisão muda execução, e execução leva tempo para virar número.",
    "Vale ajustar a expectativa desde o começo: o retorno de uma consultoria aparece primeiro como clareza e economia, quando você para de gastar com o que não faria diferença, e só depois como crescimento."]},

  {"h2": "Consultoria ou agência: como decidir",
   "p": [
    "A dúvida entre contratar consultoria ou contratar uma agência para executar aparece sempre, e a resposta depende de onde está o gargalo.",
    "Se você já sabe o que precisa ser feito, tem clareza de público e de oferta, e o que falta é braço para produzir e publicar, o caminho é execução. Contratar consultoria nesse caso vai confirmar o que você já sabia.",
    "Se a dúvida é sobre o que fazer, em qual canal investir ou por que o esforço atual não converte, comece pelo direcionamento. Contratar execução antes disso costuma significar produzir bastante material na direção errada, com custo mensal.",
    "Há também o caso em que os dois andam juntos: uma etapa inicial de diagnóstico e plano, seguida pela execução do que foi definido."]},

  {"h2": "Como aproveitar melhor",
   "p": [
    "Chegue com material: os números que você tem, o histórico do que já tentou, o que deu certo e o que não deu. Quanto mais contexto, mais específica é a recomendação.",
    "Leve também a pergunta real, não a pergunta educada. Se a dúvida é se vale continuar investindo em um canal que não está dando retorno, é isso que deve ser colocado na mesa.",
    "E combine antes como o resultado será avaliado. Consultoria boa termina com você sabendo exatamente o que fazer nas próximas semanas, e com um jeito de verificar se funcionou."]},
],
},

{
"slug": "como-organizar-feed-instagram-empresa",
"title": "Como estruturar o feed do Instagram da sua empresa",
"meta_description": "Como organizar o feed do Instagram de uma empresa: coerência de cor, alternância de formatos, capas de vídeo e o que realmente importa na primeira visita.",
"category": SOCIAL,
"date": "2026-05-26",
"excerpt": "O feed é a primeira impressão de quem chega pela primeira vez. Organizar ele é menos sobre estética e mais sobre deixar claro o que você faz.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "O feed cumpre uma função específica e frequentemente mal compreendida. Ele não existe para ser admirado como mosaico, existe para convencer quem chegou pela primeira vez.",
    "Alguém viu um conteúdo seu, uma indicação ou um anúncio, e entrou no perfil. Nos primeiros segundos, essa pessoa está respondendo três perguntas: o que essa empresa faz, ela parece confiável, e ela atende o que eu preciso.",
    "Todo o resto do trabalho de organização visual serve para responder essas três perguntas mais rápido. Quando a decisão de design não ajuda nisso, ela é decoração."]},

  {"h2": "Coerência importa mais que perfeição",
   "p": [
    "Feed organizado não significa grade milimétrica com todas as fotos do mesmo tom. Significa que os posts parecem da mesma empresa.",
    "Três decisões resolvem a maior parte disso: uma paleta reduzida de cores que se repete, uma fonte para título e uma para texto de apoio, e um tratamento padrão de foto, com o mesmo tipo de luz e enquadramento.",
    "Repetição é o que constrói reconhecimento. Quando alguém identifica seu post no meio da rolagem sem ler o nome do perfil, a coerência está funcionando."]},

  {"h2": "Alterne os tipos de publicação",
   "p": [
    "Feed inteiro de arte com texto cansa e não mostra a empresa. Feed inteiro de foto de produto não ensina nada. A alternância é o que mantém o conjunto interessante e informativo.",
    "Uma distribuição que funciona bem para negócio de serviço: conteúdo que ensina algo, prova social como depoimento ou resultado, bastidor mostrando o trabalho real, e oferta direta em menor proporção.",
    "Ao publicar, olhe as duas últimas fileiras. Se três posts seguidos são do mesmo tipo, vale intercalar antes de publicar o próximo."]},

  {"h2": "Capas de vídeo fazem parte do feed",
   "p": [
    "Com vídeo curto ocupando espaço cada vez maior, a capa de cada vídeo virou elemento visual do feed tanto quanto uma foto.",
    "Capa automática, tirada de um quadro qualquer, costuma ser o que mais desorganiza um perfil. Definir uma capa por vídeo, com o mesmo padrão de fonte e posição de texto, resolve de uma vez.",
    "Vale lembrar que o texto da capa aparece cortado na grade do perfil em alguns formatos. Deixe a informação principal centralizada e longe das bordas."]},

  {"h2": "Legibilidade antes de estética",
   "p": ["Alguns cuidados simples evitam o post bonito que ninguém consegue ler:"],
   "ul": [
    "Texto grande o suficiente para ser lido na miniatura, antes de a pessoa abrir",
    "Contraste real entre a cor do texto e o fundo, principalmente sobre foto",
    "Uma ideia por post, não três mensagens disputando espaço",
    "Margem interna generosa, para o conteúdo não encostar nas bordas",
    "Elementos importantes fora das áreas que a interface cobre"]},

  {"h2": "Os primeiros nove posts",
   "p": [
    "É o que a pessoa vê sem rolar, e é o que precisa responder as três perguntas iniciais. Vale olhar esse bloco como se fosse uma vitrine.",
    "Se entre os nove primeiros não houver nada que explique o serviço, nada que mostre resultado e nada que dê um caminho de contato, o feed está bonito e mudo.",
    "Uma tática simples é fixar no topo três publicações escolhidas: uma que apresenta a empresa, uma que mostra prova social e uma que apresenta a oferta principal. Isso garante a mensagem certa mesmo quando o conteúdo recente for mais casual."]},

  {"h2": "O feed não trabalha sozinho",
   "p": [
    "Vale lembrar que quem chega ao perfil também olha a bio, os destaques e as avaliações antes de decidir. O feed convence pela impressão geral, mas é o conjunto que fecha.",
    "Destaques bem organizados fazem metade desse trabalho. Separados por dúvida real, como preço, como funciona, resultados e perguntas frequentes, eles respondem antes que a pessoa precise perguntar.",
    "Se o feed está impecável e os destaques estão vazios ou desatualizados, o esforço visual está sendo desperdiçado no último passo da decisão."]},

  {"h2": "Como manter sem travar a produção",
   "p": [
    "Perfeccionismo com feed é um dos motivos mais comuns de queda na frequência. Se cada post precisa encaixar em um mosaico planejado, publicar vira operação complexa e a constância morre.",
    "Defina o padrão uma vez, salve modelos reutilizáveis para os formatos que se repetem, e siga publicando. Coerência sustentada por meses vale mais do que uma grade perfeita por três semanas.",
    "E revise o conjunto uma vez por mês, não a cada publicação. É frequência suficiente para corrigir a rota sem transformar cada post em decisão de design."]},
],
},

{
"slug": "tendencias-marketing-digital-que-vieram-para-ficar",
"title": "Tendências de marketing digital que vieram para ficar",
"meta_description": "Mudanças estruturais no marketing digital que não são modismo: vídeo curto, busca dentro das redes, conteúdo útil e conversa como canal de venda.",
"category": SOCIAL,
"date": "2026-05-19",
"excerpt": "Ignore a lista de tendências do ano. Existem mudanças de comportamento que já se consolidaram e que devem orientar decisão de investimento.",
"cta": CTA_SOCIAL,
"body": [
  {"p": [
    "Toda virada de ano traz uma lista de tendências que envelhece em poucos meses. Formato da moda, recurso novo de plataforma, termo que aparece em toda apresentação e some depois.",
    "Mais útil do que perseguir novidade é reconhecer as mudanças de comportamento que já se consolidaram. Elas mudam devagar, valem para negócios de portes diferentes e sustentam decisão de investimento por anos."]},

  {"h2": "Vídeo curto virou a porta de entrada",
   "p": [
    "Não é questão de preferência estética, é questão de distribuição. As plataformas mostram vídeo curto para quem ainda não segue o perfil, o que faz dele o principal caminho para alcançar público novo.",
    "Foto e texto continuam funcionando, mas cumprem outro papel: conversam com quem já conhece a marca. Quem publica só nesses formatos está falando basicamente com quem já chegou.",
    "A consequência prática é que produzir vídeo deixou de ser diferencial e virou requisito básico, mesmo para negócio pequeno e sem estrutura de produção."]},

  {"h2": "Autenticidade rende mais que produção",
   "p": [
    "Essa é a mudança que mais incomoda quem investiu em produção elaborada. Conteúdo gravado no celular, com a pessoa real do negócio falando, costuma performar melhor do que material com acabamento de comercial.",
    "O motivo é simples: o público aprendeu a reconhecer publicidade em um segundo, e desviar dela virou reflexo. Conteúdo que parece anúncio é tratado como anúncio.",
    "Isso não significa abandonar qualidade. Significa que a qualidade que importa mudou de lugar: som limpo, luz decente e clareza valem mais do que efeito e trilha."]},

  {"h2": "As redes viraram buscador",
   "p": [
    "Muita gente pesquisa onde comer, qual serviço contratar e como resolver um problema direto na rede social, sem passar por buscador tradicional.",
    "Isso muda o que se escreve. Legenda, texto na tela e nome de perfil passam a funcionar como termos de busca, e conteúdo que responde uma pergunta específica continua sendo encontrado meses depois de publicado.",
    "Para negócio local, a consequência é direta: usar o nome do serviço junto com o nome da cidade nos textos deixou de ser detalhe e virou parte da estratégia."]},

  {"h2": "Conteúdo útil ganhou da autopromoção",
   "p": [
    "Perfil que só anuncia perde alcance e atenção. O conteúdo que constrói audiência é o que resolve alguma coisa para quem assiste, mesmo que a pessoa não compre naquele momento.",
    "Existe uma lógica comercial nisso, não só generosidade. Quem tirou uma dúvida com você chega para comprar já confiando, e a conversa de venda fica muito mais curta.",
    "É também o conteúdo com vida mais longa. Post que responde uma pergunta frequente continua trazendo gente nova por muito tempo, enquanto promoção morre no dia seguinte."]},

  {"h2": "A conversa virou o canal de venda",
   "p": [
    "A decisão de compra migrou para a mensagem direta. As pessoas perguntam preço, disponibilidade e detalhe por direct ou WhatsApp antes de fechar, principalmente em serviço.",
    "Isso desloca o gargalo. Não adianta alcance grande com caixa de mensagem abandonada, porque é exatamente ali que a intenção de compra aparece e esfria.",
    "Vale tratar o atendimento por mensagem como parte do marketing, com tempo de resposta combinado e respostas prontas para as perguntas que se repetem."]},

  {"h2": "Perfis menores ganharam espaço",
   "p": [
    "A lógica de contratar apenas grandes números perdeu força. Criadores com público menor e bem definido entregam relação mais próxima e costumam converter melhor por real investido.",
    "Para marcas regionais isso é especialmente relevante, porque um perfil com audiência concentrada na mesma cidade vale muito mais do que alcance nacional disperso.",
    "É por isso que trabalhamos com um grupo enxuto de criadoras, com nichos distintos, em vez de perseguir volume de nomes."]},

  {"h2": "O que continua igual",
   "p": [
    "Vale registrar o que não mudou, porque é o que dá estabilidade a qualquer plano. Oferta clara, atendimento que responde, preço coerente com o que é entregue e produto que cumpre o prometido continuam decidindo o resultado.",
    "Marketing digital acelera o que já funciona e apenas expõe mais rápido o que não funciona. Nenhuma tendência de formato compensa uma dessas bases quebrada.",
    "Por isso, antes de investir em formato novo, vale checar se o básico está de pé. É a checagem que ninguém quer fazer e a que mais evita gasto inútil."]},

  {"h2": "O que fazer com isso",
   "p": [
    "Nenhuma dessas mudanças exige orçamento grande. Todas exigem consistência, que é o recurso mais escasso.",
    "Se você precisa escolher por onde começar, comece pelo vídeo curto respondendo dúvidas reais dos seus clientes, e pelo tempo de resposta nas mensagens. São os dois pontos que mais mexem no resultado e menos dependem de investimento."]},
],
},

{
"slug": "storytelling-de-marca",
"title": "Storytelling de marca: como contar a história da sua empresa nas redes",
"meta_description": "Como transformar a história real de fundação e propósito da sua empresa em conteúdo para redes sociais, sem soar forçado ou publicitário.",
"category": BRANDING,
"date": "2026-05-12",
"excerpt": "Sua empresa já tem história. O trabalho não é inventar uma narrativa, é reconhecer o que já aconteceu e contar do jeito certo.",
"cta": CTA_BRANDING,
"body": [
  {"p": [
    "Storytelling virou palavra gasta, usada para justificar qualquer texto emotivo em legenda de post. Vale recuperar o sentido prático dela, porque a técnica funciona quando aplicada com honestidade.",
    "Contar a história de uma marca não é escrever a biografia da empresa nem produzir um vídeo institucional emocionante. É usar narrativa para explicar por que a empresa faz o que faz, de um jeito que fique na memória."]},

  {"h2": "Por que história funciona melhor que argumento",
   "p": [
    "Argumento convence quem já está disposto a ouvir. História prende quem estava passando, e por isso funciona bem em rede social, onde ninguém está procurando ser convencido.",
    "Há também a memória. Lista de diferenciais some, situação concreta fica. É mais fácil lembrar do dia em que a empresa refez um pedido inteiro por causa de um detalhe do que da frase que promete compromisso com qualidade.",
    "E existe a diferenciação. Seus concorrentes podem prometer as mesmas coisas que você, mas nenhum deles passou pelo que a sua empresa passou."]},

  {"h2": "Os elementos que toda história precisa",
   "p": ["Não é preciso técnica literária. Quatro elementos bastam para uma história funcionar:"],
   "ul": [
    "Alguém: uma pessoa concreta, com nome ou pelo menos com situação reconhecível",
    "Um problema: o que estava difícil, incômodo ou em risco",
    "Uma decisão: o que foi feito, principalmente quando custou algo",
    "O que mudou: o resultado, sem exagero e sem promessa"]},

  {"h2": "Onde encontrar as histórias que você já tem",
   "p": [
    "A parte mais difícil raramente é contar, é perceber que existe história ali. Quem vive a operação todo dia acha o próprio trabalho banal.",
    "Costumam render: o motivo pelo qual a empresa foi aberta, a primeira venda, o erro que mudou o processo, o cliente que voltou anos depois, a decisão de recusar um trabalho, o que quase deu errado e como foi resolvido.",
    "Vale montar uma lista dessas situações e ir usando aos poucos. Elas não vencem, e a maioria nunca foi contada publicamente."]},

  {"h2": "O cliente é o herói, não a marca",
   "p": [
    "Esse é o erro mais comum e o que faz o conteúdo soar publicitário. A empresa se coloca no centro, como protagonista genial que resolveu tudo, e o público desliga.",
    "A estrutura que funciona coloca o cliente no papel principal, com o problema dele, e a marca no papel de quem ajudou a resolver. É uma inversão simples que muda completamente a recepção.",
    "Na prática: em vez de contar como sua equipe é dedicada, conte a situação de alguém que estava com um problema e o que aconteceu depois. A dedicação da equipe aparece sozinha, sem precisar ser afirmada."]},

  {"h2": "Como não soar forçado",
   "p": [
    "Três cuidados resolvem a maior parte do risco.",
    "O primeiro é não inventar. Público reconhece história fabricada, e o custo de ser pego é alto demais para o benefício. Se não houve drama, não crie drama.",
    "O segundo é manter a escala. Nem toda história precisa ser de superação. Um episódio pequeno e específico, contado com detalhe verdadeiro, funciona melhor do que uma narrativa grandiosa e vaga.",
    "O terceiro é não amarrar tudo em lição de moral. Deixe a história falar e feche com o que ela mostra na prática, sem transformar em frase motivacional."]},

  {"h2": "Repetir não é problema, é o método",
   "p": [
    "Existe um receio comum de cansar o público contando a mesma história mais de uma vez. Na prática acontece o contrário: quem acompanha uma marca vê uma fração pequena do que ela publica.",
    "Histórias que definem a marca devem ser recontadas em momentos e formatos diferentes ao longo do tempo. É assim que elas se fixam e passam a ser repetidas por outras pessoas.",
    "O que cansa não é a repetição da história, é a repetição da mesma frase pronta. Conte o mesmo episódio por outro ângulo, com outro detalhe, e ele funciona de novo."]},

  {"h2": "Formatos práticos para usar",
   "p": [
    "A mesma história rende em vários lugares. Um vídeo curto contando o episódio, uma sequência de stories em capítulos, uma legenda mais longa acompanhando foto do bastidor, uma seção do site.",
    "Histórias de origem funcionam bem em conteúdo fixo, como destaques e página institucional, porque quem chega pela primeira vez procura entender quem está por trás.",
    "Histórias de cliente funcionam melhor no fluxo, publicadas com regularidade, porque cada uma alcança pessoas em situação parecida com a daquele cliente específico."]},
],
},

{
"slug": "como-funciona-agencia-gestao-influenciadores",
"title": "Como funciona uma agência de gestão de influenciadores",
"meta_description": "O que uma agência de gestão de influenciadores realmente faz: negociação, curadoria de propostas, mídia kit, contrato e desenvolvimento de marca pessoal.",
"category": GESTAO,
"date": "2026-05-05",
"excerpt": "A agência não posta por você. Ela cuida de tudo o que não é criação, que é justamente o que consome o tempo de quem cria.",
"cta": CTA_GESTAO,
"body": [
  {"p": [
    "Existe uma ideia difusa sobre o que uma agência de gestão de influenciadores faz. Muita gente imagina que ela produz o conteúdo, ou que ela simplesmente arruma contratos em troca de uma porcentagem.",
    "Nenhuma das duas descreve bem o trabalho. A agência cuida da parte comercial e estratégica da carreira, para que a criadora possa usar o tempo dela criando, que é o que gera valor."]},

  {"h2": "O que a agência resolve",
   "p": ["Na prática, o trabalho se concentra em algumas frentes bem definidas:"],
   "ul": [
    "Prospecção e relacionamento com marcas, incluindo apresentar a criadora para oportunidades que ela não alcançaria sozinha",
    "Curadoria das propostas que chegam, filtrando o que faz sentido para a imagem e o público dela",
    "Negociação comercial: valor, entregas, prazo, exclusividade e direito de uso",
    "Produção e atualização do mídia kit por temporada, com dados recentes",
    "Organização do calendário de entregas, para não acumular campanhas na mesma semana",
    "Acompanhamento de métricas, que embasa a negociação seguinte com dado e não com intuição",
    "Desenvolvimento de marca pessoal a médio e longo prazo"]},

  {"h2": "Dizer não faz parte do serviço",
   "p": [
    "É a parte menos glamourosa e uma das mais valiosas. Nem toda proposta que chega deve ser aceita, mesmo quando o valor é bom.",
    "Marca que não conversa com o público da criadora queima credibilidade. Excesso de publicidade em sequência cansa a audiência. Categoria conflitante com um contrato existente gera problema jurídico.",
    "Ter alguém avaliando isso com distância, sem o entusiasmo do momento, protege o ativo mais importante da criadora, que é a confiança de quem a acompanha."]},

  {"h2": "A negociação que ninguém vê",
   "p": [
    "Boa parte do trabalho acontece em conversas que a audiência nunca percebe. Definir quantas rodadas de ajuste estão incluídas, o que acontece se a marca atrasar a aprovação, por quanto tempo a publicação fica no ar, se a peça pode virar anúncio pago.",
    "São detalhes que parecem burocracia e que decidem se o contrato foi bom ou ruim. Criadora sem apoio costuma descobrir esses pontos depois, quando já não há margem para negociar.",
    "Ter tudo por escrito também protege a relação com a marca. A maior parte dos conflitos nasce de expectativa não combinada, não de má fé."]},

  {"h2": "Estratégia de longo prazo",
   "p": [
    "Uma carreira construída só por oportunidade imediata vira uma sequência de publicidades sem linha. O público não consegue dizer do que aquele perfil trata, e o valor comercial cai com o tempo.",
    "O trabalho de longo prazo é escolher com que tipo de marca a criadora quer ser associada, que assuntos ela quer dominar e como o perfil deve evoluir. Isso às vezes significa recusar dinheiro hoje para valer mais depois.",
    "É também o que permite passar de publicidade avulsa para contratos mais longos, que dão previsibilidade de renda e constroem associação real entre criadora e marca."]},

  {"h2": "O que continua sendo da criadora",
   "p": [
    "A agência não cria no lugar dela, e não deveria. A voz, o formato, o jeito de falar com a audiência e a relação com quem segue são exatamente o produto.",
    "Quando uma agência começa a escrever roteiro e padronizar fala, o resultado cai, porque o público percebe. O papel é organizar em volta da criação, não substituí-la."]},

  {"h2": "Como a agência é remunerada",
   "p": [
    "Os modelos variam, e vale entender antes de fechar. O mais comum é percentual sobre os contratos fechados, o que alinha o interesse dos dois lados: a agência ganha mais quando a criadora ganha mais.",
    "Há também formatos com valor fixo mensal, que costumam fazer sentido quando o trabalho envolve construção de carreira a longo prazo e não depende só do volume de publicidade do mês.",
    "O que precisa estar claro em qualquer modelo é o que está incluído, se há exclusividade de representação, qual o prazo do contrato e como ele pode ser encerrado."]},

  {"h2": "Quando faz sentido ter assessoria",
   "p": [
    "Costuma fazer sentido quando o volume de proposta passou do que dá para administrar sozinha, quando as negociações estão travando por falta de material organizado, ou quando a criadora percebe que está gastando mais tempo respondendo mensagem comercial do que criando.",
    "Hoje cuidamos da parte comercial de um grupo de criadoras com nichos diferentes, de conteúdo de fé e lifestyle a fitness e dicas de cidade, e a demanda que aparece é sempre a mesma: tempo para criar."]},
],
},

{
"slug": "marketing-digital-joinville-o-que-funciona",
"title": "Marketing para o comércio local de Joinville: o que funciona",
"meta_description": "O que funciona no marketing digital para comércio e serviço em Joinville: busca local, perfil no Google, conteúdo da cidade e parceria com criadores da região.",
"category": BRANDING,
"date": "2026-04-28",
"excerpt": "Negócio que atende uma cidade tem estratégia diferente de negócio que vende para o país inteiro. O que muda quando o seu cliente mora perto.",
"cta": CTA_BRANDING,
"body": [
  {"p": [
    "Boa parte do conteúdo sobre marketing digital foi escrita pensando em negócio que vende para qualquer lugar. Para quem atende uma cidade, várias dessas recomendações não se aplicam, e algumas atrapalham.",
    "Quando o cliente mora perto, alcance nacional não é vantagem, é desperdício. O jogo passa a ser aparecer para as pessoas certas dentro de um raio pequeno, e isso muda as prioridades."]},

  {"h2": "Aparecer na busca local é o básico",
   "p": [
    "A maior parte da procura por serviço começa com alguém digitando o que precisa junto com o nome da cidade ou do bairro. Quem não aparece nessa busca perde cliente que já estava decidido a contratar.",
    "O perfil da empresa no Google costuma ser o ativo mais subaproveitado do comércio local. Ele é gratuito, aparece antes do site nos resultados e mostra horário, telefone, endereço, fotos e avaliações.",
    "Manter esse perfil vivo, com informação correta, fotos recentes e categorias bem escolhidas, costuma render mais procura direta do que semanas de conteúdo novo nas redes."]},

  {"h2": "Avaliações são conteúdo",
   "p": [
    "Para negócio local, avaliação pesa muito na decisão. É a prova social mais acessível para quem nunca ouviu falar de você e está comparando duas ou três opções próximas.",
    "Pedir avaliação a cliente satisfeito precisa virar rotina, não campanha. O momento certo é logo depois da entrega, quando a experiência está fresca.",
    "Responder também importa, inclusive as negativas. Resposta educada e objetiva a uma reclamação comunica mais sobre a empresa para quem está lendo do que a reclamação em si."]},

  {"h2": "Conteúdo que fala com a cidade",
   "p": [
    "Conteúdo genérico compete com o mundo inteiro. Conteúdo que menciona bairro, referência local, rotina da cidade e sazonalidade da região conversa com quem realmente pode comprar de você.",
    "Isso vale para o assunto e para o vocabulário. Falar dos pontos que todo mundo conhece, do trajeto que as pessoas fazem, do clima e do calendário local cria identificação imediata.",
    "Tem efeito prático também na busca: mencionar naturalmente o nome da cidade e do bairro nos textos ajuda a aparecer para quem procura por ali."]},

  {"h2": "Parceria com quem já fala com a cidade",
   "p": [
    "Criadores locais costumam ter audiência concentrada na mesma região, o que é exatamente o que um negócio local precisa. Um perfil com público majoritariamente da cidade vale mais do que um nacional com números maiores.",
    "Vale sempre conferir a distribuição geográfica da audiência antes de fechar, porque nem todo perfil da cidade tem público da cidade.",
    "Perfis que falam sobre a própria região, indicando lugares e programas, são particularmente úteis para comércio e serviço com ponto físico, porque o público já está em modo de descoberta."]},

  {"h2": "Sazonalidade e agenda da cidade",
   "p": [
    "O calendário de um negócio local não é o calendário nacional de datas comemorativas. Ele é feito de eventos da cidade, período de férias escolares, alta e baixa temporada do setor e movimentos próprios da região.",
    "Mapear esses períodos com antecedência permite planejar oferta e conteúdo para quando a demanda existe, em vez de reagir depois que ela passou."]},

  {"h2": "Anúncio pago com raio pequeno",
   "p": [
    "Para negócio local, a vantagem do anúncio pago não está no alcance, está na precisão. É possível limitar a exibição a um raio de poucos quilômetros em volta do ponto, o que reduz muito o desperdício.",
    "Isso muda a expectativa de volume. O público disponível é pequeno, então o mesmo conjunto de pessoas vê o anúncio com mais frequência. Trocar a peça com regularidade passa a ser necessário para não saturar.",
    "Com orçamento baixo, costuma render mais concentrar em um objetivo só, como iniciar conversa no WhatsApp, do que dividir a verba entre vários formatos e esperar aprender com todos ao mesmo tempo."]},

  {"h2": "Não copie estratégia de quem vende para o país",
   "p": [
    "Muito do que se lê sobre crescimento em redes sociais pressupõe público ilimitado. Metas de seguidores, viralização e volume alto de publicação fazem sentido nesse contexto e pouco sentido no seu.",
    "Um perfil local com poucos milhares de seguidores da própria cidade pode sustentar um negócio inteiro. O mesmo número espalhado pelo país não sustenta nada, porque essas pessoas não podem comprar de você."]},

  {"h2": "O que priorizar",
   "p": [
    "Se a estrutura é enxuta, a ordem que costuma render mais é: perfil no Google atualizado, rotina de avaliações, atendimento rápido por mensagem e só então volume de conteúdo.",
    "Atendemos clientes em Joinville e em São Paulo, com necessidades bem diferentes justamente por causa disso. Para quem depende da cidade, o esforço concentrado perto rende mais do que alcance espalhado."]},
],
},

{
"slug": "mentoria-marketing-digital-para-quem-e",
"title": "Mentoria em marketing digital: para quem é e o que esperar",
"meta_description": "A diferença entre mentoria e consultoria em marketing digital, para quem a mentoria faz sentido e o que esperar de um acompanhamento desse tipo.",
"category": MENTORIA,
"date": "2026-04-21",
"excerpt": "Consultoria resolve o problema da empresa. Mentoria desenvolve a pessoa que vai continuar resolvendo depois que o encontro acabar.",
"cta": CTA_MENTORIA,
"body": [
  {"p": [
    "Mentoria e consultoria são vendidas quase como sinônimos, e a diferença entre elas é justamente o que determina se o investimento vai fazer sentido para você.",
    "A distinção mais útil é essa: consultoria olha para o problema e entrega um plano. Mentoria olha para a pessoa e desenvolve a capacidade dela de resolver os próximos problemas sozinha."]},

  {"h2": "A diferença na prática",
   "p": [
    "Em uma consultoria, você traz uma situação e recebe um diagnóstico com recomendações. O foco está no negócio, o entregável é o direcionamento, e a relação pode terminar quando aquela questão específica for resolvida.",
    "Em uma mentoria, o foco está em quem conduz. O trabalho é sobre repertório, critério de decisão e confiança para escolher. O entregável é menos tangível e o efeito é mais duradouro.",
    "Na prática, uma boa mentoria também resolve problemas concretos no caminho. A diferença é que ela não para no problema, ela usa o problema para desenvolver quem está sendo mentorado."]},

  {"h2": "Para quem a mentoria faz sentido",
   "p": ["Costuma funcionar bem para alguns perfis específicos:"],
   "ul": [
    "Profissional que assumiu o marketing da empresa sem formação na área e precisa ganhar critério",
    "Dono de negócio que quer entender o suficiente para conduzir a estratégia e cobrar fornecedores",
    "Criadora de conteúdo que quer transformar audiência em carreira sustentável",
    "Quem está começando a atender clientes de marketing e precisa estruturar método de trabalho",
    "Profissional que executa bem, mas trava quando precisa decidir prioridade e direção"]},

  {"h2": "Para quem não faz sentido",
   "p": [
    "Se o que falta é braço para executar, mentoria não resolve. Nesse caso o que você precisa é de alguém produzindo, não de alguém desenvolvendo sua capacidade de decidir.",
    "Também não faz sentido para quem procura uma fórmula pronta que funcione sem adaptação. Mentoria trabalha com o seu contexto, e isso exige envolvimento de quem está sendo mentorado.",
    "E não substitui a experiência de fazer. Ninguém aprende a conduzir marketing só ouvindo, o aprendizado vem do ciclo entre orientação, execução e revisão do que aconteceu."]},

  {"h2": "O que esperar de um encontro",
   "p": [
    "Uma mentoria produtiva costuma partir do que está acontecendo agora no seu trabalho. Você traz a situação real, com os números e as restrições que existem, e o encontro trabalha em cima disso.",
    "O valor aparece quando a conversa não entrega só a resposta, mas o raciocínio que levou até ela. Da segunda vez que uma situação parecida aparecer, você já sabe como pensar.",
    "É comum sair com poucas tarefas e muita clareza, o oposto do que se espera. Lista longa de ação costuma indicar que a prioridade ainda não foi definida."]},

  {"h2": "Como aproveitar melhor",
   "p": [
    "Chegue com pergunta específica em vez de pedido genérico de orientação. A diferença entre me ajuda com o Instagram e não consigo transformar alcance em cliente é a diferença entre uma conversa vaga e uma conversa útil.",
    "Leve o que já tentou, inclusive o que não funcionou. O histórico de tentativas frustradas é o material mais rico que existe, porque elimina caminhos e revela padrões.",
    "E execute entre um encontro e outro. Mentoria sem execução vira conversa agradável sem efeito, e o aprendizado só se fixa quando encontra a realidade."]},

  {"h2": "Encontro único ou acompanhamento",
   "p": [
    "Mentoria pode acontecer em formatos diferentes, e a escolha depende de onde você está.",
    "Um encontro único funciona quando existe uma decisão específica travando o avanço e você precisa de perspectiva externa para escolher. É objetivo, resolve o nó e devolve autonomia rápido.",
    "O acompanhamento ao longo de semanas faz sentido quando o objetivo é desenvolver critério, e não resolver uma questão. Ele permite o ciclo que faz o aprendizado fixar: orientar, executar, revisar o que aconteceu e ajustar."]},

  {"h2": "Como é a nossa",
   "p": [
    "A mentoria da Bertoluchi é conduzida pela Beatriz Bertoluchi, que começou como criadora de conteúdo antes de assessorar outras pessoas e de montar a agência.",
    "Isso significa uma perspectiva que vem dos dois lados: de quem já esteve na frente da câmera negociando a própria publicidade, e de quem hoje conduz a operação de uma agência que atende marcas e criadoras.",
    "O formato é personalizado para o momento de quem procura, com foco em estratégia e resolução de desafios reais, não em conteúdo padronizado.",
    "Se você não tem certeza se o seu caso pede mentoria ou consultoria, essa é uma boa primeira pergunta a levar para a conversa. Contratar o formato errado custa tempo dos dois lados, e a distinção costuma ficar clara em poucos minutos de conversa sobre o seu contexto."]},
],
},

]


def _contar_palavras(post):
    partes = []
    for bloco in post["body"]:
        if bloco.get("h2"):
            partes.append(bloco["h2"])
        partes.extend(bloco.get("p", []))
        partes.extend(bloco.get("ul", []))
    return len(" ".join(partes).split())


# tempo de leitura calculado do texto real, a 200 palavras por minuto
for _post in BLOG_POSTS:
    _post["word_count"] = _contar_palavras(_post)
    _post["read_time_min"] = max(1, round(_post["word_count"] / 200))

CATEGORIES = []
for _post in BLOG_POSTS:
    if _post["category"] not in CATEGORIES:
        CATEGORIES.append(_post["category"])

# usado nas classes de CSS e no filtro por hash da /blog.html
CATEGORY_SLUGS = {
    GESTAO: "gestao",
    SOCIAL: "social",
    BRANDING: "branding",
    CONSULTORIA: "consultoria",
    MENTORIA: "mentoria",
}

_MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
          "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def data_extenso(iso):
    ano, mes, dia = iso.split("-")
    return "%d de %s de %s" % (int(dia), _MESES[int(mes) - 1], ano)


def relacionados(post, quantos=3):
    """Mesma categoria primeiro; completa com os mais recentes se faltar."""
    mesma = [p for p in BLOG_POSTS
             if p["category"] == post["category"] and p["slug"] != post["slug"]]
    escolhidos = mesma[:quantos]
    if len(escolhidos) < 2:
        outros = [p for p in BLOG_POSTS
                  if p["slug"] != post["slug"] and p not in escolhidos]
        escolhidos += outros[:quantos - len(escolhidos)]
    return escolhidos
