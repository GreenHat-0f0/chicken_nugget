# 7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
# para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
# peso, baseado, também, no nome informado.

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
    global cont, pessoas, Pessoa
    
    x = int(input("""
    Cadastro de Pessoas
    -------------------
    1 - Cadastrar
    2 - Listar
    3 - Excluir
    4 - Atualizar
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
            
    elif x == 3:
        lixo = input("Digite o nome da pessoa à ser exluída: ")
        for pessoa in pessoas:
            if pessoa.nome == lixo:
                pessoas.remove(pessoa)
                break
                
    elif x == 4:
        atual = input("Digite o nome da pessoa à ser atualizada: ")
        for pessoa in pessoas:
            if pessoa.nome == atual:
                pessoa.idade = int(input("Idade: "))
                pessoa.altura = int(input("Altura: "))
                pessoa.peso = int(input("Peso: "))
    if x != 0:
        aaa()
aaa()