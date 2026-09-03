# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from common import SITE, NAV, SERVICES, INFLUENCERS, TESTIMONIALS, CASES, head, header, footer

DIST = os.path.join(os.path.dirname(__file__), "..", "dist")


def write(path, html):
    full = os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
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
        <div class="pillar-card">
          <span class="pillar-index">0{i}</span>
          <h3>{s['title']}</h3>
          <p>{s['short']}</p>
          <a class="pillar-link" href="/servicos/{s['slug']}.html">Saiba mais →</a>
        </div>"""

    influencer_preview = ""
    for inf in INFLUENCERS[:4]:
        influencer_preview += f"""
        <a class="influencer-card" href="https://www.instagram.com/{inf['handle'][1:]}/" target="_blank" rel="noopener">
          <img src="{inf['img']}" alt="{inf['name']}" loading="lazy">
          <div class="influencer-overlay"><strong>{inf['name']}</strong><span>{inf['handle']}</span></div>
        </a>"""

    testimonial_preview = ""
    for t in TESTIMONIALS[:3]:
        testimonial_preview += f"""
        <div class="testimonial-card">
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
      <div class="section-head center">
        <span class="eyebrow">O que fazemos</span>
        <h2>Três frentes, um único objetivo: sua marca em evidência</h2>
        <p>Da negociação da parceria certa até o post que sai no ar, cuidamos de cada etapa da sua presença digital.</p>
      </div>
      <div class="pillars-grid">{pillars}</div>
    </div>
  </section>

  <section class="section section-dark">
    <div class="container">
      <div class="section-head center" style="max-width:640px">
        <span class="eyebrow" style="color:#F4D9C4;-webkit-text-fill-color:#F4D9C4">Nossa essência</span>
        <h2>Ética, compromisso e honestidade em cada entrega</h2>
        <p>Nossa missão é impulsionar empresas no ramo digital, conectando marcas e influenciadoras de forma estratégica, sem perder o cuidado humano em cada parceria.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head" style="display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:16px;max-width:none">
        <div>
          <span class="eyebrow">Talentos</span>
          <h2 style="margin-bottom:0">Influenciadoras que assessoramos</h2>
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
      <div class="section-head center">
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
      <div class="section-head">
        <span class="eyebrow">Sobre a Bertoluchi</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Uma agência nascida dentro da própria criação de conteúdo</h1>
      </div>

      <div class="bio-split">
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
      <div class="section-head center">
        <span class="eyebrow">O que nos move</span>
        <h2>Missão, visão e valores</h2>
      </div>
      <div class="values-grid">
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
        <div class="service-row">
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
      <div class="section-head">
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
      <div class="service-body">
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
      <div class="section-head" style="max-width:none">
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
    cards = ""
    for inf in INFLUENCERS:
        cards += f"""
        <a class="influencer-card" href="https://www.instagram.com/{inf['handle'][1:]}/" target="_blank" rel="noopener">
          <img src="{inf['img']}" alt="{inf['name']}" loading="lazy">
          <div class="influencer-overlay"><strong>{inf['name']}</strong><span>{inf['handle']}</span></div>
        </a>"""

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
      <div class="section-head">
        <span class="eyebrow">Influenciadoras</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Talentos que assessoramos</h1>
        <p>Cada uma com um nicho, um público e uma forma própria de se conectar. A gente cuida da parte comercial para que elas continuem focadas em criar.</p>
      </div>
      <div class="influencer-grid mt-lg">{cards}</div>
      <p class="note-block">As fotos acima ainda são as do acervo atual da agência. Assim que o novo material fotográfico for enviado, esta seção é atualizada.</p>
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
        <div class="case-card">
          <span class="eyebrow">{c['tag']}</span>
          <h3>{c['name']}</h3>
          <p>{c['text']}</p>
        </div>"""

    testimonial_full = ""
    for t in TESTIMONIALS:
        testimonial_full += f"""
        <div class="testimonial-card">
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
      <div class="section-head">
        <span class="eyebrow">Resultados</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Cases e depoimentos</h1>
        <p>Estamos organizando cases com números completos de cada cliente. Por enquanto, veja o projeto social que apoiamos e o que dizem sobre a gente.</p>
      </div>
      {cases_html}
      <p class="note-block">Métricas de resultado (engajamento, crescimento de seguidores, conversão) serão adicionadas aqui assim que autorizadas por cada cliente. Nenhum número é publicado sem confirmação.</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center">
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
      <div class="section-head">
        <span class="eyebrow">Blog</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Conteúdo sobre marketing digital e redes sociais</h1>
      </div>
      <div class="blog-empty mt-lg">
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
      <div class="section-head">
        <span class="eyebrow">Contato</span>
        <h1 style="font-size:clamp(2rem,4vw,2.8rem)">Vamos conversar</h1>
        <p>Preencha o formulário e nossa equipe retorna assim que possível. Se preferir, fale direto pelo WhatsApp.</p>
      </div>

      <div class="contact-grid mt-lg">
        <form class="contact-form" action="#" method="post">
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

        <div class="contact-info">
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


def main():
    build_home()
    build_sobre()
    build_servicos_hub()
    for s in SERVICES:
        build_service_detail(s)
    build_influenciadoras()
    build_resultados()
    build_blog()
    build_contato()


if __name__ == "__main__":
    main()
