# Orientações: Resolva os exercícios utilizando Python e apresente mensagens claras.
# 1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
# é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} e um ano bissexto!")
else:
    print(f"{ano} nao e um ano bissexto :(")