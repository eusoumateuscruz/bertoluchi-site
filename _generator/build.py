# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from common import (
    SITE, NAV, SERVICES, INFLUENCERS, TESTIMONIALS, CASES,
    SOCIAL_MEDIA_CLIENTS, INFLUENCER_BRAND_LOGOS,
    head, header, footer,
    influencer_card, client_card, stats_strip, brand_list, client_marquee,
)
from blog_posts import (
    BLOG_POSTS, CATEGORIES, CATEGORY_SLUGS, data_extenso, relacionados,
)

# O site e servido a partir da raiz do repositorio (a Vercel publica o repo
# como estatico, sem build step). Forcamos quebra de linha LF para o
# arquivo gerado no Windows nao entrar no git com CRLF.
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def write(path, html):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", path)


def picture(base, alt, cls="", sizes="100vw"):
    return f"""<picture>
      <source srcset="/assets/img/{base}.webp" type="image/webp">
      <img src="/assets/img/{base}.jpg" alt="{alt}" class="{cls}" loading="lazy" sizes="{sizes}">
    </picture>"""


def cta_band(title, sub):
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-band">
      <div>
        <h2>{title}</h2>
        <p>{sub}</p>
      </div>
      <a class="btn btn-light" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------- HOME
def build_home():
    pillars = ""
    for i, s in enumerate(SERVICES[:3], start=1):
        pillars += f"""
        <div class="pillar-card reveal">
          <span class="pillar-index">0{i}</span>
          <h3>{s['title']}</h3>
          <p>{s['short']}</p>
          <a class="pillar-link" href="/servicos/{s['slug']}.html">Saiba mais →</a>
        </div>"""

    influencer_preview = "".join(influencer_card(inf) for inf in INFLUENCERS[:4])
    client_preview = client_marquee(SOCIAL_MEDIA_CLIENTS)

    testimonial_preview = ""
    for t in TESTIMONIALS[:3]:
        testimonial_preview += f"""
        <div class="testimonial-card reveal">
          <p>&ldquo;{t['quote']}&rdquo;</p>
          <cite>{t['author']}</cite>
        </div>"""

    case = CASES[0]

    html = head(
        "Bertoluchi Agência: Gestão de Influenciadoras e Social Media em Joinville",
        "Gestão completa de influenciadoras, social media e branding. Torne seu negócio uma referência nas redes sociais com a Bertoluchi Agência.",
        "/index.html",
    )
    html += header("/index.html")
    html += f"""
<main id="conteudo">

  <section class="hero">
    <div class="hero-media">
      <picture>
        <source media="(max-width: 720px)" srcset="/assets/img/hero-mobile.webp" type="image/webp">
        <source media="(max-width: 720px)" srcset="/assets/img/hero-mobile.jpg">
        <source srcset="/assets/img/hero-desktop.webp" type="image/webp">
        <img src="/assets/img/hero-desktop.jpg" alt="Beatriz Bertoluchi, fundadora da Bertoluchi Agência" fetchpriority="high">
      </picture>
    </div>
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <div class="container">
        <span class="eyebrow">Publicidade e marketing digital</span>
        <h1 class="hero-headline">Torne seu negócio uma referência nas redes sociais</h1>
        <p class="hero-sub">Gestão completa de influenciadoras, planejamento estratégico e criação de conteúdo de alta qualidade, para marcas e criadoras que querem crescer com consistência.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Fale com a gente</a>
          <a class="btn btn-outline-invert" href="/servicos.html">Conhecer serviços</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">O que fazemos</span>
        <h2>Três frentes, um único objetivo: sua marca em evidência</h2>
        <p>Da negociação da parceria certa até o post que sai no ar, cuidamos de cada etapa da sua presença digital.</p>
      </div>
      <div class="pillars-grid">{pillars}</div>
    </div>
  </section>

  <section class="section section-dark">
    <div class="container">
      <div class="section-head center narrow reveal">
        <span class="eyebrow">Nossa essência</span>
        <h2>Ética, compromisso e honestidade em cada entrega</h2>
        <p>Nossa missão é impulsionar empresas no ramo digital, conectando marcas e influenciadoras de forma estratégica, sem perder o cuidado humano em cada parceria.</p>
      </div>
      {stats_strip()}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head split reveal">
        <div>
          <span class="eyebrow">Social media</span>
          <h2>Marcas que cuidamos todo dia</h2>
          <p>Os negócios que confiam a presença digital à nossa equipe.</p>
        </div>
        <a class="btn btn-outline" href="/clientes-social-media.html">Ver todos os clientes</a>
      </div>
      <div class="reveal">{client_preview}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head split reveal">
        <div>
          <span class="eyebrow">Talentos</span>
          <h2>Influenciadoras que assessoramos</h2>
        </div>
        <a class="btn btn-outline" href="/influenciadoras.html">Ver todas</a>
      </div>
      <div class="influencer-grid mt-lg">{influencer_preview}</div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="case-card">
        <span class="eyebrow">{case['tag']}</span>
        <h3>{case['name']}</h3>
        <p>{case['text']}</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">O que dizem</span>
        <h2>Quem trabalha com a gente, indica</h2>
      </div>
      <div class="testimonial-grid">{testimonial_preview}</div>
    </div>
  </section>

  {cta_band("Vamos tornar sua marca uma referência nas redes?", "Fale com a nossa equipe e receba um direcionamento sob medida para o seu momento.")}

</main>
"""
    html += footer()
    write("/index.html", html)


