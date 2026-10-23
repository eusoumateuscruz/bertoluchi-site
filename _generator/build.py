# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from common import (
    SITE, NAV, SERVICES, INFLUENCERS, TESTIMONIALS,
    SOCIAL_MEDIA_CLIENTS, INFLUENCER_BRAND_LOGOS,
    head, header, footer, whatsapp,
    influencer_card, client_card, stats_strip, brand_list, client_marquee,
    coverflow, initials,
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


def cta_band(title, sub, link=None, rotulo="Falar no WhatsApp"):
    link = link or SITE["whatsapp_link"]
    alvo = ' target="_blank" rel="noopener"' if link.startswith("http") else ""
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-band">
      <div>
        <h2>{title}</h2>
        <p>{sub}</p>
      </div>
      <a class="btn btn-light" href="{link}"{alvo}>{rotulo}</a>
    </div>
  </div>
</section>"""


def testimonial_card(t):
    fonte = ('<span class="testimonial-source">'
             '<span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> '
             'Avaliação no Google</span>') if t.get("google") else ""
    return f"""
        <div class="testimonial-card reveal">
          {fonte}
          <p>&ldquo;{t['quote']}&rdquo;</p>
          <cite>{t['author']}</cite>
        </div>"""


def review_card(t):
    """Cartão compacto da faixa de depoimentos (estilo marquee)."""
    sub = ('<span class="review-sub"><span class="review-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> Google</span>'
           if t.get("google") else '<span class="review-sub">Cliente Bertoluchi</span>')
    return f"""
          <figure class="review-card">
            <div class="review-head">
              <span class="review-avatar" aria-hidden="true">{initials(t['author'])}</span>
              <div><figcaption class="review-name">{t['author']}</figcaption>{sub}</div>
            </div>
            <blockquote class="review-body">&ldquo;{t['quote']}&rdquo;</blockquote>
          </figure>"""


def testimonial_marquee(items):
    """Duas faixas de depoimentos correndo em sentidos opostos.
    O conteúdo é repetido para o loop não ter emenda; a cópia fica escondida do leitor de tela."""
    meio = (len(items) + 1) // 2
    linhas = []
    for i, grupo in enumerate((items[:meio], items[meio:])):
        cards = "".join(review_card(t) for t in grupo)
        reverso = " review-row--reverse" if i else ""
        linhas.append(f"""
        <div class="review-row{reverso}">
          <div class="review-track">{cards}</div>
          <div class="review-track" aria-hidden="true">{cards}</div>
        </div>""")
    return f'<div class="review-marquee">{"".join(linhas)}</div>'


def campo(nome, rotulo, tipo="text", obrigatorio=True, extra=""):
    req = " required" if obrigatorio else ""
    opc = "" if obrigatorio else ' <span class="form-optional">(opcional)</span>'
    if tipo == "textarea":
        controle = f'<textarea id="{nome}" name="{nome}"{req}{extra}></textarea>'
    else:
        controle = f'<input type="{tipo}" id="{nome}" name="{nome}"{req}{extra}>'
    return f"""
          <div class="form-field">
            <label for="{nome}">{rotulo}{opc}</label>
            {controle}
          </div>"""


def seletor(nome, rotulo, opcoes):
    ops = "".join(f'<option value="{o}">{o}</option>' for o in opcoes)
    return f"""
          <div class="form-field">
            <label for="{nome}">{rotulo}</label>
            <select id="{nome}" name="{nome}" required>
              <option value="" disabled selected>Selecione</option>{ops}
            </select>
          </div>"""


def formulario(tipo, assunto, campos, botao, id_form=""):
    """Formulario enviado pelo FormSubmit.co direto para o e-mail da agencia.

    Cada envio chega como e-mail em tabela, com o assunto padronizado
    (ex.: "[Casting] Nome"), o que deixa tudo pesquisavel na caixa de entrada.
    O main.js completa o assunto com o nome e manda o visitante para
    /obrigado.html depois do envio.
    """
    ident = f' id="{id_form}"' if id_form else ""
    return f"""
        <form class="contact-form site-form reveal"{ident} action="https://formsubmit.co/{SITE['form_email']}" method="POST" data-form="{tipo}" data-assunto="{assunto}">
          <input type="hidden" name="_subject" value="{assunto}">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_next" value="{SITE['domain']}/obrigado.html">
          <input type="hidden" name="Origem" value="{tipo}">
          <input type="text" name="_honey" class="form-honey" tabindex="-1" autocomplete="off" aria-hidden="true">
          {campos}
          <button type="submit" class="btn btn-primary">{botao}</button>
          <p class="form-note">Seus dados são usados apenas pela equipe da Bertoluchi para responder a este contato.</p>
        </form>"""


def form_casting():
    campos = (
        campo("Nome", "Nome completo")
        + campo("Instagram", "Seu @ no Instagram", extra=' placeholder="@seuperfil"')
        + campo("Seguidores", "Número aproximado de seguidores", extra=' placeholder="Ex.: 25 mil"')
        + campo("Nicho", "Nicho de conteúdo", extra=' placeholder="Ex.: lifestyle, fitness, fé, maternidade"')
        + campo("Cidade", "Cidade e estado")
        + campo("WhatsApp", "WhatsApp", "tel")
        + campo("email", "E-mail", "email")
        + campo("Midia kit", "Link do mídia kit", "url", obrigatorio=False, extra=' placeholder="https://"')
        + campo("Mensagem", "Conta um pouco sobre você e por que quer ser assessorada pela Bertoluchi", "textarea")
    )
    return formulario("Casting", "[Casting] Nova inscrição de influenciadora", campos, "Enviar inscrição", "casting")


def schema_empresa():
    """JSON-LD da agência na home. Só dados que já estão no site (common.SITE)."""
    dados = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE["domain"] + "/#empresa",
        "name": SITE["full_name"],
        "alternateName": "Bertoluchi Agência",
        "url": SITE["domain"] + "/",
        "logo": SITE["domain"] + "/assets/img/logo.png",
        "image": SITE["domain"] + "/assets/img/hero-desktop.jpg",
        "description": "Agência de publicidade e marketing digital em Joinville: social media, branding e gestão de influenciadoras.",
        "email": SITE["email"],
        "telephone": SITE["phone_tel"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "R. Victor Müller, 215, Costa e Silva",
            "addressLocality": "Joinville",
            "addressRegion": "SC",
            "postalCode": "89218-460",
            "addressCountry": "BR",
        },
        "areaServed": {"@type": "City", "name": "Joinville"},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00",
            "closes": "17:00",
        }],
        "sameAs": [SITE["instagram"], SITE["linkedin"], SITE["behance"]],
    }
    return ('<script type="application/ld+json">'
            + json.dumps(dados, ensure_ascii=False) + "</script>\n")


# ---------------------------------------------------------------- HOME
def build_home():
    pillars = ""
    for i, s in enumerate(SERVICES[:3], start=1):
        pillars += f"""
        <div class="pillar-card reveal">
          <span class="pillar-index">{i:02d}</span>
          <h3>{s['title']}</h3>
          <p>{s['short']}</p>
          <a class="pillar-link" href="/servicos/{s['slug']}.html">Saiba mais →</a>
        </div>"""

    influencer_preview = coverflow(INFLUENCERS, "home")
    client_preview = client_marquee(SOCIAL_MEDIA_CLIENTS)

    testimonial_preview = testimonial_marquee(TESTIMONIALS)

    html = head(
        "Bertoluchi Agência: Gestão de Influenciadoras e Social Media em Joinville",
        "Social media, branding e gestão de influenciadoras em Joinville. Torne seu negócio uma referência nas redes sociais com a Bertoluchi Agência.",
        "/index.html",
        extra_head=schema_empresa(),
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
        <div class="hero-painel">
        <span class="eyebrow">Publicidade e marketing digital</span>
        <h1 class="hero-headline">Referência nas redes sociais em Joinville</h1>
        <p class="hero-sub">Social media com estratégia, criação de conteúdo de alta qualidade e branding, para marcas que querem crescer com consistência. E, quando faz sentido, conectamos sua marca às influenciadoras certas.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Fale com a gente</a>
          <a class="btn btn-outline-invert" href="/servicos.html">Conhecer serviços</a>
        </div>
      </div>
        </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">O que fazemos</span>
        <h2>Três frentes, um único objetivo: sua marca em evidência</h2>
        <p>Do planejamento do conteúdo ao post que sai no ar, cuidamos das redes sociais da sua marca de ponta a ponta, com identidade forte e as parcerias certas.</p>
      </div>
      <div class="pillars-grid">{pillars}</div>
    </div>
  </section>

  <section class="section section-dark">
    <div class="container">
      <div class="section-head center narrow reveal">
        <span class="eyebrow">Nossa essência</span>
        <h2>Ética, compromisso e honestidade em cada entrega</h2>
        <p>Nossa missão é impulsionar empresas no ramo digital com estratégia, conteúdo e as parcerias certas, sem perder o cuidado humano em cada entrega. Mais de 300 clientes de diversos setores já passaram pela Bertoluchi.</p>
      </div>
      {stats_strip()}
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head split reveal">
        <div>
          <span class="eyebrow">Social media</span>
          <h2>Marcas que cuidamos todos os dias</h2>
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
          <h2>Influenciadores que assessoramos</h2>
        </div>
        <a class="btn btn-outline" href="/influenciadoras.html">Ver todas</a>
      </div>
      <div class="mt-lg reveal">{influencer_preview}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <span class="eyebrow">O que dizem</span>
        <h2>Quem trabalha com a gente, indica</h2>
      </div>
      </div>
    <div class="reveal">{testimonial_preview}</div>
    <div class="container">
      <div class="review-cta reveal">
        <p>Já trabalhou com a gente? Deixe sua avaliação no Google:</p>
        <div class="review-cta-botoes">
          <a class="btn btn-primary" href="https://share.google/7EMR0wkWhQ438s8xv" target="_blank" rel="noopener">Avaliar a unidade de Joinville</a>
          <a class="btn btn-outline" href="https://share.google/lNIa2PT6v64zZGGB3" target="_blank" rel="noopener">Avaliar a unidade de Porto Ferreira</a>
        </div>
      </div>
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
            <span class="service-num">{i:02d}</span>
            <div>
              <h3>{s['title']}</h3>
              <p>{s['short']}</p>
            </div>
          </div>
          <a class="btn btn-outline" href="/servicos/{s['slug']}.html">Ver serviço</a>
        </div>"""

    html = head(
        "Serviços: Bertoluchi Agência",
        "Social media, branding, gestão de influenciadoras, criação de sites, tráfego pago, consultoria e mentoria: conheça os serviços da Bertoluchi Agência.",
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
        f'<li><a href="/servicos/{o["slug"]}.html">{o["title"]}</a></li>' for o in other
    )

    if s.get("casting"):
        botoes = '<a class="btn btn-primary btn-full" href="#casting">Quero fazer parte do casting</a>'
        cta_link = "#casting"
    else:
        link = whatsapp(s["cta_text"])
        botoes = f'<a class="btn btn-primary btn-full" href="{link}" target="_blank" rel="noopener">Solicitar proposta</a>'
        cta_link = link
    if s.get("portfolio"):
        botoes += (f'<a class="btn btn-outline btn-full mt-sm" href="{SITE["behance"]}" '
                   f'target="_blank" rel="noopener">Ver portfólio no Behance</a>')

    portfolio_html = ""
    if s.get("portfolio"):
        portfolio_html = f"""
  <section class="section">
    <div class="container">
      <div class="behance-callout reveal">
        <div>
          <span class="eyebrow">Portfólio</span>
          <p class="behance-text">Veja os projetos de branding que já criamos, com logotipos, paletas e manuais de marca completos.</p>
        </div>
        <a class="btn btn-primary" href="{SITE['behance']}" target="_blank" rel="noopener">Ver portfólio no Behance</a>
      </div>
    </div>
  </section>
"""

    casting_html = ""
    if s.get("casting"):
        casting_html = f"""
  <section class="section" id="casting-secao">
    <div class="container">
      <div class="form-split">
        <div class="section-head reveal">
          <span class="eyebrow">Casting</span>
          <h2>Quer ser assessorada pela Bertoluchi?</h2>
          <p>Nosso casting está fechado no momento. Preencha o formulário para entrar na nossa lista: avaliamos cada perfil com cuidado e entramos em contato quando abrirmos novas vagas.</p>
        </div>
        {form_casting()}
      </div>
    </div>
  </section>
"""

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
          {botoes}
        </aside>
      </div>
    </div>
  </section>

