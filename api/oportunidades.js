const { lerConfig, lerSessao, criarSessao, semCache } = require("./_area");
const { publisDe } = require("./_clickup");

module.exports = async (req, res) => {
  semCache(res);
  const sessao = lerSessao(req);
  if (!sessao) return res.status(401).json({ erro: "Sessão expirada. Entre de novo." });
  try {
    const [contas, todas] = await Promise.all([lerConfig("influenciadoras"), lerConfig("oportunidades")]);
    const { usuario } = sessao;
    const conta = (contas || {})[usuario];
    if (!conta || conta.ativo === false) return res.status(401).json({ erro: "Acesso desativado." });
    const minhas = (todas || []).filter((o) => {
      const para = o.para || ["*"];
      return para.includes("*") || para.includes(usuario);
    });
    // falha no ClickUp não derruba o portal: as oportunidades seguem aparecendo
    let publis = null;
    try {
      publis = await publisDe(usuario, conta);
    } catch (e) {
      console.error(e);
    }
    // quem marcou "Manter conectado" ganha mais 90 dias a cada visita
    if (sessao.lembrar) criarSessao(res, usuario, true);
    return res.status(200).json({ nome: conta.nome || usuario, oportunidades: minhas, publis });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ erro: "Não foi possível carregar as oportunidades." });
  }
};