# ---------------------------------------------------------------- SOBRE
def build_sobre():
    html = head(
        "Sobre a Bertoluchi: quem está por trás da agência",
        "Conheça a história da Bertoluchi Agência e da fundadora Beatriz Bertoluchi, além da missão, visão e valores que guiam cada projeto.",
        "/sobre.html",
    )
    html += header("/sobre.html")
    html += f"""
<main id="conteudo">

  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Sobre a Bertoluchi</span>
        <h1>Uma agência nascida dentro da própria criação de conteúdo</h1>
      </div>

      <div class="bio-split reveal">
        <div class="bio-media">
          <picture>
            <source media="(max-width: 860px)" srcset="/assets/img/sobre-mobile.webp" type="image/webp">
            <source media="(max-width: 860px)" srcset="/assets/img/sobre-mobile.jpg">
            <source srcset="/assets/img/sobre-desktop.webp" type="image/webp">
            <img src="/assets/img/sobre-desktop.jpg" alt="Beatriz Bertoluchi, fundadora e CEO da Bertoluchi Agência">
          </picture>
        </div>
        <div class="bio-copy">
          <h2>Beatriz Bertoluchi</h2>
          <p>Beatriz começou como influenciadora, quando uma marca lhe deu a oportunidade de apresentar um produto ao seu público. <strong>Deu certo</strong>, e, no mesmo período em que se tornou mãe, passou a compartilhar sua experiência com quem também queria entender o universo da criação de conteúdo, oferecendo cursos e mentorias.</p>
          <p>O <strong>currículo</strong> ganhou corpo com especializações em marketing e mídias sociais. E o passo seguinte veio naturalmente: gerenciar a carreira de outras influenciadoras e prestar serviço para marcas de branding e social media.</p>
          <p><strong>Assim nasceu a Bertoluchi Publicidade e Marketing Digital</strong>, uma agência que entende o criador de conteúdo por dentro, porque começou sendo um.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">O que nos move</span>
        <h2>Missão, visão e valores</h2>
      </div>
      <div class="values-grid reveal">
        <div class="value-card">
          <h3>Missão</h3>
          <p>Impulsionar empresas e criadoras de conteúdo no ramo digital, com estratégia, criatividade e acompanhamento próximo em cada etapa do crescimento.</p>
        </div>
        <div class="value-card">
          <h3>Visão</h3>
          <p>Ser a ponte de confiança entre marcas e influenciadoras, construindo parcerias que geram resultado real para os dois lados.</p>
        </div>
        <div class="value-card">
          <h3>Valores</h3>
          <p>Ética, compromisso e honestidade em cada negociação, em cada entrega, em cada relação de longo prazo que construímos.</p>
        </div>
      </div>
    </div>
  </section>

  {cta_band("Quer conhecer a equipe de perto?", "Agende uma conversa e entenda como podemos caminhar juntos.")}

</main>
"""
    html += footer()
    write("/sobre.html", html)


