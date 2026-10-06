# -*- coding: utf-8 -*-
"""
Dados centrais do site Bertoluchi Agência.
Toda informação factual (endereço, telefone, e-mail, links) vem do site
atual (bertoluchi.com.br) ou de materiais enviados por Mateus.
Nenhum número, depoimento ou dado de contato foi inventado.
"""

SITE = {
    "name": "Bertoluchi",
    "full_name": "Bertoluchi Publicidade e Marketing Digital",
    "tagline": "Publicidade e marketing digital",
    "domain": "https://www.bertoluchi.com.br",
    "phone_display": "(47) 9254-5015",
    "whatsapp_link": "https://wa.me/554792545015?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20reuni%C3%A3o.",
    "email": "beatriz@bertoluchiagencia.com.br",
    "address_line1": "R. Victor Müller, 215 - Costa e Silva",
    "address_line2": "Joinville - SC, 89218-460",
    "hours": "Segunda a sexta, das 9h às 17h",
    "instagram": "https://www.instagram.com/bertoluchiagencia/",
    "linkedin": "https://www.linkedin.com/company/bertoluchi/",
    "behance": "https://www.behance.net/beatrizbertolu",
    "whatsapp_link_vaga_designer": "https://wa.me/554792545015?text=Ol%C3%A1%21%20Tenho%20interesse%20na%20vaga%20de%20Designer%20Gr%C3%A1fico%20para%20Social%20Media.%20Meu%20portf%C3%B3lio%3A%20",
    # Formularios do site enviam para este e-mail via FormSubmit.co
    # (sem chave; o primeiro envio pede ativacao no proprio e-mail).
    "form_email": "beatriz@bertoluchiagencia.com.br",
}

# Numeros confirmados pela Beatriz no PDF de ajustes (2026-10-06).
STATS = [
    ("+200", "Brandings realizados"),
    ("+10", "Influenciadores assessorados"),
    ("+20", "Clientes de social media"),
    ("+300", "Clientes já atendidos"),
]


def whatsapp(texto):
    """Link de WhatsApp com mensagem pronta."""
    from urllib.parse import quote
    return "https://wa.me/554792545015?text=" + quote(texto)

NAV = [
    ("Início", "/index.html"),
    ("Sobre", "/sobre.html"),
    ("Serviços", "/servicos.html"),
    ("Influenciadoras", "/influenciadoras.html"),
    ("Clientes", "/clientes-social-media.html"),
    ("Resultados", "/resultados.html"),
    ("Blog", "/blog.html"),
]

