# 5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
# programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
# sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
# ser através de um menu com as seguintes opções:
# 1 – Cadastrar
# 2 - Excluir
# 3 - Alterar
# 4 - Listar
# 0 - Sair
# A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
# excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
# solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
# da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
# das pessoas cadastradas.

# nome, idade, altura e peso
import sys
pdts = []
idade = []
altura = []
peso = []
def grah():
    global pdts, idade, altura, peso
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar todos
    3 - Exluir
    4 - Alterar
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    if x == 1:
        pdts.append(input("Digite o nome da pessoa:  "))
        idade.append(input("Digite a idade da pessoa:  "))
        altura.append(input("Digite a altura da pessoa:  "))
        peso.append(input("Digite o peso da pessoa:  "))
        grah()
    elif x == 2:
        items = len(pdts)
        for i in range(items):
            print(pdts[i])
            print(" ", idade[i])
            print(" ", altura[i])
            print(" ", peso[i])
            print(" ")
        grah()
    elif x == 3:
        lixo = (input("Qual o nome da pessoa que voce deseja \033[9massassinar\033[0m exluir? "))
        bbb = pdts.index(lixo)
        pdts.pop(bbb)
        idade.pop(bbb)
        altura.pop(bbb)
        peso.pop(bbb)
        print(lixo, "Aniquilado.")
        grah()
    elif x == 4:
        dif = input("Qual o nome da pessoa que voce deseja \033[9mfazer lavagem cerebral\033[0m alterar os dados? ")
        bbb = pdts.index(dif)
        idade[bbb] = input("Idade: ")
        altura[bbb] = input("altura: ")
        peso[bbb] = input("peso: ")
        grah()
    return pdts, idade, altura, peso
pdts, idade, altura, peso  = grah()