# ---------------------------------------------------------------- SERVICOS (hub)
def build_servicos_hub():
    rows = ""
    for i, s in enumerate(SERVICES, start=1):
        rows += f"""
        <div class="service-row reveal">
          <div class="service-row-left">
            <span class="service-num">0{i}</span>
            <div>
              <h3>{s['title']}</h3>
              <p>{s['short']}</p>
            </div>
          </div>
          <a class="btn btn-outline" href="/servicos/{s['slug']}.html">Ver serviço</a>
        </div>"""

    html = head(
        "Serviços: Bertoluchi Agência",
        "Gestão de influenciadoras, social media, branding, consultoria e mentoria: conheça os serviços da Bertoluchi Agência.",
        "/servicos.html",
    )
    html += header("/servicos.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Serviços</span>
        <h1>Tudo o que sua marca precisa para crescer nas redes</h1>
        <p>Cada serviço pode ser contratado isoladamente ou combinado, de acordo com o momento do seu negócio.</p>
      </div>
      <div class="mt-lg">{rows}</div>
    </div>
  </section>

  {cta_band("Não sabe por onde começar?", "Conta pra gente o momento da sua marca e a gente te diz qual serviço faz mais sentido.")}
</main>
"""
    html += footer()
    write("/servicos.html", html)


# ---------------------------------------------------------------- SERVICO (detalhe)
def build_service_detail(s):
    body_html = "".join(f"<p>{p}</p>" for p in s["body"])
    highlights = "".join(f"<li>{h}</li>" for h in s["highlights"])

    other = [x for x in SERVICES if x["slug"] != s["slug"]]
    other_links = "".join(
        f'<li><a href="/servicos/{o["slug"]}.html">{o["title"]}</a></li>' for o in other[:4]
    )

    html = head(
        f"{s['title']}: Serviços Bertoluchi",
        s["summary"],
        f"/servicos/{s['slug']}.html",
    )
    html += header("/servicos.html")
    html += f"""
<main id="conteudo">
  <section class="service-hero">
    <div class="container">
      <span class="eyebrow">Serviços / {s['title']}</span>
      <h1>{s['title']}</h1>
      <p>{s['summary']}</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="service-body reveal">
        <div class="service-copy">
          {body_html}
        </div>
        <aside class="service-side">
          <h3>O que está incluso</h3>
          <ul>{highlights}</ul>
          <a class="btn btn-primary btn-full" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Solicitar proposta</a>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head full reveal">
        <span class="eyebrow">Outros serviços</span>
      </div>
      <ul class="grid-2 link-list">{other_links}</ul>
    </div>
  </section>

  {cta_band(f"Quer contratar {s['title']}?", "Fale com a gente e receba um direcionamento sob medida.")}
</main>
"""
    html += footer()
    write(f"/servicos/{s['slug']}.html", html)


# ---------------------------------------------------------------- INFLUENCIADORAS
def build_influenciadoras():
    cards = "".join(influencer_card(inf) for inf in INFLUENCERS)
    sem_foto = len([i for i in INFLUENCERS if not i.get("img")])
    # a nota so faz sentido enquanto alguem estiver sem foto
    nota = ""
    if sem_foto:
        plural = "perfis ainda aparecem" if sem_foto > 1 else "perfil ainda aparece"
        nota = (f'<p class="note-block">{sem_foto} {plural} com o card de iniciais, '
                'porque o material fotográfico não chegou. Assim que as fotos forem '
                'enviadas, esta seção é atualizada.</p>')

    html = head(
        "Influenciadoras: Bertoluchi Agência",
        "Conheça as influenciadoras assessoradas pela Bertoluchi Agência.",
        "/influenciadoras.html",
    )
    html += header("/influenciadoras.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Influenciadoras</span>
        <h1>Talentos que assessoramos</h1>
        <p>Cada uma com um nicho, um público e uma forma própria de se conectar. A gente cuida da parte comercial para que elas continuem focadas em criar.</p>
      </div>
      <div class="influencer-grid mt-lg">{cards}</div>
      {nota}
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">Campanhas</span>
        <h2>Marcas que já confiaram em nossas influenciadoras</h2>
        <p>Empresas que já rodaram campanha publicitária com os perfis que assessoramos.</p>
      </div>
      <div class="reveal">{brand_list()}</div>
    </div>
  </section>

  {cta_band("É influenciadora e quer assessoria?", "Fale com a gente e entenda como podemos cuidar da parte comercial da sua carreira.")}
</main>
"""
    html += footer()
    write("/influenciadoras.html", html)


# ---------------------------------------------------------------- RESULTADOS
def build_resultados():
    cases_html = ""
    for c in CASES:
        cases_html += f"""
        <div class="case-card reveal">
          <span class="eyebrow">{c['tag']}</span>
          <h3>{c['name']}</h3>
          <p>{c['text']}</p>
        </div>"""

    testimonial_full = ""
    for t in TESTIMONIALS:
        testimonial_full += f"""
        <div class="testimonial-card reveal">
          <p>&ldquo;{t['quote']}&rdquo;</p>
          <cite>{t['author']}</cite>
        </div>"""

    html = head(
        "Resultados: Bertoluchi Agência",
        "Cases e depoimentos de quem já trabalhou com a Bertoluchi Agência.",
        "/resultados.html",
    )
    html += header("/resultados.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Resultados</span>
        <h1>Cases e depoimentos</h1>
        <p>Estamos organizando cases com números completos de cada cliente. Por enquanto, veja os números que já podemos confirmar, o projeto social que apoiamos e o que dizem sobre a gente.</p>
      </div>

      {stats_strip(light=True)}

      <div class="behance-callout reveal mt-lg">
        <div>
          <span class="eyebrow">Portfólio</span>
          <p class="behance-text">Fazemos mídia kit para influenciadoras, veja o portfólio completo no Behance</p>
        </div>
        <a class="btn btn-primary" href="{SITE['behance']}" target="_blank" rel="noopener">Ver portfólio no Behance</a>
      </div>

      <div class="mt-lg">{cases_html}</div>
      <p class="note-block">Métricas de resultado (engajamento, crescimento de seguidores, conversão) serão adicionadas aqui assim que autorizadas por cada cliente. Nenhum número é publicado sem confirmação.</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">Depoimentos</span>
        <h2>Quem trabalha com a gente, indica</h2>
      </div>
      <div class="testimonial-grid">{testimonial_full}</div>
    </div>
  </section>

  {cta_band("Quer ser o próximo case de sucesso?", "Fale com a gente e vamos construir esse resultado juntos.")}
</main>
"""
    html += footer()
    write("/resultados.html", html)


# ---------------------------------------------------------------- BLOG
def post_card(post, reveal=True):
    cat_slug = CATEGORY_SLUGS[post["category"]]
    cls = "post-card" + (" reveal" if reveal else "")
    return f"""
        <article class="{cls}" data-categoria="{cat_slug}">
          <a class="post-card-link" href="/blog/{post['slug']}.html">
            <span class="post-cover post-cover--{cat_slug}" aria-hidden="true"></span>
            <span class="post-card-body">
              <span class="post-tag">{post['category']}</span>
              <span class="post-card-title">{post['title']}</span>
              <span class="post-card-excerpt">{post['excerpt']}</span>
              <span class="post-card-meta">
                <time datetime="{post['date']}">{data_extenso(post['date'])}</time>
                <span class="post-dot" aria-hidden="true"></span>
                {post['read_time_min']} min de leitura
              </span>
            </span>
          </a>
        </article>"""


def build_blog():
    cards = "".join(post_card(p) for p in BLOG_POSTS)
    filtros = '<button class="filtro-chip is-active" type="button" data-filtro="todos">Todos</button>'
    for c in CATEGORIES:
        filtros += (f'<button class="filtro-chip" type="button" '
                    f'data-filtro="{CATEGORY_SLUGS[c]}">{c}</button>')

    html = head(
        "Blog: marketing digital, social media e influenciadoras",
        f"Artigos práticos sobre gestão de influenciadoras, social media, branding e "
        f"marketing digital, escritos pela equipe da Bertoluchi Agência.",
        "/blog.html",
    )
    html += header("/blog.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Blog</span>
        <h1>Conteúdo sobre marketing digital e redes sociais</h1>
        <p>Artigos práticos sobre gestão de influenciadoras, social media e branding, escritos a partir do que a gente vê no dia a dia com clientes e criadoras.</p>
      </div>

      <div class="filtros reveal" role="group" aria-label="Filtrar artigos por categoria">
        {filtros}
      </div>

      <div class="post-grid" data-post-grid>{cards}</div>
      <p class="filtro-vazio" data-filtro-vazio hidden>Nenhum artigo nesta categoria por enquanto.</p>
    </div>
  </section>

  {cta_band("Prefere falar com a gente direto?", "Conta o momento da sua marca e a gente indica por onde começar.")}
</main>
"""
    html += footer()
    write("/blog.html", html)


def build_blog_post(post):
    cat_slug = CATEGORY_SLUGS[post["category"]]
    caminho = f"/blog/{post['slug']}.html"
    canonical = SITE["domain"] + caminho

    corpo = ""
    for bloco in post["body"]:
        if bloco.get("h2"):
            corpo += f'\n        <h2>{bloco["h2"]}</h2>'
        for par in bloco.get("p", []):
            corpo += f'\n        <p>{par}</p>'
        if bloco.get("ul"):
            itens = "".join(f"<li>{i}</li>" for i in bloco["ul"])
            corpo += f'\n        <ul class="lista-marcada">{itens}</ul>'

    rel = relacionados(post)
    rel_cards = "".join(post_card(r) for r in rel)

    artigo_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["meta_description"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "articleSection": post["category"],
        "inLanguage": "pt-BR",
        "wordCount": post["word_count"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "author": {
            "@type": "Organization",
            "name": SITE["full_name"],
            "url": SITE["domain"],
        },
        "publisher": {
            "@type": "Organization",
            "name": SITE["full_name"],
            "url": SITE["domain"],
            "logo": {
                "@type": "ImageObject",
                "url": SITE["domain"] + "/assets/img/logo.png",
            },
        },
    }
    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Blog",
             "item": SITE["domain"] + "/blog.html"},
            {"@type": "ListItem", "position": 2, "name": post["category"],
             "item": SITE["domain"] + "/blog.html#" + cat_slug},
            {"@type": "ListItem", "position": 3, "name": post["title"],
             "item": canonical},
        ],
    }
    extra = (
        '<script type="application/ld+json">'
        + json.dumps(artigo_ld, ensure_ascii=False)
        + '</script>\n<script type="application/ld+json">'
        + json.dumps(breadcrumb_ld, ensure_ascii=False)
        + '</script>\n'
    )

    html = head(post["title"], post["meta_description"], caminho,
                og_type="article", extra_head=extra)
    html += header("/blog.html")
    html += f"""
<main id="conteudo">
  <article class="post">
    <div class="container container-narrow">
      <nav class="breadcrumb" aria-label="Trilha de navegação">
        <a href="/blog.html">Blog</a>
        <span aria-hidden="true">/</span>
        <a href="/blog.html#{cat_slug}">{post['category']}</a>
        <span aria-hidden="true">/</span>
        <span aria-current="page">{post['title']}</span>
      </nav>

      <header class="post-head">
        <span class="eyebrow">{post['category']}</span>
        <h1>{post['title']}</h1>
        <p class="post-meta">
          <time datetime="{post['date']}">{data_extenso(post['date'])}</time>
          <span class="post-dot" aria-hidden="true"></span>
          {post['read_time_min']} min de leitura
        </p>
      </header>

      <div class="post-body">{corpo}
      </div>

      <aside class="post-cta">
        <p>Quer ajuda para colocar isso em prática?</p>
        <div class="post-cta-acoes">
          <a class="btn btn-primary" href="{post['cta']['href']}">{post['cta']['label']}</a>
          <a class="btn btn-outline" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Falar no WhatsApp</a>
        </div>
      </aside>
    </div>
  </article>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Continue lendo</span>
        <h2>Artigos relacionados</h2>
      </div>
      <div class="post-grid">{rel_cards}</div>
    </div>
  </section>
</main>
"""
    html += footer()
    write(caminho, html)


