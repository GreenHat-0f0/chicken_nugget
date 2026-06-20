# Desafio do Desafio
# No laboratório o problema volta todo dia: sentou na máquina, abriu o VS Code, foi dar commit — e o Git
# ainda está com o colega anterior.
# Crie um segundo arquivo, na raiz do seu repositório no GitHub (mesmo nível de pastas como src/ ou
# README.md), com um nome pessoal e fácil de lembrar. Exemplo: sou_ignacio.py (use o seu nome).
# Esse script é o ritual de início de trabalho: toda vez que for programar naquele PC, rode-o antes de codar
# ou commitar. Ele deve configurar automaticamente o user.name e o user.email corretos para você — sem
# perguntar, com seus dados já definidos no código.

import subprocess

subprocess.run(["git", "config", "--global", "user.name", f'"{un}"'])
subprocess.run(["git", "config", "--global", "user.email", f'"{ue}"'])

print("Executado com sucesso")
print()
print("Seu usuário é:") 
subprocess.run(["git", "config", "user.name"])
print()
print("Seu email é:")
subprocess.run(["git", "config", "user.email"])