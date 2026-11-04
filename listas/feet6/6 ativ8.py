# 8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
# deve ter um menu com as seguintes opções:
# Sistema de Cadastro
# -------------------
# 1 – Cadastrar estudante
# 2 – Cadastrar professor
# 3 – Listar estudantes
# 4 – Listar professores
# 5 – Alterar estudante pela matrícula
# 6 – Alterar estudante pelo nome
# 7 – Alterar professor pela matrícula
# 8 – Alterar professor pelo nome
# 9 – Excluir estudante pela matrícula
# 10 – Excluir professor pela matrícula
# 0 – Sair
# Opção:

class Estudante:
    def __init__(self, matri, nome, sobre_n, idade):
        self.matri = matri
        self.nome = nome
        self.sobre_n = sobre_n
        self.idade = idade
        
    def apresentar(self):
        return self.matri, self.nome, self.sobre_n, self.idade
    
class Professor:
    def __init__(self, matri, nome, sobre_n, idade, espec):
        self.matri = matri
        self.nome = nome
        self.sobre_n = sobre_n
        self.idade = idade
        self.espec = espec
        
    def apresentar(self):
        return self.matri, self.nome, self.sobre_n, self.idade, self.espec

estudantes = []
professores = []

def aaa():
    
    x = int(input("""
Sistema de Cadastro
-------------------
1 - Cadastrar estudante
2 - Cadastrar professor
3 - Listar estudantes
4 - Listar professores
5 - Alterar estudante pela matrícula
6 - Alterar estudante pelo nome
7 - Alterar professor pela matrícula
8 - Alterar professor pelo nome
9 - Excluir estudante pela matrícula
10 - Excluir professor pela matrícula
0 - Sair
Opção: """))
    
    if x == 1:
        matri = int(input("Matricula: "))
        nome = input("Nome: ")
        sobre_n = input("Sobrenome: ")
        idade = int(input("Idade: "))

        estudantes.append(Estudante(matri, nome, sobre_n, idade))
        
    elif x == 2:
        matri = int(input("Matricula: "))
        nome = input("Nome: ")
        sobre_n = input("Sobrenome: ")
        idade = int(input("Idade: "))
        espec = input("Especializacao: ")

        professores.append(Professor(matri, nome, sobre_n, idade, espec))
        
    elif x == 3:
        for estudante in estudantes:
            print(estudante.apresentar())
            
    elif x == 4:
        for professor in professores:
            print(professor.apresentar())
            
    elif x == 5:
        atual = int(input("Digite a matricula do estudante à ser alterado: "))
        for estudante in estudantes:
            if estudante.matri == atual:
                estudante.nome = input("Nome: ")
                estudante.sobre_n = input("Sobrenome: ")
                estudante.idade = int(input("Idade: "))
                
                break     

    elif x == 6:
        atual = input("Digite o nome do estudante à ser alterado: ")
        for estudante in estudantes:
            if estudante.nome == atual:
                estudante.matri = int(input("Matricula: "))
                estudante.sobre_n = input("Sobrenome: ")
                estudante.idade = int(input("Idade: "))
                
                break
            
    elif x == 7:
        atual = int(input("Digite a matricula do professor à ser alterado: "))
        for professor in professores:
            if professor.matri == atual:
                professor.nome = input("Nome: ")
                professor.sobre_n = input("Sobrenome: ")
                professor.idade = int(input("Idade: "))
                professor.espec = input("Especializacao: ")
                
                break     

    elif x == 8:
        atual = input("Digite o nome do professor à ser alterado: ")
        for professor in professores:
            if professor.nome == atual:
                professor.matri = int(input("Matricula: "))
                professor.sobre_n = input("Sobrenome: ")
                professor.idade = int(input("Idade: "))
                professor.espec = input("Especializacao: ")
                
                break       
                
    elif x == 9:
        lixo = int(input("Digite a matricula do estudante à ser exluído: "))
        for estudante in estudantes:
            if estudante.matri == lixo:
                estudantes.remove(estudante)
                
                break
            
    elif x == 10:
        lixo = int(input("Digite a matricula do professor à ser exluído: "))
        for professor in professores:
            if professor.matri == lixo:
                professores.remove(professor)
                
                break
                
    if x != 0:
        aaa()
aaa()        