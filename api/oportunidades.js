const { lerConfig, lerSessao, semCache } = require("./_area");

module.exports = async (req, res) => {
  semCache(res);
  const usuario = lerSessao(req);
  if (!usuario) return res.status(401).json({ erro: "Sessão expirada. Entre de novo." });
  try {
    const [contas, todas] = await Promise.all([lerConfig("influenciadoras"), lerConfig("oportunidades")]);
    const conta = (contas || {})[usuario];
    if (!conta || conta.ativo === false) return res.status(401).json({ erro: "Acesso desativado." });
    const minhas = (todas || []).filter((o) => {
      const para = o.para || ["*"];
      return para.includes("*") || para.includes(usuario);
    });
    return res.status(200).json({ nome: conta.nome || usuario, oportunidades: minhas });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ erro: "Não foi possível carregar as oportunidades." });
  }
};
