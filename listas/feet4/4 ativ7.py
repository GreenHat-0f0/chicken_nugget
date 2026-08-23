# 7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
# informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
# não existam notas cadastradas, seu programa deve informar “Erro: não há notas
# cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
# programa:
# Notas
# -----
# 1 - Cadastrar
# 2 - Excluir
# 3 - Listar
# 4 - Calcular média
# 5 – Mostrar maior nota
# 6 – Mostrar menor nota
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
    5 - Mostrar maior nota
    6 - Mostrar menor nota
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
        
    elif x == 5:
        if not notas:
            print("\nNenhuma nota cadastrada.")
        else:
            cont = 0
            for i in notas:
                maior = notas[0]
                if notas[cont] > maior:
                    maior = notas[cont]
                cont += 1
            print(maior)

    elif x == 6:
        if not notas:
            print("\nNenhuma nota cadastrada.")
        else:
            cont = 0
            for i in notas:
                menor = notas[0]
                if notas[cont] < menor:
                    menor = notas[cont]
                cont += 1
            print(menor)
            
    if x != 0:
        grah()
    return x, notas, n
x, notas, n = grah()
