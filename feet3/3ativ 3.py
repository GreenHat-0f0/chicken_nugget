# 3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
# loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
# os elementos da lista com -1, este valor indicará que o elemento está vago para o
# cadastro. 
# -Seu programa deve ter um menu com uma opção para cadastrar um novo código (apenas um por vez) 
# -e para listar todos os códigos cadastrados (não devem ser
# listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
# na hora de cadastrar um novo código e também não deve ser possível cadastrar um
# produto com o código -1. No momento do cadastro, não deve ser informado o valor do
# índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
# Menu
# ----
# 1 – Cadastrar
# 2 – Listar todos
# 0 – Sair

import sys
n = 0
pdts = [-1]*10
def grah():
    global pdts, n
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar todos
    0 - Sair 
        
        """)


    x = int(input("Digite uma opção: "))
    if x == 1:
        def AAA():
            global pdts, n
            cadastro = int(input("Digite o código do produto que você deseja cadastrar: "))
            if cadastro != -1:
                pdts[n] = cadastro
                n += 1
            else:
                print("ESCOLHA OUTRO NOME, TOLO!!!")
                AAA()
            return n, pdts
        if n<10:
            n, pdts = AAA()
        else:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("O estoque esta cheio.")
        grah()
    elif x == 2:
        for i in pdts:
            if i != -1:
                print(i)
        grah()
    elif x == 0:
        sys.exit()
    return x, pdts, n
x, pdts, n = grah()