{portfolio_html}{casting_html}
  <section class="section section-alt">
    <div class="container">
      <div class="section-head full reveal">
        <span class="eyebrow">Outros serviços</span>
      </div>
      <ul class="grid-2 link-list">{other_links}</ul>
    </div>
  </section>

  {cta_band(f"Quer contratar {s['title']}?", "Fale com a gente e receba um direcionamento sob medida.", cta_link) if not s.get("casting") else ""}
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
        <h1>Influenciadores que assessoramos</h1>
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

  <section class="section">
    <div class="container">
      <div class="area-chamada reveal">
        <div>
          <span class="eyebrow">Já faz parte do casting?</span>
          <h2>Portal do influenciador</h2>
          <p>Entre com seu usuário e senha para ver as oportunidades de campanha que a Bertoluchi está fechando para você.</p>
        </div>
        <a class="btn btn-primary" href="/portal-do-influenciador.html">Entrar no portal</a>
      </div>
    </div>
  </section>

  {cta_band("É influenciadora e quer assessoria?", "Nosso casting está fechado no momento, mas você pode se inscrever na lista e ser avaliada nas próximas aberturas.", "/servicos/gestao-de-influenciadores.html#casting", "Quero me inscrever")}
</main>
"""
    html += footer()
    write("/influenciadoras.html", html)


# ---------------------------------------------------------------- RESULTADOS
def build_resultados():
    testimonial_full = "".join(testimonial_card(t) for t in TESTIMONIALS)

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
        <p>Mais de 300 clientes de diversos setores já passaram pela Bertoluchi. Veja nossos números, o portfólio de branding e o que dizem sobre a gente.</p>
      </div>

      {stats_strip(light=True)}

      <div class="behance-callout reveal mt-lg">
        <div>
          <span class="eyebrow">Portfólio</span>
          <p class="behance-text">Branding, identidade visual e mídia kit para influenciadoras: veja o portfólio completo no Behance</p>
        </div>
        <a class="btn btn-primary" href="{SITE['behance']}" target="_blank" rel="noopener">Ver portfólio no Behance</a>
      </div>

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
{formulario("Contato", "[Contato] Nova mensagem pelo site",
                   campo("Nome", "Nome") + campo("email", "E-mail", "email")
                   + campo("WhatsApp", "WhatsApp", "tel", obrigatorio=False)
                   + campo("Assunto", "Assunto", obrigatorio=False)
                   + campo("Mensagem", "Mensagem", "textarea"),
                   "Enviar mensagem")}

                <div class="contact-info reveal">
          <a class="btn btn-primary btn-full mb-sm" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Agendar no WhatsApp</a>

          <h3>Endereço</h3>
          <p>{SITE['address_line1']}<br>{SITE['address_line2']}</p>

          <h3>E-mail</h3>
          <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>

          <h3>Telefone</h3>
          <p><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></p>

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
        "Conheça alguns dos mais de 20 negócios que confiam a gestão das redes sociais à Bertoluchi Agência, em Joinville e região.",
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
        <p>São mais de 20 marcas ativas em social media, de estética e nutrição a alimentação, pet, mineração e turismo. Cada uma com estratégia própria, calendário próprio e acompanhamento de métrica.</p>
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
# Vagas abertas. Para abrir uma vaga nova, acrescente um item; para fechar,
# remova. Sem vaga, a secao some e a pagina fica so com o formulario.
# (vaga de Designer Grafico para Social Media encerrada em 2026-10-23)
VAGAS = []

# Candidaturas chegam pelo Jotform da agencia; a pagina so apresenta o
# banco de talentos e leva a pessoa ao formulario em outra aba.
JOTFORM_URL = "https://form.jotform.com/262935108328056"

AREAS_TALENTO = [
    "Design gráfico", "Social media e estratégia", "Captação e edição de vídeo",
    "Redação e copy", "Atendimento e comercial", "Tráfego pago",
]

PASSOS_CANDIDATURA = [
    ("Preencha o formulário", "Seus dados, sua área e o link do seu portfólio. O formulário abre em uma nova aba."),
    ("A equipe avalia", "Olhamos cada portfólio com calma, pensando nas demandas dos nossos clientes."),
    ("A gente te chama", "Quando surgir uma oportunidade com o seu perfil, entramos em contato pelo WhatsApp ou e-mail."),
]


def build_trabalhe_conosco():
    vagas_secao = ""
    if VAGAS:
        vagas_html = ""
        for v in VAGAS:
            tags_html = "".join(f'<li class="vaga-tag">{t}</li>' for t in v["tags"])
            req = "".join(f"<li>{r}</li>" for r in v["requisitos"])
            vagas_html += f"""
        <article class="vaga-card reveal">
          <span class="eyebrow">Vaga aberta · {v['area']}</span>
          <h3>{v['titulo']}</h3>
          <ul class="vaga-tags">{tags_html}</ul>
          <div class="vaga-card-corpo">
            <div>
              <h4>Sobre a vaga</h4>
              <p>{v['resumo']}</p>
              <h4>O que você vai fazer</h4>
              <p>{v['atividades']}</p>
            </div>
            <div>
              <h4>O que buscamos</h4>
              <ul class="lista-marcada">{req}</ul>
            </div>
          </div>
          <a class="btn btn-primary" href="{JOTFORM_URL}" target="_blank" rel="noopener">Candidatar-se a esta vaga</a>
        </article>"""
        vagas_secao = f"""
  <section class="section section-alt" id="vagas">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Oportunidades</span>
        <h2>Vagas abertas</h2>
      </div>
      <div class="vaga-lista">{vagas_html}</div>
    </div>
  </section>
