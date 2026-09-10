(function () {
  "use strict";

  // Ano dinâmico no rodapé
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Menu mobile: drawer lateral (hamburguer, X, scrim e Esc)
  var toggles = document.querySelectorAll("[data-menu-toggle]");
  var menu = document.querySelector("[data-mobile-menu]");
  var scrim = document.querySelector("[data-menu-scrim]");
  var hamburger = document.querySelector(".menu-toggle");

  function setMenu(isOpen) {
    menu.classList.toggle("is-open", isOpen);
    if (scrim) scrim.classList.toggle("is-open", isOpen);
    menu.setAttribute("aria-hidden", isOpen ? "false" : "true");
    if (hamburger) hamburger.setAttribute("aria-expanded", isOpen ? "true" : "false");
    document.body.style.overflow = isOpen ? "hidden" : "";
  }

  if (menu && toggles.length) {
    toggles.forEach(function (btn) {
      btn.addEventListener("click", function () {
        setMenu(!menu.classList.contains("is-open"));
      });
    });
    if (scrim) {
      scrim.addEventListener("click", function () { setMenu(false); });
    }
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () { setMenu(false); });
    });
  }

  // Header: transparente no topo, vidro fosco ao rolar
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 12);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Reveal on scroll, respeitando prefers-reduced-motion
  var alvos = document.querySelectorAll(".reveal");
  var semMovimento =
    window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!alvos.length) {
    // nada a fazer
  } else if (semMovimento || !("IntersectionObserver" in window)) {
    // sem animacao: mostra tudo de uma vez
    alvos.forEach(function (el) {
      el.classList.add("is-visible");
    });
  } else {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.08 }
    );
    alvos.forEach(function (el) {
      observer.observe(el);
    });

    // Rede de seguranca: num salto rapido de rolagem (ancora, fim da pagina)
    // um elemento pode nunca chegar a intersectar e ficaria invisivel para
    // sempre. Observado no WebKit. A varredura garante que tudo que ja passou
    // pela dobra aparece, sem depender do observer.
    var varrendo = false;
    var varrer = function () {
      alvos.forEach(function (el) {
        if (el.classList.contains("is-visible")) return;
        if (el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("is-visible");
          observer.unobserve(el);
        }
      });
    };
    window.addEventListener("scroll", function () {
      if (varrendo) return;
      varrendo = true;
      requestAnimationFrame(function () { varrer(); varrendo = false; });
    }, { passive: true });
    window.addEventListener("load", varrer);
  }


  // Filtro de categoria do blog
  var grade = document.querySelector("[data-post-grid]");
  if (grade) {
    var chips = document.querySelectorAll("[data-filtro]");
    var cards = grade.querySelectorAll("[data-categoria]");
    var vazio = document.querySelector("[data-filtro-vazio]");

    var aplicar = function (alvo) {
      var visiveis = 0;
      cards.forEach(function (card) {
        var mostra = alvo === "todos" || card.dataset.categoria === alvo;
        card.hidden = !mostra;
        if (mostra) visiveis++;
      });
      chips.forEach(function (chip) {
        chip.classList.toggle("is-active", chip.dataset.filtro === alvo);
        chip.setAttribute("aria-pressed", chip.dataset.filtro === alvo ? "true" : "false");
      });
      if (vazio) vazio.hidden = visiveis > 0;
    };

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var alvo = chip.dataset.filtro;
        aplicar(alvo);
        history.replaceState(null, "", alvo === "todos" ? location.pathname : "#" + alvo);
      });
    });

    // permite chegar filtrado por link, ex.: /blog.html#branding
    var doHash = function () {
      var alvo = location.hash.replace("#", "");
      var existe = Array.prototype.some.call(chips, function (c) {
        return c.dataset.filtro === alvo;
      });
      if (existe) aplicar(alvo);
    };
    doHash();
    window.addEventListener("hashchange", doHash);
  }


  // ---------------------------------------------------------------
  // Coverflow: carrossel 3D da secao Talentos
  // ---------------------------------------------------------------
  function initCoverflow(root) {
    var frame = root.querySelector(".coverflow-frame");
    var cards = Array.prototype.slice.call(root.querySelectorAll(".coverflow-card"));
    var caption = root.querySelector(".coverflow-caption");
    var dotsBox = root.querySelector(".coverflow-dots");
    var btnPrev = root.querySelector(".coverflow-prev");
    var btnNext = root.querySelector(".coverflow-next");
    if (!frame || !cards.length) return;

    var semMovimento =
      window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var index = Math.floor(cards.length / 2);
    var pos = index;      // posicao continua, permite arraste fracionado
    var alvo = index;
    var raf = null;
    var larguraCard = 0;

    var dots = cards.map(function (card, i) {
      var d = document.createElement("button");
      d.type = "button";
      d.className = "coverflow-dot";
      d.setAttribute("aria-label", "Ver " + (card.dataset.title || "item " + (i + 1)));
      d.addEventListener("click", function () { irPara(i); });
      dotsBox.appendChild(d);
      return d;
    });

    function medir() {
      // offsetWidth e a largura de layout: getBoundingClientRect() traria a
      // largura JA transformada (escala/rotacao), e o ResizeObserver dispara
      // depois de pintar, colapsando o leque a cada remedicao.
      larguraCard = cards[0].offsetWidth || 200;
    }

    function pintar() {
      for (var i = 0; i < cards.length; i++) {
        var d = i - pos;
        var abs = Math.abs(d);
        var limitado = Math.max(-3, Math.min(3, d));
        var x = limitado * larguraCard * 0.56;
        var z = -Math.min(abs, 3) * larguraCard * 0.32;
        var giro = -limitado * 38;
        var escala = 1 - Math.min(abs, 3) * 0.1;
        var opacidade = abs > 3.2 ? 0 : 1 - Math.min(abs, 3) * 0.22;
        var c = cards[i];
        c.style.transform =
          "translate(-50%,0) translate3d(" + x + "px,0," + z + "px) rotateY(" + giro + "deg) scale(" + escala + ")";
        c.style.opacity = opacidade;
        c.style.zIndex = String(100 - Math.round(abs * 10));
        c.style.visibility = opacidade <= 0.02 ? "hidden" : "visible";
      }
    }

    function atualizarLegenda() {
      var c = cards[index];
      caption.innerHTML =
        "<strong>" + (c.dataset.title || "") + "</strong>" +
        "<span>" + (c.dataset.subtitle || "") + "</span>";
      dots.forEach(function (d, i) { d.classList.toggle("is-active", i === index); });
    }

    function passo() {
      var delta = alvo - pos;
      if (Math.abs(delta) < 0.002) {
        pos = alvo;
        pintar();
        raf = null;
        return;
      }
      pos += delta * 0.16;
      pintar();
      raf = requestAnimationFrame(passo);
    }

    function assentar() {
      if (semMovimento) { pos = alvo; pintar(); return; }
      if (!raf) raf = requestAnimationFrame(passo);
    }

    function irPara(i) {
      index = Math.max(0, Math.min(cards.length - 1, i));
      alvo = index;
      atualizarLegenda();
      assentar();
    }

    // arraste com inercia
    var arrastando = false, xInicial = 0, posInicial = 0;
    var xUltimo = 0, tUltimo = 0, velocidade = 0, percorrido = 0;

    frame.addEventListener("pointerdown", function (e) {
      // as setas ficam dentro do frame: sem esse guard, o setPointerCapture
      // abaixo sequestra o ponteiro e o clique nunca chega ao botao
      if (e.target && e.target.closest && e.target.closest(".coverflow-nav")) return;
      arrastando = true;
      xInicial = xUltimo = e.clientX;
      posInicial = pos;
      tUltimo = Date.now();
      velocidade = 0;
      percorrido = 0;
      if (raf) { cancelAnimationFrame(raf); raf = null; }
      try { frame.setPointerCapture(e.pointerId); } catch (err) {}
    });

    frame.addEventListener("pointermove", function (e) {
      if (!arrastando) return;
      var dx = e.clientX - xInicial;
      percorrido = Math.abs(dx);
      pos = posInicial - dx / (larguraCard * 0.56);
      pos = Math.max(-0.6, Math.min(cards.length - 0.4, pos));
      var agora = Date.now();
      if (agora > tUltimo) {
        velocidade = (e.clientX - xUltimo) / (agora - tUltimo);
        xUltimo = e.clientX;
        tUltimo = agora;
      }
      pintar();
    });

    function soltar(e) {
      if (!arrastando) return;
      arrastando = false;
      try { frame.releasePointerCapture(e.pointerId); } catch (err) {}
      if (percorrido < 6) {
        // toque curto: centraliza o card clicado, se houver
        var alvoCard = e.target && e.target.closest ? e.target.closest(".coverflow-card") : null;
        if (alvoCard) { irPara(cards.indexOf(alvoCard)); return; }
      }
      var inercia = -velocidade * 2.2;
      inercia = Math.max(-2, Math.min(2, inercia));
      irPara(Math.round(pos + inercia));
    }
    frame.addEventListener("pointerup", soltar);
    frame.addEventListener("pointercancel", soltar);

    if (btnPrev) btnPrev.addEventListener("click", function () { irPara(index - 1); });
    if (btnNext) btnNext.addEventListener("click", function () { irPara(index + 1); });

    frame.setAttribute("tabindex", "0");
    frame.setAttribute("role", "group");
    frame.setAttribute("aria-label", "Influenciadoras assessoradas, use as setas do teclado");
    frame.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { irPara(index - 1); e.preventDefault(); }
      if (e.key === "ArrowRight") { irPara(index + 1); e.preventDefault(); }
    });

    if (window.ResizeObserver) {
      new ResizeObserver(function () { medir(); pintar(); }).observe(frame);
    } else {
      window.addEventListener("resize", function () { medir(); pintar(); });
    }

    medir();
    pintar();
    atualizarLegenda();
  }

  document.querySelectorAll("[data-coverflow]").forEach(initCoverflow);

})();
