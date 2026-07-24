# 4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
# um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
# lista. Seu programa deve ter um menu com a seguinte estrutura:
# 1 – Cadastrar
# 2 - Excluir
# 3 - Listar
# 0 - Sair
# A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
# houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
# disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
# nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
# simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
# um espaço vago na lista.

import sys
n = 0
pdts = ["o"]*15
def grah():
    global pdts, n
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar todos
    3 - Exluir
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    if x == 1:
        def AAA():
            global pdts, n
            cadastro = (input("Digite o placa do carro que você deseja cadastrar: "))
            if cadastro != "o":
                pdts[n] = cadastro
                n += 1
            else:
                print("ISTO NAO E UMA OPCAO VALIDA, TOLO!!!")
                AAA()
            return n, pdts
        if n<15:
            n, pdts = AAA()
        else:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("O estacionamento esta cheio.")
        grah()
    elif x == 2:
        for i in pdts:
            if i != "o":
                print(i)
        grah()
    elif x == 3:
        lixo = (input("Qual a placa do carro que voce deseja exluir? "))
        idx = pdts.index(lixo)
        pdts[idx] = "o"
        print(lixo, " Aniquilado.")
        grah()
    return x, pdts, n
x, pdts, n = grah()