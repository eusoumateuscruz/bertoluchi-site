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
  var publisBox = document.querySelector("[data-area-publis]");
  var publisLista = document.querySelector("[data-publis-lista]");
  var publisResumo = document.querySelector("[data-publis-resumo]");
  var publisCal = document.querySelector("[data-publis-cal]");
  var MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
  var publisTodas = [];
  var anoSel = null;
  var mesSel = null;
  var carregando = document.querySelector("[data-area-carregando]");
  var linksBox = document.querySelector("[data-area-links]");
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

  function dataBr(ms) {
    if (!ms) return "";
    return new Date(ms).toLocaleDateString("pt-BR", { timeZone: "America/Sao_Paulo" });
  }

  function cartaoPubli(p) {
    var st = status(p);
    var meta = [["Data", dataBr(p.data)], ["Prazo", dataBr(p.prazo)]]
      .filter(function (m) { return m[1]; })
      .map(function (m) { return "<div><dt>" + m[0] + "</dt><dd>" + esc(m[1]) + "</dd></div>"; }).join("");
    return '<article class="area-op">' +
      '<div class="area-op-topo"><span class="area-op-marca">Publi</span>' +
      '<span class="area-status area-status--' + st.replace(/\s+/g, "-") + '">' + esc(st) + "</span></div>" +
      "<h3>" + esc(p.marca) + "</h3>" +
      (meta ? '<dl class="area-op-meta">' + meta + "</dl>" : "") + "</article>";
  }

  // publis vêm do ClickUp da Bertoluchi; null = sincronização indisponível
  function renderPublis(publis) {
    if (!publis) { publisBox.hidden = true; return; }
    publisBox.hidden = false;
    publisTodas = publis;
    escolherPeriodo();
    desenharPublis();
  }

  // abre no mês atual; sem publi nele, no mês mais recente que tiver alguma
  function escolherPeriodo() {
    var hoje = new Date();
    var ano = hoje.getFullYear();
    var mes = hoje.getMonth() + 1;
    var temAgora = publisTodas.some(function (p) { return p.ano === ano && p.mes === mes; });
    if (temAgora || !publisTodas.length) { anoSel = ano; mesSel = mes; return; }
    var recente = publisTodas.filter(function (p) { return p.ano && p.mes; }).sort(function (x, y) {
      return (y.ano - x.ano) || (y.mes - x.mes);
    })[0];
    if (recente) { anoSel = recente.ano; mesSel = recente.mes; return; }
    anoSel = (publisTodas[0] && publisTodas[0].ano) || ano;
    mesSel = 0;
  }

  function desenharPublis() {
    var doAno = publisTodas.filter(function (p) { return p.ano === anoSel; });
    var cont = { aberta: 0, "em andamento": 0, encerrada: 0 };
    doAno.forEach(function (p) { if (cont[status(p)] != null) cont[status(p)]++; });
    publisResumo.innerHTML = [
      [doAno.length, (doAno.length === 1 ? "publi em " : "publis em ") + anoSel], [cont.aberta, "a fazer"],
      [cont["em andamento"], "em andamento"], [cont.encerrada, "concluídas"]
    ].map(function (r) { return '<div class="area-num"><strong>' + r[0] + "</strong><span>" + r[1] + "</span></div>"; }).join("");

    var anos = publisTodas.map(function (p) { return p.ano; }).filter(Boolean);
    if (anos.indexOf(anoSel) < 0) anos.push(anoSel);
    anos = anos.filter(function (a, i) { return anos.indexOf(a) === i; }).sort();
    var i = anos.indexOf(anoSel);
    var chips = MESES.map(function (nome, n) {
      var qtd = doAno.filter(function (p) { return p.mes === n + 1; }).length;
      return '<button type="button" class="area-cal-mes' + (qtd ? "" : " is-vazio") + (mesSel === n + 1 ? " is-ativo" : "") +
        '" data-cal-mes="' + (n + 1) + '" aria-pressed="' + (mesSel === n + 1) + '" aria-label="' + nome + ", " + qtd + (qtd === 1 ? " publi" : " publis") + '">' +
        "<span>" + nome.slice(0, 3) + "</span><b>" + (qtd || "·") + "</b></button>";
    }).join("");
    var semMes = doAno.filter(function (p) { return !p.mes; }).length;
    if (semMes) {
      chips += '<button type="button" class="area-cal-mes' + (mesSel === 0 ? " is-ativo" : "") + '" data-cal-mes="0" aria-pressed="' + (mesSel === 0) + '"><span>Outras</span><b>' + semMes + "</b></button>";
    }
    publisCal.innerHTML = '<div class="area-cal-ano">' +
      '<button type="button" data-cal-ano="-1" aria-label="Ano anterior"' + (i <= 0 ? " disabled" : "") + ">&lsaquo;</button>" +
      "<strong>" + anoSel + "</strong>" +
      '<button type="button" data-cal-ano="1" aria-label="Próximo ano"' + (i >= anos.length - 1 ? " disabled" : "") + ">&rsaquo;</button></div>" +
      '<div class="area-cal-meses">' + chips + "</div>" +
      '<h3 class="area-cal-titulo">' + (mesSel ? MESES[mesSel - 1] + " de " + anoSel : "Outras publis de " + anoSel) + "</h3>";

    var ordem = { aberta: 0, "em andamento": 1, encerrada: 2 };
    var doMes = doAno.filter(function (p) { return mesSel ? p.mes === mesSel : !p.mes; }).sort(function (x, y) {
      return (ordem[status(x)] - ordem[status(y)]) || ((x.prazo || Infinity) - (y.prazo || Infinity));
    });
    publisLista.innerHTML = doMes.length ? doMes.map(cartaoPubli).join("") :
      '<p class="note-block">' + (publisTodas.length ? "Nenhuma publi neste mês." :
        "Ainda não há publis no seu cadastro. Assim que a equipe registrar uma, ela aparece aqui.") + "</p>";
    var ativo = publisCal.querySelector(".is-ativo");
    var faixa = publisCal.querySelector(".area-cal-meses");
    if (ativo && faixa && faixa.scrollWidth > faixa.clientWidth) faixa.scrollLeft = ativo.offsetLeft - faixa.offsetLeft - faixa.clientWidth / 2 + ativo.clientWidth / 2;
  }

  publisCal.addEventListener("click", function (e) {
    var alvo = e.target.closest ? e.target.closest("button") : null;
    if (!alvo || alvo.disabled) return;
    if (alvo.hasAttribute("data-cal-mes")) {
      mesSel = Number(alvo.getAttribute("data-cal-mes"));
    } else if (alvo.hasAttribute("data-cal-ano")) {
      var anos = publisTodas.map(function (p) { return p.ano; }).filter(Boolean);
      anos = anos.filter(function (a, i) { return anos.indexOf(a) === i; }).sort();
      var novo = anos[anos.indexOf(anoSel) + Number(alvo.getAttribute("data-cal-ano"))];
      if (!novo) return;
      anoSel = novo;
      var meses = publisTodas.filter(function (p) { return p.ano === novo && p.mes; }).map(function (p) { return p.mes; });
      mesSel = meses.length ? Math.max.apply(null, meses) : 0;
    }
    desenharPublis();
  });

  function renderLinks(links) {
    links = links || {};
    var lista = [["Meu Instagram", links.instagram], ["Minha pasta no Drive", links.drive], ["Meu mídia kit", links.midiakit]]
      .filter(function (l) { return /^https:\/\//i.test(l[1] || ""); });
    linksBox.hidden = !lista.length;
    linksBox.innerHTML = lista.map(function (l) {
      return '<a class="area-link" href="' + esc(l[1]) + '" target="_blank" rel="noopener">' + esc(l[0]) + "</a>";
    }).join("");
  }

  function abrirPainel(json) {
    dados = json.oportunidades || [];
    ola.textContent = "Olá, " + (json.nome || "tudo bem") + "!";
    raiz.hidden = true;
    painel.hidden = false;
    render();
    renderLinks(json.links);
    renderPublis(json.publis);
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

  // Ao abrir a página, o aviso de carregamento fica no lugar do login: quem já
  // está conectado não vê o formulário enquanto os dados chegam. Sem sessão, a
  // resposta é imediata e o login aparece. Se demorar demais, o login aparece
  // assim mesmo, e o painel toma o lugar dele se os dados chegarem depois.
  function iniciar() {
    raiz.hidden = true;
    carregando.hidden = false;
    var limite = setTimeout(function () {
      carregando.hidden = true;
      if (painel.hidden) raiz.hidden = false;
    }, 15000);
    carregar().then(function (json) {
      clearTimeout(limite);
      carregando.hidden = true;
      if (!json) raiz.hidden = false;
    });
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

  iniciar();
})();
