const { lerConfig, conferirSenha, criarSessao, semCache } = require("./_area");

module.exports = async (req, res) => {
  semCache(res);
  if (req.method !== "POST") return res.status(405).json({ erro: "Método não permitido" });
  const { usuario, senha, lembrar } = req.body || {};
  const login = String(usuario || "").trim().toLowerCase().replace(/^@/, "");
  if (!login || !senha) return res.status(400).json({ erro: "Preencha usuário e senha." });
  try {
    const contas = (await lerConfig("influenciadoras")) || {};
    const conta = Object.prototype.hasOwnProperty.call(contas, login) ? contas[login] : null;
    if (!conta || conta.ativo === false || !conferirSenha(senha, conta)) {
      // atraso fixo para encarecer tentativa por força bruta
      await new Promise((r) => setTimeout(r, 600));
      return res.status(401).json({ erro: "Usuário ou senha incorretos." });
    }
    criarSessao(res, login, lembrar !== false);
    return res.status(200).json({ ok: true, nome: conta.nome || login });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ erro: "Não foi possível entrar agora. Tente de novo em instantes." });
  }
};
