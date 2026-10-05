# 7 - Desenha moldura. Construa uma função que desenhe um retângulo usando os
# caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para valores dentro
# da faixa de forma elegante.
linhas = int(input("Linhas: "))
if linhas > 20:
    linhas = 20
elif linhas < 1:
    linhas = 1
colunas = int(input("Colunas: "))
if colunas > 20:
    colunas = 20
elif colunas < 1:
    colunas = 1
def moldura(linhas, colunas):
    # print("+", "-"*linhas, "+"), print(("\n|", " "*linhas, "|")*colunas,), print("+", "-"*linhas, "+")
    print(f"+{"-"*linhas}+{(f"\n|55{" "*linhas}|")*colunas}\n+{"-"*linhas}+")
moldura(linhas, colunas)
    