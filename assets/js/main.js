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

})();
