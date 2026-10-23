(function () {
  var raiz = document.querySelector("[data-area]");
  if (!raiz) return;
  var form = document.querySelector("[data-area-login]");
  var erro = document.querySelector("[data-area-erro]");
  var painel = document.querySelector("[data-area-painel]");
  var lista = document.querySelector("[data-area-lista]");
  var resumo = document.querySelector("[data-area-resumo]");
  var ola = document.querySelector("[data-area-ola]");
  var WHATS = "https://wa.me/5547992545015?text=";
  var dados = [];
  var filtro = "todas";

  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function mostrarErro(msg) {
    erro.textContent = msg;
    erro.hidden = !msg;
  }

  function status(o) { return (o.status || "aberta").toLowerCase(); }

  function cartao(o) {
    var st = status(o);
    var meta = [["Formato", o.formato], ["Cachê", o.cache], ["Prazo", o.prazo], ["Cidade", o.cidade]]
      .filter(function (m) { return m[1]; })
      .map(function (m) { return "<div><dt>" + m[0] + "</dt><dd>" + esc(m[1]) + "</dd></div>"; }).join("");
    var msg = "Olá! Vi na área da influenciadora a oportunidade " + (o.marca ? o.marca + " - " : "") + (o.titulo || "") + " e quero conversar.";
    var acao = st === "encerrada" ? "" :
      '<a class="btn btn-primary" href="' + WHATS + encodeURIComponent(msg) + '" target="_blank" rel="noopener">Tenho interesse</a>';
    return '<article class="area-op">' +
      '<div class="area-op-topo"><span class="area-op-marca">' + esc(o.marca || "Bertoluchi") + "</span>" +
      '<span class="area-status area-status--' + st.replace(/\s+/g, "-") + '">' + esc(st) + "</span></div>" +
      "<h3>" + esc(o.titulo) + "</h3>" +
      (o.descricao ? "<p>" + esc(o.descricao) + "</p>" : "") +
      (meta ? '<dl class="area-op-meta">' + meta + "</dl>" : "") +
      acao + "</article>";
  }

  function render() {
    var cont = { aberta: 0, "em andamento": 0, encerrada: 0 };
    dados.forEach(function (o) { if (cont[status(o)] != null) cont[status(o)]++; });
    resumo.innerHTML = [
      [dados.length, "oportunidades"], [cont.aberta, "abertas"],
      [cont["em andamento"], "em andamento"], [cont.encerrada, "encerradas"]
    ].map(function (r) { return '<div class="area-num"><strong>' + r[0] + "</strong><span>" + r[1] + "</span></div>"; }).join("");
    var visiveis = dados.filter(function (o) { return filtro === "todas" || status(o) === filtro; });
    lista.innerHTML = visiveis.length ? visiveis.map(cartao).join("") :
      '<p class="note-block">' + (dados.length ? "Nenhuma oportunidade neste filtro." :
        "Ainda não há oportunidades para você. Assim que a Bertoluchi fechar uma nova proposta, ela aparece aqui.") + "</p>";
  }

  function abrirPainel(json) {
    dados = json.oportunidades || [];
    ola.textContent = "Olá, " + (json.nome || "tudo bem") + "!";
    raiz.hidden = true;
    painel.hidden = false;
    render();
  }

  function carregar() {
    return fetch("/api/oportunidades", { credentials: "same-origin" }).then(function (r) {
      if (!r.ok) return null;
      return r.json();
    }).then(function (json) {
      if (json) abrirPainel(json);
      return json;
    }).catch(function () { return null; });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    mostrarErro("");
    var botao = form.querySelector('button[type="submit"]');
    var usuario = form.usuario.value.trim();
    var senha = form.senha.value;
    if (!usuario || !senha) { mostrarErro("Preencha usuário e senha."); return; }
    botao.disabled = true; botao.textContent = "Entrando...";
    fetch("/api/entrar", {
      method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ usuario: usuario, senha: senha, lembrar: form.lembrar.checked })
    }).then(function (r) {
      return r.json().then(function (j) { return { ok: r.ok, j: j }; });
    }).then(function (res) {
      if (!res.ok) throw new Error(res.j.erro || "Não foi possível entrar.");
      form.senha.value = "";
      return carregar();
    }).catch(function (err) {
      mostrarErro(err.message || "Não foi possível entrar.");
    }).then(function () {
      botao.disabled = false; botao.textContent = "Entrar";
    });
  });

  document.querySelector("[data-ver-senha]").addEventListener("click", function () {
    var campo = form.senha;
    var ver = campo.type === "password";
    campo.type = ver ? "text" : "password";
    this.textContent = ver ? "Ocultar" : "Mostrar";
    this.setAttribute("aria-label", ver ? "Ocultar senha" : "Mostrar senha");
  });

  document.querySelectorAll("[data-filtro]").forEach(function (b) {
    b.addEventListener("click", function () {
      filtro = b.getAttribute("data-filtro");
      document.querySelectorAll("[data-filtro]").forEach(function (x) { x.classList.toggle("is-ativo", x === b); });
      render();
    });
  });

  document.querySelector("[data-area-sair]").addEventListener("click", function () {
    fetch("/api/sair", { method: "POST", credentials: "same-origin" }).then(function () {
      painel.hidden = true;
      raiz.hidden = false;
      dados = [];
    });
  });

  carregar();
})();