"""

    passos = "".join(
        f'<li class="talentos-passo"><span class="talentos-num">{i:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
        for i, (t, d) in enumerate(PASSOS_CANDIDATURA, start=1))
    areas = "".join(f"<li>{a}</li>" for a in AREAS_TALENTO)

    n = len(VAGAS)
    desc_vagas = (f"{n} vaga aberta" if n == 1 else f"{n} vagas abertas") if n else "Banco de talentos aberto"
    botao_vagas = '<a class="btn btn-outline" href="#vagas">Ver vagas abertas</a>' if VAGAS else ""
    html = head(
        "Trabalhe conosco: vagas e banco de talentos da Bertoluchi",
        f"Trabalhe na Bertoluchi, agência de marketing digital de Joinville (SC). {desc_vagas}. "
        "Mesmo sem vaga para a sua área, cadastre-se no nosso banco de talentos.",
        "/trabalhe-conosco.html",
    )
    html += header("/trabalhe-conosco.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Trabalhe conosco</span>
        <h1>Venha construir marcas com a gente</h1>
        <p>A Bertoluchi é uma agência de marketing digital com atuação em Joinville (SC) e São Paulo. Atendemos clientes de diversos segmentos, com uma atuação direta e estratégica, sempre buscando gerar resultado real e fortalecer o posicionamento de cada marca.</p>
      </div>
      <div class="hero-actions reveal">
        <a class="btn btn-primary" href="#banco-de-talentos">Quero fazer parte</a>
        {botao_vagas}
      </div>
    </div>
  </section>
{vagas_secao}
  <section class="section{'' if VAGAS else ' section-alt'}" id="banco-de-talentos">
    <div class="container">
      <div class="talentos reveal">
        <div class="talentos-cta">
          <span class="eyebrow">Banco de talentos</span>
          <h2>Deixe seu perfil com a gente</h2>
          <p>Mesmo que hoje não tenha vaga para a sua área, cadastre-se. Quando surge uma oportunidade, é no banco de talentos que procuramos primeiro.</p>
          <a class="btn btn-primary btn-talentos" href="{JOTFORM_URL}" target="_blank" rel="noopener">
            Preencher formulário
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>
          </a>
          <p class="talentos-nota">Abre em uma nova aba.</p>
        </div>
        <ol class="talentos-passos">{passos}</ol>
      </div>

      <div class="talentos-extra">
        <div class="talentos-bloco reveal">
          <h3>Áreas em que buscamos talentos</h3>
          <ul class="talentos-areas">{areas}</ul>
        </div>
        <div class="talentos-bloco talentos-bloco--destaque reveal">
          <h3>Capriche no portfólio</h3>
          <p>Deixe um link do Behance, Instagram, Drive ou site com os seus trabalhos. É o que a gente usa para avaliar sua candidatura.</p>
        </div>
      </div>

      <div class="vaga-rodape reveal">
        <p>Dúvidas? Fale com a Beatriz: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
      </div>
    </div>
  </section>
</main>
"""
    html += footer()
    write("/trabalhe-conosco.html", html)


