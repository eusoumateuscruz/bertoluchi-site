(function () {
  "use strict";

  // Ano dinâmico no rodapé
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Menu mobile
  var toggle = document.querySelector("[data-menu-toggle]");
  var menu = document.querySelector("[data-mobile-menu]");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var isOpen = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
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

})();