# ---------------------------------------------------------------- CONTATO
def build_contato():
    html = head(
        "Contato: Bertoluchi Agência",
        f"Fale com a Bertoluchi Agência. {SITE['address_line1']}, {SITE['address_line2']}.",
        "/contato.html",
    )
    html += header("/contato.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Contato</span>
        <h1>Vamos conversar</h1>
        <p>Preencha o formulário e nossa equipe retorna assim que possível. Se preferir, fale direto pelo WhatsApp.</p>
      </div>

      <div class="contact-grid mt-lg">
        <form class="contact-form reveal" action="#" method="post">
          <div class="form-field">
            <label for="name">Nome</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-field">
            <label for="email">E-mail</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-field">
            <label for="subject">Assunto</label>
            <input type="text" id="subject" name="subject">
          </div>
          <div class="form-field">
            <label for="message">Mensagem</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Enviar mensagem</button>
          <p class="form-note">Este formulário ainda precisa ser conectado a um serviço de envio (ex.: Formspree, Netlify Forms) antes da publicação.</p>
        </form>

        <div class="contact-info reveal">
          <a class="btn btn-primary btn-full mb-sm" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Agendar no WhatsApp</a>

          <h3>Endereço</h3>
          <p>{SITE['address_line1']}<br>{SITE['address_line2']}</p>

          <h3>E-mail</h3>
          <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>

          <h3>Telefone</h3>
          <p>{SITE['phone_display']}</p>

          <h3>Horário</h3>
          <p>{SITE['hours']}</p>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += footer()
    write("/contato.html", html)


# ---------------------------------------------------------------- CLIENTES SOCIAL MEDIA
def build_clientes_social_media():
    cards = "".join(client_card(c) for c in SOCIAL_MEDIA_CLIENTS)

    html = head(
        "Clientes de Social Media: Bertoluchi Agência",
        f"Conheça os {len(SOCIAL_MEDIA_CLIENTS)} negócios que confiam a gestão das redes sociais à Bertoluchi Agência, em Joinville e região.",
        "/clientes-social-media.html",
    )
    html += header("/clientes-social-media.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Clientes</span>
        <h1>Quem confia a presença digital à nossa equipe</h1>
        <p>São {len(SOCIAL_MEDIA_CLIENTS)} marcas ativas em social media, de estética e nutrição a alimentação, pet, mineração e turismo. Cada uma com estratégia própria, calendário próprio e acompanhamento de métrica.</p>
      </div>
      <div class="client-grid mt-lg">{cards}</div>
    </div>
  </section>

  {cta_band("Quer sua marca nessa lista?", "Fale com a gente e receba uma proposta de social media sob medida para o seu negócio.")}
</main>
"""
    html += footer()
    write("/clientes-social-media.html", html)


# ---------------------------------------------------------------- TRABALHE CONOSCO
def build_trabalhe_conosco():
    tags = [
        "Remoto · Santa Catarina e São Paulo",
        "Regime · PJ",
        "Início · Imediato",
        "Salário · a partir de R$ 2.000 (a combinar)",
    ]
    tags_html = "".join(f'<li class="vaga-tag">{t}</li>' for t in tags)

    buscamos = [
        "Experiência comprovada em design gráfico",
        "Domínio de pelo menos um editor de imagem, preferencialmente Canva e Photoshop",
        "Disponibilidade de segunda a sexta, das 9h às 17h",
        "Possibilidade de atuar como PJ",
        "Início imediato",
    ]
    buscamos_html = "".join(f"<li>{b}</li>" for b in buscamos)

    html = head(
        "Vaga: Designer Gráfico para Social Media na Bertoluchi",
        "A Bertoluchi está contratando designer gráfico(a) para social media. "
        "Vaga remota para Santa Catarina e São Paulo, regime PJ e início imediato. "
        "Candidatura pelo WhatsApp, com portfólio.",
        "/trabalhe-conosco.html",
    )
    html += header("/trabalhe-conosco.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Vaga aberta · Design</span>
        <h1>Designer Gráfico para Social Media</h1>
        <p>A Bertoluchi, agência de marketing digital, está contratando um(a) designer gráfico(a) para social media.</p>
      </div>

      <ul class="vaga-tags reveal">{tags_html}</ul>

      <div class="vaga-corpo">
        <div class="reveal">
          <h2>Sobre a vaga</h2>
          <p>Vaga remota, para candidatos de Santa Catarina e São Paulo. Contratação PJ, com início imediato.</p>
        </div>

        <div class="reveal">
          <h2>Sobre a Bertoluchi</h2>
          <p>A Bertoluchi é uma agência de marketing digital com atuação em Joinville (SC) e São Paulo. Atendemos clientes de diversos segmentos, com uma atuação direta e estratégica no mercado, sempre buscando gerar resultado real e fortalecer o posicionamento de cada marca.</p>
        </div>

        <div class="reveal">
          <h2>O que você vai fazer:</h2>
          <p>Desenvolver criativos e carrosséis para os clientes de social media da agência.</p>
        </div>

        <div class="reveal">
          <h2>O que buscamos</h2>
          <ul class="lista-marcada">{buscamos_html}</ul>
        </div>

        <div class="destaque-portfolio reveal">
          <p><strong>Portfólio:</strong> deixe um link (Behance, Instagram, Drive ou site) com os seus trabalhos, é o que a gente usa pra avaliar sua candidatura.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-band">
        <div>
          <h2>Quer se candidatar?</h2>
          <p>Manda seu portfólio e uma mensagem pra gente pelo WhatsApp.</p>
        </div>
        <a class="btn btn-light" href="{SITE['whatsapp_link_vaga_designer']}" target="_blank" rel="noopener">Aplicar pelo WhatsApp</a>
      </div>

      <div class="vaga-rodape reveal">
        <p>Dúvidas sobre a vaga? Fale com a Beatriz: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        <p>Vaga aberta até o preenchimento da posição.</p>
      </div>
    </div>
  </section>
</main>
"""
    html += footer()
    write("/trabalhe-conosco.html", html)


def main():
    build_home()
    build_sobre()
    build_servicos_hub()
    for s in SERVICES:
        build_service_detail(s)
    build_influenciadoras()
    build_clientes_social_media()
    build_resultados()
    build_blog()
    for _p in BLOG_POSTS:
        build_blog_post(_p)
    build_contato()
    build_trabalhe_conosco()


if __name__ == "__main__":
    main()
