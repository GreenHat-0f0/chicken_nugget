# 5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
# Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
# conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
# amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
# Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
# Amigos Próximos
# ---------------
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 0 - Sair

# Opção:
import sys
pdts = []
def grah():
    global pdts
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar
    3 - Exluir
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    if x == 1:
        cadastro = (input("Digite o nome do(a) amigo(a): "))
        pdts.append(cadastro)
    elif x == 2:
        if not pdts:
            print("\nNenhum amigo cadastrado.")
        else:
            print("\n", pdts)
    elif x == 3:
        lixo = (input("Qual amigo voce deseja exluir? "))
        idx = pdts.index(lixo)
        pdts.pop(idx)
        print(lixo, " Aniquilado.")
    grah()
    return x, pdts
x, pdts = grah()