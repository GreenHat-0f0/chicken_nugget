# 6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
# baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
# o nome da pessoa como critério de busca.

import sys
pdts = []
idade = []
altura = []
peso = []
cod = []
def grah():
    global pdts, idade, altura, peso, cod
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar todos
    3 - Exluir
    4 - Alterar
    5 - Pesquisar
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    if x == 1:
        pdts.append(input("Digite o nome da pessoa:  "))
        cod.append(input("Digite o codigo da pessoa:  "))
        idade.append(input("Digite a idade da pessoa:  "))
        altura.append(input("Digite a altura da pessoa:  "))
        peso.append(input("Digite o peso da pessoa:  "))
        grah()
    elif x == 2:
        items = len(pdts)
        for i in range(items):
            print(pdts[i])
            print(" ", cod[i])
            print(" ", idade[i])
            print(" ", altura[i])
            print(" ", peso[i])
            print()
        grah()
    elif x == 3:
        y = input("""Exluir por nome ou por codigo?
1 - Nome
2 - Codigo
""")
        if y == "1":
            lixo = (input("Qual o nome da pessoa que voce deseja \033[9massassinar\033[0m exluir? "))
            bbb = pdts.index(lixo)
            pdts.pop(bbb)
            cod.pop(bbb)
            idade.pop(bbb)
            altura.pop(bbb)
            peso.pop(bbb)
            print(lixo, "Aniquilado.")
        elif y == "2":
            lixo = (input("Qual o codigo da pessoa que voce deseja \033[9massassinar\033[0m exluir? "))
            bbb = cod.index(lixo)
            pdts.pop(bbb)
            cod.pop(bbb)
            idade.pop(bbb)
            altura.pop(bbb)
            peso.pop(bbb)
            print(lixo, "Aniquilado.")
            
        grah()
    elif x == 4:
        dif = input("Qual o nome da pessoa que voce deseja \033[9mfazer lavagem cerebral\033[0m alterar os dados? ")
        bbb = pdts.index(dif)
        cod[bbb] = input("Codigo: ")
        idade[bbb] = input("Idade: ")
        altura[bbb] = input("altura: ")
        peso[bbb] = input("peso: ")
        grah()
    elif x == 5:
        pesq = input("Qual o nome da pessoa que voce deseja \033[9mstalkear\033[0m pesquisar? ")
        bbb = pdts.index(pesq)
        print(f"""
        {pdts[bbb]}
            {cod[bbb]}
            {idade[bbb]}
            {altura[bbb]}
            {peso[bbb]}
        """)
        grah()
    return pdts, idade, altura, peso, cod
pdts, idade, altura, peso, cod  = grah()