# ------------------------------------------------- AREA DA INFLUENCIADORA
# Login e painel ficam na mesma pagina; o JS consulta /api/oportunidades e
# mostra o painel quando a sessao existe. Contas e oportunidades moram no
# Global Config da Vercel (ver api/_area.js), nunca neste repositorio publico.
def build_area_influenciadora():
    html = head(
        "Portal do influenciador: Bertoluchi Agência",
        "Acesso exclusivo dos influenciadores assessorados pela Bertoluchi às oportunidades de campanha.",
        "/portal-do-influenciador.html",
        extra_head='<meta name="robots" content="noindex, nofollow">\n',
    )
    html += header("/portal-do-influenciador.html")
    html += f"""
<main id="conteudo">
  <section class="section page-hero area-hero">
    <div class="container">
      <div class="area-grid" data-area>
        <div class="section-head reveal">
          <span class="eyebrow">Portal do influenciador</span>
          <h1>Suas oportunidades, num só lugar</h1>
          <p>Aqui você acompanha as campanhas que a Bertoluchi está fechando para você: marca, formato, cachê e prazo de cada uma.</p>
          <ul class="area-pontos">
            <li><strong>Exclusivo</strong> para quem faz parte do nosso casting</li>
            <li><strong>Atualizado</strong> sempre que surge uma nova proposta</li>
            <li><strong>Sem acesso?</strong> Peça seu usuário para a equipe pelo WhatsApp</li>
          </ul>
        </div>

        <form class="contact-form site-form area-login reveal" data-area-login novalidate>
          <h2 class="area-login-titulo">Entrar</h2>
          <div class="form-field">
            <label for="area-usuario">Usuário</label>
            <input type="text" id="area-usuario" name="usuario" autocomplete="username" autocapitalize="none" spellcheck="false" required placeholder="seu @ do Instagram">
          </div>
          <div class="form-field">
            <label for="area-senha">Senha</label>
            <div class="area-senha">
              <input type="password" id="area-senha" name="senha" autocomplete="current-password" required>
              <button type="button" class="area-ver-senha" data-ver-senha aria-label="Mostrar senha">Mostrar</button>
            </div>
          </div>
          <p class="area-erro" data-area-erro role="alert" hidden></p>
          <button type="submit" class="btn btn-primary btn-full">Entrar</button>
          <p class="form-note">Esqueceu a senha? <a href="{whatsapp('Olá! Faço parte do casting da Bertoluchi e preciso de ajuda com o acesso ao portal do influenciador.')}" target="_blank" rel="noopener">Fale com a equipe</a>.</p>
        </form>
      </div>

      <div class="area-painel" data-area-painel hidden>
        <div class="area-painel-topo">
          <div>
            <span class="eyebrow">Portal do influenciador</span>
            <h1 data-area-ola>Olá!</h1>
          </div>
          <button type="button" class="btn btn-outline" data-area-sair>Sair</button>
        </div>
        <div class="area-resumo" data-area-resumo></div>
        <div class="area-filtros" role="tablist" data-area-filtros>
          <button type="button" class="area-filtro is-ativo" data-filtro="todas">Todas</button>
          <button type="button" class="area-filtro" data-filtro="aberta">Abertas</button>
          <button type="button" class="area-filtro" data-filtro="em andamento">Em andamento</button>
          <button type="button" class="area-filtro" data-filtro="encerrada">Encerradas</button>
        </div>
        <div class="area-lista" data-area-lista></div>
      </div>
    </div>
  </section>
</main>
"""
    html += footer().replace('<script src="/assets/js/main.js"></script>',
                             '<script src="/assets/js/main.js"></script>\n<script src="/assets/js/area-influenciadora.js"></script>')
    write("/portal-do-influenciador.html", html)


