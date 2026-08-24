# 1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
# Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
# Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
# professores já cadastrados no sistema de uso dos laboratórios.
# O sistema deve possuir:

# • Um cadastro completo de professores (adicionar, alterar, excluir e listar) que
# associe o código do professor ao seu nome, alguns professores já devem ser pré-
# cadastrados, veja a lista abaixo;

# • Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,
# alterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas
# Lab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no
# sistema, o que pode ser alterado são os acessos, alguns professores já devem
# ser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a
# implementação, sugere-se que os laboratórios sejam associados ao código do
# professor e não ao seu nome);
# • Teste de acesso ao laboratório: deve ser possível informar o nome de um
# laboratório e um código de professor para verificar se o acesso é permitido ou não
# (por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o
# código de professor 002, nesse caso, o sistema deve negar o acesso).
# Pré-cadastro de Professores (códigos x nomes)
# 001 – Prof Thiago Paes
# 002 – Prof Schalata
# 003 – Prof Ignácio
# 004 – Prof Ryan
# 005 – Prof André
# 006 – Profª Fabiana
# 007 – Prof Alberto
# 008 – Prof Juliano
# 009 – Prof Thiago Waltrik
# 010 – Prof João Eduardo
# Pré-cadastro de Acessos (laboratório x professor)
# • Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª
# Fabiana;
# • Lab103 – Prof Alberto;
# • Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
# • Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
# • Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
# • Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
# João Eduardo.

import sys
professor = ["Prof Schalata", "Prof Ignácio", "Prof Ryan", "Prof André", "Profª Fabiana", "Prof Alberto", "Prof Juliano", "Prof Thiago Waltrik", "Prof João Eduardo"]
codigo = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010"]
n = 0
def grah():
    global professor, n, codigo
    print("""
    Menu
    ----
    1 - Adicionar
    2 - Listar
    3 - Exluir
    4 - Alterar
    0 - Sair 
        
        """)
    x = int(input("Digite uma opção: "))
    
    if x == 1:
        cadastro = (input("Digite o nome do professor: "))
        professor.append(cadastro)
        cadastro = (input("Digite o codigo do professor: "))
        codigo.append(cadastro)
        n += 1
    elif x == 2:
        
        if not professor:
            print("\nNenhum professor cadastrado.")
        else:
            cont = 1
            for i in professor:
                print(f"\n{professor[cont-1]} - {codigo[cont-1]}")
                cont += 1
            
    elif x == 3:
        if not professor:
            print("\nNenhum professor cadastrado.")
        else:
            cont = 1
            for i in professor:
                print(f"\n{professor[cont-1]} - {codigo[cont-1]}")
                cont += 1

            lixo = (input("Qual o codigo do professor que voce deseja exluir? "))
            ind = codigo.index(lixo)
            codigo.pop(ind)
            professor.pop(ind)
            print(professor[ind], " Aniquilado.")
            
    elif x == 4:
        if not professor:
            print("\nNenhum professor cadastrado.")
        else:
            cont = 1
            for i in professor:
                print(f"\n{professor[cont-1]} - {codigo[cont-1]}")
                cont += 1
    
        alterar = (input("Digite o codigo do professor que voce deseja alterar: "))
        ind = codigo.index(alterar)
        bosta = (input("Digite o nome alterado do professor: " ))
        
            
    if x != 0:
        grah()
    return x, professor, n
x, professor, n = grah()
