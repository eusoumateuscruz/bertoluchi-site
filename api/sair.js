const { encerrarSessao, semCache } = require("./_area");

module.exports = async (req, res) => {
  semCache(res);
  encerrarSessao(res);
  return res.status(200).json({ ok: true });
};
