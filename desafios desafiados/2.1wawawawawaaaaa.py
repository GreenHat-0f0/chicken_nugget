# Desafio 02 — Carteira de Identidade do Git

# No laboratório vocês usam o VS Code com GitHub. O computador é compartilhado: um aluno senta, outro
# senta depois. Às vezes o Git fica com o nome ou e-mail de outra pessoa — e o commit sai no histórico com
# o autor errado, sem ninguém perceber na hora.
# Isso acontece porque o Git guarda uma identidade local (user.name e user.email) no sistema. Não é a
# senha do GitHub: é só o rótulo que aparece em cada commit.
# Neste desafio você vai usar Python para rodar comandos de terminal, como se digitasse no console. O
# foco é aprender a executar um comando do sistema a partir do programa — não decorar Git, e sim ligar
# Python ao terminal.
# O exercício
# Crie um programa em Python chamado desafio02.py que:
# 1. Pede o nome e o e-mail que devem valer no Git;
# 2. Usa o módulo subprocess para executar os comandos git config ‐‐global e gravar esses dois valores;
# 3. Confirma no terminal que a configuração foi aplicada.
# O programa deve ser sequencial (sem funções). O Git precisa estar instalado na máquina.
# Comando no terminal
# No console, estes comandos definem sua identidade globalmente (vale em qualquer repositório neste usu-
# ário do sistema):
# git config ‐‐global user.name "Maria Silva"
# git config ‐‐global user.email "maria.silva@escola.ifsc.edu.br"
# Executar o mesmo comando em Python
# O módulo subprocess chama programas do sistema. Cada parte do comando vira um item na lista:
# import subprocess
# subprocess.run(["git", "config", "‐‐global", "user.name", "Maria Silva"])
# Monte o desafio02.py a partir disso: leia nome e e-mail com input(), execute os dois git config e avise
# quando terminar.
# Entrega: arquivo desafio02.py + captura de tela do terminal mostrando a execução.

import subprocess
un=(input("Digite seu nome de usuário do GitHub: "))
ue=(input("Digite seu email do GitHub: "))
subprocess.run(["git", "config", "--global", "user.name", f'"{un}"'])
subprocess.run(["git", "config", "--global", "user.email", f'"{ue}"'])

print("Executado com sucesso")
print()
print("Seu usuário é:") 
subprocess.run(["git", "config", "user.name"])
print()
print("Seu email é:")
subprocess.run(["git", "config", "user.email"])