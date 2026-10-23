# -*- coding: utf-8 -*-
"""Gera a entrada de uma influenciadora para o item "influenciadoras" do
Global Config da Vercel (a senha nunca vai para o repositorio).

Uso: python _generator/senha_influenciadora.py usuario "Nome Exibido" [senha]
Sem senha, gera uma aleatoria. Imprime o JSON da conta e a senha para enviar.
"""
import hashlib
import json
import os
import secrets
import sys


def gerar(usuario, nome, senha=None):
    senha = senha or secrets.token_urlsafe(9)
    sal = os.urandom(16)
    h = hashlib.scrypt(senha.encode(), salt=sal, n=16384, r=8, p=1, dklen=32)
    conta = {"nome": nome, "sal": sal.hex(), "hash": h.hex(), "ativo": True}
    return usuario.strip().lower().lstrip("@"), conta, senha


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    u, conta, senha = gerar(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    print(json.dumps({u: conta}, ensure_ascii=False))
    print("senha:", senha)
