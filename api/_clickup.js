// Publis de cada influenciadora, lidas do ClickUp da Bertoluchi.
//
// No ClickUp, a lista "Influenciadoras" tem um cartão por influenciadora
// ("[INFLUENCIADORA] - Nome"). Dentro dele há a subtarefa "PUBLICIDADES 2026",
// que tem um cartão por mês ("OUTUBRO"), e cada publi é uma subtarefa do mês
// (o Sistema Bertoluchi grava assim: "Publicidade - [marca] : 📌"). Publi que
// esteja direto em PUBLICIDADES, sem mês, também conta. Só os cartões com status "Influ Ativas"
// entram no portal, e só nome, status, data e prazo de cada publi saem daqui:
// contrato, precificação e dados bancários nunca são lidos.
//
// O token fica na variável CLICKUP_TOKEN da Vercel. A conta do portal se liga
// ao cartão pelo campo "clickup" (id da tarefa) no Global Config ou, sem ele,
// pelo nome ou pelo @ que aparecem no título do cartão.
const LISTA = "901306280507";
const STATUS_ATIVO = "influ ativas";
const CACHE_MS = 60 * 1000;
const MESES = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho",
  "agosto", "setembro", "outubro", "novembro", "dezembro"];

let cacheCartoes = { quando: 0, dados: null };

async function api(caminho) {
  const r = await fetch("https://api.clickup.com/api/v2" + caminho, {
    headers: { Authorization: process.env.CLICKUP_TOKEN },
  });
  if (!r.ok) throw new Error(`ClickUp ${r.status} em ${caminho}`);
  return r.json();
}

function normalizar(t) {
  return String(t || "").normalize("NFD").replace(/[̀-ͯ]/g, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

// cartões da lista, sem subtarefas; guardados por 1 minuto para não estourar
// o limite de 100 chamadas por minuto do ClickUp
async function cartoes() {
  if (cacheCartoes.dados && Date.now() - cacheCartoes.quando < CACHE_MS) return cacheCartoes.dados;
  const todos = [];
  for (let pagina = 0; pagina < 10; pagina++) {
    const j = await api(`/list/${LISTA}/task?include_closed=true&page=${pagina}`);
    todos.push(...(j.tasks || []));
    if (j.last_page !== false) break;
  }
  cacheCartoes = { quando: Date.now(), dados: todos };
  return todos;
}

function acharCartao(lista, usuario, conta) {
  if (conta.clickup) return lista.find((t) => t.id === conta.clickup) || null;
  const chaves = [conta.nome, usuario, conta.slug].map(normalizar).filter(Boolean);
  return lista.find((t) => {
    const titulo = " " + normalizar(t.name.replace(/^\s*\[[^\]]*\]\s*-?\s*/, "")) + " ";
    const compacto = titulo.replace(/ /g, "");
    return chaves.some((c) => titulo.includes(" " + c + " ") || compacto.includes(c.replace(/ /g, "")));
  }) || null;
}

// "Publicidade - [Marca] :  📌 " vira "Marca"; outro formato fica como está
function nomeDaMarca(nome) {
  const m = String(nome || "").match(/^\s*publicidade\s*-\s*\[([^\]]+)\]/i);
  return (m ? m[1] : String(nome || "")).trim();
}

function grupo(status) {
  const tipo = (status && status.type) || "";
  if (tipo === "closed" || tipo === "done") return "encerrada";
  if (tipo === "open") return "aberta";
  return "em andamento";
}

async function publisDe(usuario, conta) {
  if (!process.env.CLICKUP_TOKEN) return null;
  const cartao = acharCartao(await cartoes(), usuario, conta);
  if (!cartao || normalizar(cartao.status && cartao.status.status) !== STATUS_ATIVO) return [];
  const completo = await api(`/task/${cartao.id}?include_subtasks=true`);
  const pastas = (completo.subtasks || []).filter((s) => /^\s*publicidades/i.test(s.name));
  const blocos = await Promise.all(pastas.map((p) => api(`/task/${p.id}?include_subtasks=true`)));
  const itens = blocos.flatMap((b) => b.subtasks || []);
  const ehMes = (t) => MESES.includes(normalizar(t.name));
  const meses = await Promise.all(itens.filter(ehMes).map((t) => api(`/task/${t.id}?include_subtasks=true`)));
  // cada mês traz um cartão-modelo ("MARCA", status "template") que não é publi
  const ehModelo = (t) => normalizar(t.status && t.status.status) === "template" || normalizar(t.name) === "marca";
  const publis = itens.filter((t) => !ehMes(t)).concat(meses.flatMap((m) => m.subtasks || [])).filter((t) => !ehModelo(t));
  return publis.map((s) => ({
    id: s.id,
    marca: nomeDaMarca(s.name),
    status: grupo(s.status),
    etapa: (s.status && s.status.status) || "",
    data: s.start_date ? Number(s.start_date) : null,
    prazo: s.due_date ? Number(s.due_date) : null,
  }));
}

module.exports = { publisDe };
