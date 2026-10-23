// Base da Área da Influenciadora: leitura do Global Config (Edge Config),
// conferência de senha e cookie de sessão assinado.
//
// O repositório é público, então nada sensível fica aqui: as contas e as
// oportunidades moram no Global Config da Vercel (variável EDGE_CONFIG) e a
// assinatura do cookie usa a variável SESSAO_SEGREDO.
//
// Global Config, item "influenciadoras":
//   { "usuario": { "nome": "...", "sal": "<hex>", "hash": "<hex>", "ativo": true } }
//   hash = scrypt(senha, sal, 32), gerado por _generator/senha_influenciadora.py
// Global Config, item "oportunidades":
//   [ { "id", "marca", "titulo", "descricao", "formato", "cache", "prazo",
//       "cidade", "status": "aberta" | "em andamento" | "encerrada",
//       "para": ["*"] ou ["usuario", ...] } ]
const crypto = require("crypto");

const COOKIE = "bt_inf";
// "Manter conectado": 90 dias, renovados a cada visita. Sem a opção, a sessão
// vale até fechar o navegador (e no máximo 12 horas).
const DURACAO_LONGA = 60 * 60 * 24 * 90;
const DURACAO_CURTA = 60 * 60 * 12;

async function lerConfig(chave) {
  const bruto = process.env.EDGE_CONFIG;
  if (!bruto) throw new Error("EDGE_CONFIG ausente");
  const url = new URL(bruto);
  const id = url.pathname.replace(/^\/+/, "");
  const token = url.searchParams.get("token");
  const r = await fetch(`https://edge-config.vercel.com/${id}/item/${chave}?token=${token}`);
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`Global Config ${r.status}`);
  return r.json();
}

function conferirSenha(senha, conta) {
  if (!conta || !conta.sal || !conta.hash) return false;
  const calc = crypto.scryptSync(String(senha), Buffer.from(conta.sal, "hex"), 32);
  const salvo = Buffer.from(conta.hash, "hex");
  return salvo.length === calc.length && crypto.timingSafeEqual(calc, salvo);
}

function assinar(texto) {
  return crypto.createHmac("sha256", process.env.SESSAO_SEGREDO || "").update(texto).digest("base64url");
}

function criarSessao(res, usuario, lembrar) {
  const duracao = lembrar ? DURACAO_LONGA : DURACAO_CURTA;
  const expira = Math.floor(Date.now() / 1000) + duracao;
  const corpo = `${Buffer.from(usuario).toString("base64url")}.${expira}.${lembrar ? 1 : 0}`;
  const validade = lembrar ? `; Max-Age=${duracao}` : "";
  res.setHeader("Set-Cookie",
    `${COOKIE}=${corpo}.${assinar(corpo)}; Path=/${validade}; HttpOnly; Secure; SameSite=Lax`);
}

function encerrarSessao(res) {
  res.setHeader("Set-Cookie", `${COOKIE}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`);
}

function lerSessao(req) {
  if (!process.env.SESSAO_SEGREDO) return null;
  const linha = req.headers.cookie || "";
  const par = linha.split(/;\s*/).find((c) => c.startsWith(COOKIE + "="));
  if (!par) return null;
  const [u, expira, lembrar, sig] = par.slice(COOKIE.length + 1).split(".");
  if (!u || !expira || !lembrar || !sig) return null;
  const esperado = Buffer.from(assinar(`${u}.${expira}.${lembrar}`));
  const recebido = Buffer.from(sig);
  if (esperado.length !== recebido.length || !crypto.timingSafeEqual(esperado, recebido)) return null;
  if (Number(expira) < Date.now() / 1000) return null;
  return { usuario: Buffer.from(u, "base64url").toString(), lembrar: lembrar === "1" };
}

function semCache(res) {
  res.setHeader("Cache-Control", "no-store");
}

module.exports = { lerConfig, conferirSenha, criarSessao, encerrarSessao, lerSessao, semCache };
