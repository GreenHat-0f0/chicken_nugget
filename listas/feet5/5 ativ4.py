# 4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
# resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
# números ao usuário, chamar a função e exibir o resultado da soma na tela.

weee = []
for num in range(0, 4):
    x = int(input(f"digite o {num+1}⁰ numero: "))
    weee.append(x)
def soma():
    print("Soma = ", sum(weee))
soma()