SERVICES = [
    {
        "slug": "social-media",
        "title": "Social Media",
        "short": "Presença digital consistente, do planejamento à publicação.",
        "summary": "Gestão de redes sociais projetada para as necessidades específicas de cada cliente, com estratégia, criação de conteúdo e acompanhamento de métrica.",
        "body": [
            "Cada cliente recebe uma estratégia própria de redes sociais, elaborada a partir do momento atual da marca, do público que ela quer atingir e dos objetivos de negócio por trás da presença digital.",
            "O trabalho inclui planejamento de conteúdo, produção criativa, publicação e monitoramento de métricas, com ajuste de rota sempre que o resultado pedir.",
            "Os planos são personalizados por cliente. Se você quer entender o que caberia na sua realidade, fale com a gente.",
        ],
        "highlights": [
            "Estratégia de conteúdo personalizada por cliente",
            "Produção criativa (roteiro, gravação, edição e arte)",
            "Calendário editorial e publicação",
            "Monitoramento de métricas com relatório periódico",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de receber uma proposta de social media.",
    },
    {
        "slug": "branding",
        "title": "Branding",
        "short": "Identidade visual e verbal que sustenta a marca no tempo.",
        "summary": "Construção de identidade de marca: logotipo, paleta, elementos visuais e manual de marca, para uma imagem coesa em qualquer ponto de contato.",
        "body": [
            "Trabalhamos os elementos que tornam uma marca reconhecível: logotipo, paleta de cores, tipografia, símbolos e o conjunto de regras que garantem consistência visual em todos os materiais.",
            "O objetivo é criar uma representação autêntica e memorável, que sustente não só a marca, mas os produtos e serviços por trás dela, com uma conexão clara com o público-alvo.",
        ],
        "highlights": [
            "Criação ou reformulação de logotipo",
            "Paleta de cores e sistema tipográfico",
            "Manual de marca",
            "Materiais de marketing alinhados à identidade",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de receber uma proposta de branding.",
        "portfolio": True,
    },
    {
        "slug": "gestao-de-influenciadores",
        "title": "Gestão de Influenciadoras",
        "short": "Assessoria completa para quem vive de criar conteúdo.",
        "summary": "Cuidamos das parcerias comerciais, negociações e crescimento de marca pessoal de influenciadoras digitais, para que a criação de conteúdo continue sendo o foco.",
        "body": [
            "A assessoria de influenciadoras existe para tirar da sua frente o que não é criação: negociação de parceria, alinhamento comercial e organização da rotina de entregas.",
            "Acompanhamos métricas de engajamento e alcance para embasar cada negociação com dado real, não com achismo. E cuidamos do desenvolvimento da marca pessoal a médio e longo prazo, para que cada parceria feche com marcas que fazem sentido para o seu público.",
            "Fazem parte do serviço: mídia kit atualizado, apoio em negociação comercial, curadoria de propostas e organização de calendário de entregas.",
        ],
        "highlights": [
            "Negociação e intermediação de parcerias comerciais",
            "Mídia kit profissional atualizado por temporada",
            "Acompanhamento de métricas de engajamento e alcance",
            "Desenvolvimento de marca pessoal a médio e longo prazo",
        ],
        "casting": True,
    },
    {
        "slug": "sites",
        "title": "Criação de Sites",
        "short": "Site profissional para sua marca ser encontrada no Google.",
        "summary": "Sites institucionais rápidos, bonitos e preparados para o Google, para transformar quem chega das redes sociais em cliente.",
        "body": [
            "Sua presença digital não termina no Instagram. Um site profissional dá credibilidade à marca, reúne seus serviços em um só lugar e ajuda você a ser encontrado por quem pesquisa no Google.",
            "Desenvolvemos o site com a mesma identidade da sua marca: layout pensado para celular, textos claros, botão de WhatsApp em destaque e estrutura otimizada para buscas.",
            "Para entregar com qualidade técnica, o desenvolvimento é feito em parceria com uma equipe especializada em sites e Google, e todo o atendimento continua com a Bertoluchi.",
        ],
        "highlights": [
            "Site institucional com a identidade da sua marca",
            "Layout pensado primeiro para o celular",
            "Estrutura otimizada para aparecer no Google",
            "Integração com WhatsApp, Instagram e formulários",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de receber uma proposta de criação de site.",
    },
    {
        "slug": "trafego-pago",
        "title": "Tráfego Pago",
        "short": "Anúncios no Google e no Instagram para atrair mais clientes.",
        "summary": "Gestão de anúncios no Google Ads e no Meta Ads (Instagram e Facebook), com foco em gerar contatos e vendas, não só curtidas.",
        "body": [
            "O conteúdo orgânico constrói a marca. O tráfego pago acelera: coloca sua mensagem na frente de quem já está procurando o que você vende, ou de quem tem o perfil do seu cliente ideal.",
            "Planejamos as campanhas a partir do objetivo do negócio, acompanhamos os resultados de perto e ajustamos verba e anúncios conforme os números mostram o que funciona.",
            "As campanhas são operadas em parceria com uma equipe especializada em Google Ads e rastreamento, e todo o atendimento continua com a Bertoluchi.",
        ],
        "highlights": [
            "Campanhas no Google Ads",
            "Campanhas no Meta Ads (Instagram e Facebook)",
            "Configuração de rastreamento de conversões",
            "Acompanhamento de resultados com relatório periódico",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de receber uma proposta de tráfego pago.",
    },
    {
        "slug": "consultoria",
        "title": "Consultoria",
        "short": "Direcionamento estratégico, pontual ou contínuo.",
        "summary": "Duas formas de acompanhamento: uma conversa objetiva para destravar uma dúvida específica, ou um acompanhamento permanente para quem quer crescimento sustentável.",
        "body": [
            "Consultoria Express: um encontro de 30 minutos para tirar as dúvidas mais urgentes sobre o digital, direto ao ponto.",
            "Consultoria Contínua: acompanhamento estratégico permanente, com foco em crescimento sustentável e otimização constante das ações de marketing digital e publicidade.",
        ],
        "highlights": [
            "Consultoria Express: 30 minutos, foco em uma dúvida específica",
            "Consultoria Contínua: acompanhamento estratégico permanente",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de saber mais sobre a consultoria.",
    },
    {
        "slug": "mentoria",
        "title": "Mentoria",
        "short": "Orientação para profissionais que querem crescer no digital.",
        "summary": "Mentoria conduzida pela CEO Beatriz Bertoluchi, com foco em desenvolvimento de estratégia, resolução de desafios reais e crescimento profissional.",
        "body": [
            "Voltada a profissionais e empresas que querem avançar no marketing digital com direcionamento especializado e personalizado.",
            "O conteúdo é conduzido pela própria Beatriz Bertoluchi, com base na experiência de quem construiu a carreira dentro do universo da criação de conteúdo antes de assessorar outras pessoas.",
        ],
        "highlights": [
            "Conduzida pela CEO Beatriz Bertoluchi",
            "Foco em estratégia e resolução de desafios reais",
            "Formato personalizado para o momento do profissional",
        ],
        "cta_text": "Olá! Vim pelo site e gostaria de saber mais sobre a mentoria.",
    },
]

# Influenciadoras assessoradas, conforme os destaques do Instagram da
# agência. Fotos baixadas do acervo da agência e otimizadas localmente
# (webp + fallback jpg). Quem ainda não tiver foto cai no card de
# iniciais, definido em influencer_card().
INFLUENCERS = [
    {"name": "Larissa Estrada", "handle": "@larissaestradaa",
     "niche": "Fé | Lifestyle", "img": "influ-larissaestradaa"},
    {"name": "Pastor Lipão", "handle": "@pastorlipao",
     "niche": "Life Style | Fé", "img": "influ-pastorlipao"},
    {"name": "Nidyellen Rodrigues", "handle": "@nidyellenr",
     "niche": "Life Style | Rotina", "img": "influ-nidyellenr"},
    {"name": "O que fazer em Joinville", "handle": "@oquefazeremjoinville",
     "niche": "Dicas de locais em Joinville e região", "img": "influ-oquefazeremjoinville"},
    {"name": "Mari Marques", "handle": "@mari.marques_",
     "niche": "Lifestyle | Fitness", "img": "influ-mari-marques"},
    {"name": "Flávia Gabriela", "handle": "@fglins",
     "niche": "Lifestyle | Empreendedorismo | Dicas", "img": "influ-flavia-gabriela"},
    {"name": "Leticia Levasz", "handle": "@_leticiafit_",
     "niche": "Fitness | Lifestyle", "img": "influ-leticia-levasz"},
    {"name": "Allan Popeye", "handle": "@allan_popeye",
     "niche": "Luta | Lifestyle", "img": "influ-allan-popeye"},
    # Novos em 2026-10-06 (fotos enviadas pela Beatriz). Nome como aparece
    # no proprio perfil do Instagram; nicho ainda nao informado.
    {"name": "Yasmin Andrade", "handle": "@yasmin.andrade__",
     "niche": "", "img": "influ-yasmin-andrade"},
    {"name": "ÉÉÉguaaa", "handle": "@eeeguaaa",
     "niche": "Joinville | Santa Catarina", "img": "influ-eeeguaaa"},
]

# Clientes ativos de social media (lista enviada por Mateus).
SOCIAL_MEDIA_CLIENTS = [
    {"name": "Tainá Dias", "handle": "@tainadiasesteticista", "link": "https://www.instagram.com/tainadiasesteticista/"},
    {"name": "Pytave", "handle": "@pytavefitness", "link": "https://www.instagram.com/pytavefitness/"},
    {"name": "André - A2 Personal", "handle": "@a2_personalfitness", "link": "https://www.instagram.com/a2_personalfitness/"},
    {"name": "Porto Pet", "handle": "@portopetpf", "link": "https://www.instagram.com/portopetpf/"},
    {"name": "Tejada's Café", "handle": "@tejadascafe", "link": "https://www.instagram.com/tejadascafe/"},
    {"name": "Sr. Tejada Coxinhas", "handle": "@srtejadacoxinhas", "link": "https://www.instagram.com/srtejadacoxinhas/"},
    {"name": "Arge Auto Escola", "handle": "@argeautoescola", "link": "https://www.instagram.com/argeautoescola/"},
    {"name": "Giovanna Giocondo", "handle": "@dragiovannagiocondo", "link": "https://www.instagram.com/dragiovannagiocondo/"},
    {"name": "SOS Mangueiras", "handle": "@sosmangueiraspf", "link": "https://www.instagram.com/sosmangueiraspf/"},
    {"name": "Loja Petrópolis", "handle": "@lojapetropolis_", "link": "https://www.instagram.com/lojapetropolis_/"},
    {"name": "Veiga", "handle": "@mineracaoveiga", "link": "https://www.instagram.com/mineracaoveiga/"},
    {"name": "Ideal Medical", "handle": "@idealemergencias", "link": "https://www.instagram.com/idealemergencias/"},
    {"name": "Bertoluchi", "handle": "@bertoluchiagencia", "link": "https://www.instagram.com/bertoluchiagencia/"},
    {"name": "Perfect Her", "handle": "@perfecther.oficial", "link": "https://www.instagram.com/perfecther.oficial/"},
    {"name": "Suéllen", "handle": "@suellenjungernutri", "link": "https://www.instagram.com/suellenjungernutri/"},
    {"name": "Congonhas Travel", "handle": "@congonhastravellcc", "link": "https://www.instagram.com/congonhastravellcc/"},
    {"name": "Amanda Vencel", "handle": "@dra.amandavencel", "link": "https://www.instagram.com/dra.amandavencel/"},
    {"name": "OTTO HOUSE", "handle": "@ottohouselarepatrimonio", "link": "https://www.instagram.com/ottohouselarepatrimonio/"},
]

# Marcas que já fizeram campanha publicitária com as influenciadoras
# assessoradas (lista enviada pela agência). Logos baixados de fonte oficial
# (site da marca, Wikimedia Commons ou perfil oficial) em 2026-10-06, a pedido
# da Beatriz. Sem logo confirmado, o card mostra o nome.
INFLUENCER_BRAND_LOGOS = [
    ("Havan", "havan.svg"), ("Starbucks", "starbucks.svg"),
    ("McDonald's", "mcdonalds.svg"), ("Shopping Mueller Joinville", "mueller-joinville.png"),
    ("Garten Shopping Joinville", "garten-shopping.svg"), ("Espaço Laser", "espaco-laser.png"),
    ("Atacadão", "atacadao.svg"), ("Hipermais", "hipermais.png"),
    ("Komprão", "komprao.png"), ("Lavô", "lavo.png"),
    ("Editora Vida", "editora-vida.png"), ("Girando Show", None),
    ("Growth", "growth.png"), ("AVI", None),
    ("Easy YSY", None), ("Madero", "madero.png"),
    ("Jerônimo", "jeronimo.png"), ("Leaves", "leaves.png"),
    ("Döhler", "dohler.svg"),
]

# Depoimentos reais, coletados do site atual (autorização de uso ainda
# pendente de confirmação por Mateus — ver checklist de bloqueantes).
TESTIMONIALS = [
    # Avaliacoes recentes do Perfil da Empresa no Google (prints no PDF de
    # ajustes enviado pela Beatriz em 2026-10-06).
    {"quote": "Já estamos há um ano juntos e só tenho a agradecer por toda a parceria e dedicação. A agência vem acompanhando de perto o crescimento da PYTAVE e fazendo parte de cada evolução da nossa marca. Muito obrigada por todo o trabalho e carinho com a gente!", "author": "Carliana Alves", "google": True},
    {"quote": "Desde que essa empresa se tornou nossa agência de marketing, nosso Instagram evoluiu significativamente. Eles possuem inúmeras ideias criativas de conteúdo, que têm impulsionado de forma notável a qualidade das nossas redes sociais.", "author": "Enzo Benazzi", "google": True},
    {"quote": "Excelente agência! Equipe muito profissional, criativa e atenciosa. Estamos muito satisfeitos com o trabalho e com os resultados. Recomendo!", "author": "Lucimara Benazzi", "google": True},
    {"quote": "Excelente atendimento, uma equipe organizada e prestativa. Trouxeram resultados incríveis para a gente. Recomendo sempre.", "author": "Elaine Stepanski", "google": True},
    {"quote": "Excelentes profissionais!! Ótimo atendimento!!", "author": "Dra. Giovana Giocondo", "google": True},
    {"quote": "Super indico a Bertoluchi!!", "author": "Mariana Toews", "google": True},
    {"quote": "Comprometimento, dedicação, criatividade e responsabilidade são alguns adjetivos que definem a agência Bertoluchi.", "author": "Joana Ostrovski"},
    {"quote": "Sem sombra de dúvidas, um eterno agradecimento à Agência Bertoluchi, que viu potencial e acreditou em mim.", "author": "Thayná"},
    {"quote": "Sou cliente há 2 anos da agência e tive muito retorno positivo nas captações, engajamento e seguidores nas redes sociais.", "author": "Ketlyn Alves"},
    {"quote": "Recomendo fortemente para qualquer pessoa ou empresa que queira levar seu marketing digital ao próximo nível.", "author": "Taíssa Souza"},
    {"quote": "Empresa séria e com compromisso com o cliente, entregando muitos resultados.", "author": "Amanda Rezende"},
    {"quote": "Um dos maiores acertos foi ter escolhido a agência para o desenvolvimento da nossa marca e cuidar das nossas redes sociais.", "author": "LED Coworking"},
    {"quote": "Conheci a agência e me encantei desde o primeiro contato. A equipe é maravilhosa e muito alto astral.", "author": "Clini.ko"},
]


FONTS_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Archivo+Expanded:wght@700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
)


def initials(name):
    """Iniciais para o card de influenciadora sem foto."""
    ignorar = {"que", "fazer", "em", "de", "do", "da", "e", "dos", "das"}
    palavras = [w for w in name.split() if w.lower() not in ignorar and w[:1].isalpha()]
    return "".join(w[0] for w in palavras[:2]).upper()


def story_chrome(inf):
    """Nome, @ e nicho na base do card vertical (formato reels)."""
    niche = f'<span class="story-niche">{inf["niche"]}</span>' if inf.get("niche") else ""
    return f"""
            <div class="story-bottom">
              <strong class="story-name">{inf['name']}</strong>
              <span class="story-handle">{inf['handle']}</span>
              {niche}
            </div>"""


def influencer_card(inf, reveal=True):
    """Card de influenciadora. Sem foto, cai no bloco de iniciais."""
    cls = "influencer-card" + (" reveal" if reveal else "")
    perfil = "https://www.instagram.com/" + inf["handle"][1:] + "/"
    niche = f'<span class="influencer-niche">{inf["niche"]}</span>' if inf.get("niche") else ""
    if inf.get("img"):
        visual = f"""<picture>
            <source srcset="/assets/img/{inf['img']}.webp" type="image/webp">
            <img src="/assets/img/{inf['img']}.jpg" alt="{inf['name']}, influenciadora assessorada pela Bertoluchi" loading="lazy" decoding="async">
          </picture>"""
    else:
        cls += " influencer-card--placeholder"
        visual = f'<span class="influencer-initials" aria-hidden="true">{initials(inf["name"])}</span>'
    return f"""
        <a class="{cls} story-card" href="{perfil}" target="_blank" rel="noopener" aria-label="{inf['name']} ({inf['handle']}) no Instagram">
          {visual}{story_chrome(inf)}
        </a>"""


def coverflow(items, id_suffix="home"):
    """Carrossel 3D estilo capa de album.

    Adaptado ao projeto: INFLUENCERS guarda "img" como nome-base do arquivo
    (ex.: influ-morguih), nao como URL. Entao servimos <picture> com webp e
    fallback jpg, igual ao resto do site. Quem nao tiver foto cai no bloco
    de iniciais, o mesmo usado em influencer_card().
    """
    cards = ""
    for it in items:
        title = it["name"]
        partes = [it.get("handle", "")]
        if it.get("niche"):
            partes.append(it["niche"])
        subtitle = " &middot; ".join([p for p in partes if p])
        if it.get("img"):
            visual = f"""<picture>
               <source srcset="/assets/img/{it['img']}.webp" type="image/webp">
               <img src="/assets/img/{it['img']}.jpg" alt="{title}, influenciadora assessorada pela Bertoluchi" loading="lazy" decoding="async">
             </picture>"""
        else:
            visual = (f'<span class="coverflow-initials" aria-hidden="true">'
                      f'{initials(title)}</span>')
        cards += f"""
           <div class="coverflow-card story-card" data-title="{title}" data-subtitle="{subtitle}">
             {visual}{story_chrome(it)}
           </div>"""
    return f"""
       <div class="coverflow" data-coverflow id="coverflow-{id_suffix}">
         <div class="coverflow-frame">
           <div class="coverflow-stage">{cards}
           </div>
           <button class="coverflow-nav coverflow-prev" type="button" aria-label="Anterior">&larr;</button>
           <button class="coverflow-nav coverflow-next" type="button" aria-label="Próximo">&rarr;</button>
         </div>
         <p class="coverflow-caption" aria-live="polite"></p>
         <div class="coverflow-dots"></div>
       </div>
"""


def client_card(c, reveal=True):
    cls = "client-card" + (" reveal" if reveal else "")
    return f"""
        <a class="{cls}" href="{c['link']}" target="_blank" rel="noopener">
          <span class="client-name">{c['name']}</span>
          <span class="client-handle">{c['handle']}</span>
        </a>"""


def stats_strip(light=False):
    """Numeros confirmados pela agencia (ver STATS)."""
    cells = "".join(
        f"""
        <div class="stat-item reveal">
          <div class="stat-number">{n}</div>
          <div class="stat-label">{label}</div>
        </div>""" for n, label in STATS
    )
    cls = "stats-strip stats-strip--light" if light else "stats-strip"
    return f'<div class="{cls}">{cells}</div>'


def marquee(itens, rotulo):
    """Faixa de wordmarks. itens: lista de (texto, link ou None).

    O conteudo e duplicado para o loop nao ter emenda; a copia fica
    aria-hidden e some quando o visitante pede menos movimento.
    Sao nomes tratados tipograficamente, nunca logotipo de terceiro.
    """
    def bloco(clone):
        marca = ' data-clone aria-hidden="true"' if clone else ""
        partes = []
        for i, (texto, link) in enumerate(itens):
            if i:
                partes.append(f'<span class="marquee-sep"{marca}></span>')
            if link:
                tab = ' tabindex="-1"' if clone else ""
                partes.append(
                    f'<a class="wordmark" href="{link}" target="_blank" '
                    f'rel="noopener"{marca}{tab}>{texto}</a>')
            else:
                partes.append(f'<span class="wordmark"{marca}>{texto}</span>')
        return "".join(partes)

    return f"""<div class="marquee" role="group" aria-label="{rotulo}">
        <div class="marquee-track">{bloco(False)}{bloco(True)}</div>
      </div>"""


def brand_list():
    """Faixa animada de logos das marcas, no mesmo esquema do marquee."""
    def bloco(clone):
        marca = ' aria-hidden="true" data-clone' if clone else ""
        partes = []
        for nome, arq in INFLUENCER_BRAND_LOGOS:
            if arq:
                alt = "" if clone else nome
                conteudo = f'<img src="/assets/img/marcas/{arq}" alt="{alt}" loading="lazy" decoding="async">'
            else:
                conteudo = f'<span class="logo-tile-nome">{nome}</span>'
            partes.append(f'<span class="logo-tile"{marca}>{conteudo}</span>')
        return "".join(partes)

    return f"""<div class="marquee marquee--logos" role="group" aria-label="Marcas que já fizeram campanha com nossas influenciadoras">
        <div class="marquee-track">{bloco(False)}{bloco(True)}</div>
      </div>"""


def client_marquee(clientes):
    return marquee([(c["name"], c["link"]) for c in clientes],
                   "Clientes de social media da Bertoluchi")


def head(title, description, path="/index.html", og_image="/assets/img/hero-desktop.jpg",
         og_type="website", extra_head=""):
    canonical = SITE["domain"] + path
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['domain']}{og_image}">
<meta property="og:site_name" content="Bertoluchi Agência">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE['domain']}{og_image}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="48x48" href="/assets/img/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/img/icon-512.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
{FONTS_LINK}
<link rel="stylesheet" href="/assets/css/style.css">
{extra_head}<script>document.documentElement.classList.add("js-reveal");</script>
</head>
<body>
"""


def header(active_path):
    links = ""
    mobile_links = ""
    for i, (label, href) in enumerate(NAV, start=1):
        active = " active" if href == active_path else ""
        links += f'<li><a class="nav-link{active}" href="{href}">{label}</a></li>'
        mobile_links += (
            f'<li><a class="mobile-nav-link{active}" href="{href}">'
            f'<span class="mobile-nav-index">{i:02d}</span>'
            f'<span class="mobile-nav-label">{label}</span>'
            f'</a></li>'
        )
    # O drawer e o scrim ficam FORA do <header> de proposito: quando o header
    # rola, ele ganha backdrop-filter, e backdrop-filter cria bloco de
    # contencao para descendentes position:fixed. Dentro do header, o drawer
    # colapsaria para a altura do header em vez de ocupar a tela.
    return f"""
<a class="skip-link" href="#conteudo">Pular para conteúdo</a>
<header class="site-header" data-header>
  <div class="container header-inner">
    <a href="/index.html" class="brand" aria-label="Bertoluchi, página inicial">
      <img src="/assets/img/logo.png" alt="Bertoluchi, Publicidade e marketing digital" width="176" height="46" class="brand-logo">
    </a>
    <nav class="main-nav" aria-label="Navegação principal">
      <ul class="nav-list">{links}</ul>
    </nav>
    <a class="btn btn-primary btn-header" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Fale com a gente</a>
    <button class="menu-toggle" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu" aria-label="Abrir menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="menu-scrim" data-menu-scrim></div>
<aside class="mobile-menu" id="mobile-menu" data-mobile-menu aria-hidden="true">
  <div class="mobile-menu-head">
    <img src="/assets/img/logo.png" alt="Bertoluchi" class="mobile-menu-logo">
    <button class="menu-close" data-menu-toggle aria-label="Fechar menu">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
        <path d="M6 6l12 12M18 6L6 18"/>
      </svg>
    </button>
  </div>
  <nav class="mobile-menu-nav" aria-label="Navegação mobile">
    <ul class="mobile-nav-list">{mobile_links}</ul>
  </nav>
  <div class="mobile-menu-foot">
    <a class="btn btn-primary mobile-menu-cta" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Fale com a gente</a>
    <div class="mobile-menu-social">
      <a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a>
      <span class="mobile-menu-social-dot">&middot;</span>
      <a href="mailto:{SITE['email']}">{SITE['email']}</a>
    </div>
  </div>
</aside>
"""


def footer():
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="/assets/img/logo-claro.png" alt="Bertoluchi" width="176" height="46" class="footer-logo">
      <p>Social media, branding e gestão de influenciadoras para marcas que querem se tornar referência nas redes sociais.</p>
      <div class="footer-social">
        <a href="{SITE['instagram']}" target="_blank" rel="noopener" aria-label="Instagram da Bertoluchi">Instagram</a>
        <a href="{SITE['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn da Bertoluchi">LinkedIn</a>
        <a href="{SITE['behance']}" target="_blank" rel="noopener" aria-label="Behance da Bertoluchi">Behance</a>
      </div>
    </div>
    <div class="footer-col">
      <h3>Navegação</h3>
      <ul>
        <li><a href="/sobre.html">Sobre</a></li>
        <li><a href="/servicos.html">Serviços</a></li>
        <li><a href="/influenciadoras.html">Influenciadoras</a></li>
        <li><a href="/clientes-social-media.html">Clientes</a></li>
        <li><a href="/resultados.html">Resultados</a></li>
        <li><a href="/blog.html">Blog</a></li>
        <li><a href="/contato.html">Contato</a></li>
        <li><a href="/trabalhe-conosco.html">Trabalhe conosco</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h3>Contato</h3>
      <ul>
        <li>{SITE['address_line1']}</li>
        <li>{SITE['address_line2']}</li>
        <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
        <li><a href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">{SITE['phone_display']}</a></li>
        <li>{SITE['hours']}</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>&copy; <span data-year></span> Bertoluchi Publicidade e Marketing Digital. Todos os direitos reservados.</p>
  </div>
</footer>
<a class="whatsapp-float" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
  <svg viewBox="0 0 32 32" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M16.02 3C9.4 3 4 8.38 4 15c0 2.36.64 4.56 1.85 6.5L4 29l7.68-1.8A11.9 11.9 0 0 0 16.02 27C22.64 27 28 21.62 28 15S22.64 3 16.02 3Zm0 2c5.5 0 10 4.48 10 10s-4.5 10-10 10a9.9 9.9 0 0 1-5.06-1.38l-.36-.21-4.53 1.06 1.1-4.36-.24-.38A9.9 9.9 0 0 1 6 15c0-5.52 4.5-10 10.02-10Zm-3.36 5.02c-.2 0-.53.08-.8.38-.28.3-1.06 1.03-1.06 2.52 0 1.48 1.08 2.92 1.23 3.12.15.2 2.1 3.36 5.2 4.58 2.58 1.02 3.1.82 3.66.77.56-.05 1.8-.73 2.06-1.44.25-.7.25-1.3.18-1.43-.08-.13-.28-.2-.58-.36-.3-.15-1.8-.9-2.08-1-.28-.1-.48-.15-.68.15-.2.3-.78 1-.96 1.2-.18.2-.35.23-.65.08-.3-.15-1.26-.47-2.4-1.5-.9-.8-1.5-1.78-1.68-2.08-.18-.3-.02-.46.13-.61.13-.13.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05-.38-.02-.53-.08-.15-.68-1.72-.95-2.35-.24-.58-.5-.5-.68-.5h-.56Z"/></svg>
</a>
<script src="/assets/js/main.js"></script>
</body>
</html>"""
