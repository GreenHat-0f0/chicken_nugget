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
per = []
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

        p = Pessoa(nome, idade, altura, peso)
        per.append(p)
        cont += 1
        
    elif x == 2:
        for id_pes, obj in enumerate(per):
            print(f"""
ID: {id_pes} | Nome: {obj.nome} | Idade: {obj.idade} | 
Altura: {obj.altura}m | Peso: {obj.peso}kg | 
IMC: {obj.imc():.2f}""")
    if x != 0:
        aaa()
    
    return cont, per, Pessoa
aaa()


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

# 9 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
# dados do disco, utilizando como base, o exercício 7.

# 10 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
# dados do disco, utilizando como base, o exercício 8.