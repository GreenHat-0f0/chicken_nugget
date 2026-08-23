# 6 – Elabore um programa que funcionará como um cadastro de notas de um estudante. Seu
# programa deve permitir que notas sejam cadastradas ou removidas (através do seu
# índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
# deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
# avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
# calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
# e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
# com o seu programa:
# Notas
# -----
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 4 - Calcular média
# 0 - Sair
# Opção:

# //////
import sys
notas = []
n = 0
def grah():
    global notas, n
    print("""
    Menu
    ----
    1 - Cadastrar
    2 - Listar
    3 - Exluir
    4 - Calcular média
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    
    if x == 1:
        cadastro = int(input("Digite a nota: "))
        notas.append(cadastro)
        n += 1
    elif x == 2:
        
        if not notas:
            print("\nNenhuma nota cadastrada.")
        else:
            # print("Nota 1:", f"\nNota {cont+1}: ".join(map(str, notas)))
            cont = 1
            for i in notas:
                print(f"\nNota {cont}: {notas[cont-1]}")
                cont += 1
            
    elif x == 3:
        if not notas:
            print("\nNenhuma nota cadastrada.")
        else:
            # print("Nota 1:", f"\nNota {cont+1}: ".join(map(str, notas)))
            cont = 1
            for i in notas:
                print(f"\nNota {cont}: {notas[cont-1]}")
                cont += 1

            lixo = int(input("Qual nota voce deseja exluir? "))
            notas.pop(lixo-1)
            print(lixo, " Aniquilado.")
            
    elif x == 4:
        cont = 0
        media = 0
        for i in notas:
            cont += 1
            media += notas[cont-1]
        print(f"{(media/cont):.2f}")
            
    if x != 0:
        grah()
    return x, notas, n
x, notas, n = grah()
