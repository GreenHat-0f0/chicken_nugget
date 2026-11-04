# 6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
# funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
# conforme abaixo:
# Cadastro de Pessoas
# -------------------
# 1 – Cadastrar
# 2 – Listar
# 0 – Sair
# Opção:

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def exibir(self):
        return self.nome, self.idade, self.altura, self.peso
    def imc(self):
        # : IMC = peso (kg) ÷ [altura (m) × altura (m)].
        eh = self.peso/(self.altura*self.altura)
        return eh
    def iiimc(self):
        eh = self.peso/(self.altura*self.altura)
        return self.nome, eh
    
cont = 0
pessoas = []
def aaa():
    global cont, per, Pessoa
    x = int(input("""
    Cadastro de Pessoas
    -------------------
    1 - Cadastrar
    2 - Listar
    0 - Sair
    Opção: """))
    
    if x == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoas.append(Pessoa(nome, idade, altura, peso))
        cont += 1
        
    elif x == 2:
        for pessoa in pessoas:
            print(pessoa.exibir())
    if x != 0:
        aaa()
aaa()

