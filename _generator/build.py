# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from common import (
    SITE, NAV, SERVICES, INFLUENCERS, TESTIMONIALS, CASES,
    SOCIAL_MEDIA_CLIENTS, INFLUENCER_BRAND_LOGOS,
    head, header, footer,
    influencer_card, client_card, stats_strip, brand_list,
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
    client_preview = "".join(client_card(c) for c in SOCIAL_MEDIA_CLIENTS[:8])

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
      <div class="section-head center reveal" style="max-width:640px">
        <span class="eyebrow" style="color:#F4D9C4;-webkit-text-fill-color:#F4D9C4">Nossa essência</span>
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
          <p>Uma parte dos negócios que confiam a presença digital à nossa equipe.</p>
        </div>
        <a class="btn btn-outline" href="/clientes-social-media.html">Ver todos os clientes</a>
      </div>
      <div class="client-grid">{client_preview}</div>
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

  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Sobre a Bertoluchi</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Uma agência nascida dentro da própria criação de conteúdo</h1>
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
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Serviços</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Tudo o que sua marca precisa para crescer nas redes</h1>
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
          <a class="btn btn-primary" style="width:100%" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Solicitar proposta</a>
        </aside>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head reveal" style="max-width:none">
        <span class="eyebrow">Outros serviços</span>
      </div>
      <ul class="grid-2" style="font-family:var(--font-heading);font-weight:700;font-size:1.1rem">{other_links}</ul>
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

    html = head(
        "Influenciadoras: Bertoluchi Agência",
        "Conheça as influenciadoras assessoradas pela Bertoluchi Agência.",
        "/influenciadoras.html",
    )
    html += header("/influenciadoras.html")
    html += f"""
<main id="conteudo">
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Influenciadoras</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Talentos que assessoramos</h1>
        <p>Cada uma com um nicho, um público e uma forma própria de se conectar. A gente cuida da parte comercial para que elas continuem focadas em criar.</p>
      </div>
      <div class="influencer-grid mt-lg">{cards}</div>
      <p class="note-block">{sem_foto} perfis ainda aparecem com o card de iniciais, porque o material fotográfico não chegou. Assim que as fotos forem enviadas, esta seção é atualizada.</p>
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
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Resultados</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Cases e depoimentos</h1>
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
def build_blog():
    html = head(
        "Blog: Bertoluchi Agência",
        "Conteúdo sobre marketing digital, redes sociais e gestão de influenciadoras.",
        "/blog.html",
    )
    html += header("/blog.html")
    html += f"""
<main id="conteudo">
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Blog</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Conteúdo sobre marketing digital e redes sociais</h1>
      </div>
      <div class="blog-empty mt-lg reveal">
        <h2>Primeiros artigos a caminho</h2>
        <p>Estamos preparando os primeiros conteúdos do blog. Em breve, artigos sobre gestão de influenciadoras, social media e branding, direto aqui.</p>
      </div>
    </div>
  </section>
</main>
"""
    html += footer()
    write("/blog.html", html)


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
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Contato</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Vamos conversar</h1>
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
          <a class="btn btn-primary" style="width:100%;margin-bottom:8px" href="{SITE['whatsapp_link']}" target="_blank" rel="noopener">Agendar no WhatsApp</a>

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
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Clientes</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Quem confia a presença digital à nossa equipe</h1>
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
    areas = [
        "Social Media", "Design", "Atendimento", "Comercial",
        "Influenciadora parceira", "Outro",
    ]
    options = "".join(f'<option value="{a}">{a}</option>' for a in areas)

    html = head(
        "Trabalhe conosco: banco de talentos da Bertoluchi",
        "Deixe seu currículo no banco de talentos da Bertoluchi Agência. Quando abrir uma posição de social media, design, atendimento ou comercial, falamos com você.",
        "/trabalhe-conosco.html",
    )
    html += header("/trabalhe-conosco.html")
    html += f"""
<main id="conteudo">
  <section class="section" style="padding-top:clamp(120px,16vw,160px)">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Banco de talentos</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Trabalhe com a gente</h1>
        <p>No momento não temos uma vaga aberta fixa. Mesmo assim, os currículos que chegam aqui ficam no nosso banco de talentos: quando surge uma posição, é para essa lista que olhamos primeiro.</p>
      </div>

      <div class="contact-grid mt-lg">
        <form class="contact-form reveal" action="#" method="post">
          <div class="form-field">
            <label for="tc-nome">Nome</label>
            <input type="text" id="tc-nome" name="nome" autocomplete="name" required>
          </div>
          <div class="form-field">
            <label for="tc-email">E-mail</label>
            <input type="email" id="tc-email" name="email" autocomplete="email" required>
          </div>
          <div class="form-field">
            <label for="tc-telefone">Telefone</label>
            <input type="tel" id="tc-telefone" name="telefone" autocomplete="tel" required>
          </div>
          <div class="form-field">
            <label for="tc-area">Área de interesse</label>
            <select id="tc-area" name="area" required>
              <option value="">Selecione uma área</option>
              {options}
            </select>
          </div>
          <div class="form-field">
            <label for="tc-portfolio">Link do portfólio ou Instagram</label>
            <input type="url" id="tc-portfolio" name="portfolio" placeholder="https://" inputmode="url">
          </div>
          <div class="form-field">
            <label for="tc-mensagem">Mensagem</label>
            <textarea id="tc-mensagem" name="mensagem" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Enviar para o banco de talentos</button>
          <p class="form-note">Este formulário ainda precisa ser conectado a um serviço de envio (ex.: Formspree, Netlify Forms) antes da publicação. Enquanto isso, nada é enviado ao clicar no botão.</p>
        </form>

        <div class="contact-info reveal">
          <h3>Como funciona</h3>
          <p>Você preenche o formulário, a gente guarda seu contato e o material que enviar. Quando abrimos uma posição compatível, entramos em contato pelo e-mail ou telefone informados.</p>

          <h3>O que ajuda a se destacar</h3>
          <p>Portfólio ou perfil com trabalhos reais, mesmo que de projetos pessoais. Para social media e design, ver o que você já produziu vale mais do que uma lista de ferramentas.</p>

          <h3>Prefere mandar por e-mail?</h3>
          <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>

          <h3>Onde ficamos</h3>
          <p>{SITE['address_line1']}<br>{SITE['address_line2']}</p>
        </div>
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
    build_contato()
    build_trabalhe_conosco()


if __name__ == "__main__":
    main()
