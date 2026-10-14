# 1 – Crie uma classe chamada Livro com:
# • Atributos: titulo e autor.
# • Um método chamado descricao que retorna: "{titulo} foi escrito por {autor}."
# Teste criando um objeto e chamando o método para exibir a descrição.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}."

livro1 = Livro(1984, "George Orwell")
print(livro1.descricao())


# 2 – Crie uma classe chamada Carro com:
# • Atributos: marca e cor.
# • Um método chamado pintar que recebe uma nova cor como argumento e altera o
# atributo cor para essa nova cor.
# • Um método chamado mostrar_cor que retorna a cor atual do carro.
# Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
# com mostrar_cor.

class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
    def pintar(self):
        self.cor = input("Nova cor: ")
    def mostrar_cor(self):
        return self.cor

carro1 = Carro("azul", "Toyota")
carro1.pintar()
print(carro1.mostrar_cor())


# 3 – Crie uma classe chamada ContaBancaria com:
# • Atributos: titular e saldo.
# • Um método chamado depositar que recebe um valor e adiciona ao saldo.
# • Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
# validar o saldo).
# • Um método chamado mostrar_saldo que retorna o saldo atual.
# Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, v):
        self.saldo += v
    def sacar(self, m):
        self.saldo -= m
    def mostrar_saldo(self):
        return saldo

conta1 = ContaBancaria("nsei", 100)

conta1.depositar(int(input("Depositar: ")))
conta1.mostrar_saldo()

# 4 – Crie uma classe chamada Produto com:
# • Atributos: nome e quantidade.
# • Um método chamado esta_disponivel que retorna True se a quantidade for maior
# que 0 e False caso contrário.
# • Um método chamado vender que diminui a quantidade em 1.
# Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
# novamente.
# 5 – Crie uma classe chamada Pessoa com:
# • Atributos: nome, idade, altura e peso;
# • Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
# pessoa;
# • Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
# • Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
# Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
# estão corretos.
# 6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
# funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
# conforme abaixo:
# Cadastro de Pessoas
# -------------------
# 1 – Cadastrar
# 2 – Listar
# 0 – Sair
# Opção:
# 7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
# para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
# peso, baseado, também, no nome informado.
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