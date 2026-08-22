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
pdts = []
n = 0
def grah():
    global pdtsm, n
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
        cadastro = (input("Digite a nota: "))
        pdts.append(cadastro)
        n += 1
    elif x == 2:
        
        if not pdts:
            print("\nNenhuma nota cadastrada.")
        else:
            cont = 1
            print("Nota 1:", f"\nNota {cont+1}: ".join(map(str, pdts)))
            
    elif x == 3:
        if not pdts:
            print("\nNenhuma nota cadastrada.")
        else:
            cont = 1
            print("Nota 1:", f"\nNota {cont+1}: ".join(map(str, pdts)))
            lixo = int(input("Qual nota voce deseja exluir? "))
            pdts.pop(lixo-1)
            print(lixo, " Aniquilado.")
        
    if x != 0:
        grah()
    return x, pdts, n
x, pdts, n = grah()