# ---------------------------------------------------------------- OBRIGADO
def build_obrigado():
    html = head(
        "Recebemos seu envio: Bertoluchi Agência",
        "Obrigado pelo contato com a Bertoluchi Agência.",
        "/obrigado.html",
        extra_head='<meta name="robots" content="noindex">\n',
    )
    html += header("")
    html += f"""
<main id="conteudo">
  <section class="section page-hero">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Tudo certo</span>
        <h1>Recebemos seu envio</h1>
        <p>Obrigado! Nossa equipe vai analisar as informações e retorna pelo contato que você deixou. Se for urgente, fale com a gente pelo WhatsApp.</p>
      </div>
      <div class="hero-actions reveal">
        <a class="btn btn-primary" href="/index.html">Voltar ao início</a>
        <a class="btn btn-outline" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Falar no WhatsApp</a>
      </div>
    </div>
  </section>
</main>
"""
    html += footer()
    write("/obrigado.html", html)


# ---------------------------------------------------------------- PRIVACIDADE
def build_privacidade():
    # Texto padrão de LGPD montado pela Destaq: precisa de revisão do CEO antes de publicar.
    html = head(
        "Política de privacidade: Bertoluchi Agência",
        "Como a Bertoluchi Agência trata os dados pessoais enviados pelo site, de acordo com a Lei Geral de Proteção de Dados (LGPD).",
        "/politica-de-privacidade.html",
    )
    html += header("")
    html += f"""
<!-- Texto padrão de LGPD: precisa de revisão do CEO antes de publicar. -->
<main id="conteudo">
  <article class="post">
    <div class="container container-narrow">
      <header class="post-head">
        <span class="eyebrow">Privacidade</span>
        <h1>Política de privacidade</h1>
        <p class="post-meta">Atualizada em 19 de outubro de 2026</p>
      </header>

      <div class="post-body">
        <p>Esta política explica como a {SITE['full_name']} trata os dados pessoais de quem visita o site e entra em contato com a agência, de acordo com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>

        <h2>Quem é a responsável pelos dados</h2>
        <p>{SITE['full_name']}, {SITE['address_line1']}, {SITE['address_line2']}. E-mail: <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>

        <h2>Quais dados coletamos</h2>
        <ul>
          <li>Dados que você envia pelos formulários: nome, e-mail, WhatsApp, assunto e mensagem. Na inscrição de influenciadoras, também o perfil no Instagram, o número aproximado de seguidores, o nicho, a cidade e o link do mídia kit.</li>
          <li>Dados que você compartilha quando fala com a gente pelo WhatsApp ou por e-mail.</li>
          <li>Dados técnicos de navegação, como endereço IP e tipo de navegador, registrados pelos serviços que mantêm o site no ar e carregam as fontes do site.</li>
        </ul>

        <h2>Para que usamos os dados</h2>
        <ul>
          <li>Responder ao seu contato e enviar propostas que você pediu.</li>
          <li>Avaliar inscrições de influenciadoras e candidaturas a vagas.</li>
          <li>Cumprir obrigações legais e manter o site funcionando com segurança.</li>
        </ul>
        <p>Não vendemos dados pessoais e não usamos os dados enviados pelo site para outras finalidades sem avisar você.</p>

        <h2>Com quem compartilhamos</h2>
        <p>Os formulários são enviados para o e-mail da agência pelo serviço FormSubmit. As conversas pelo WhatsApp passam pela plataforma da Meta. O site fica hospedado em um provedor de nuvem. Esses serviços tratam os dados apenas para prestar o serviço contratado.</p>

        <h2>Cookies</h2>
        <p>Hoje o site não usa cookies de publicidade nem de medição de audiência. Se isso mudar, esta política será atualizada.</p>

        <h2>Por quanto tempo guardamos</h2>
        <p>Guardamos os dados pelo tempo necessário para atender ao seu pedido e cumprir obrigações legais. Depois disso, eles são apagados.</p>

        <h2>Seus direitos</h2>
        <p>Você pode pedir a confirmação de que tratamos seus dados, o acesso, a correção, a exclusão, a portabilidade e informações sobre o compartilhamento, além de retirar o consentimento a qualquer momento. Basta escrever para <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>

        <h2>Mudanças nesta política</h2>
        <p>Esta política pode ser atualizada. A data da última versão fica no topo da página.</p>
      </div>
    </div>
  </article>
</main>
"""
    html += footer()
    write("/politica-de-privacidade.html", html)


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
    build_area_influenciadora()
    build_obrigado()
    build_privacidade()


if __name__ == "__main__":
    main()
