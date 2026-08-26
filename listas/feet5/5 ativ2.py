# 2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
# ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
# resultado na tela.
x = int(input("Digite o número: "))
def epar():
    if x % 2 == 0:
        print(x, " é par")
    else:
        print(x, " é ímpar")
epar()