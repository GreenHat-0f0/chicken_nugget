# 5 – Crie uma classe chamada Pessoa com:
# • Atributos: nome, idade, altura e peso;
# • Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
# pessoa;
# • Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
# • Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
# Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
# estão corretos.
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
    
pessoa1 = Pessoa("Eliott", 17, 1.66, 72)
pessoa2 = Pessoa("IG", 72, 2, 80)
pessoa3 = Pessoa("E.T.", 100, 1, 1)

print(pessoa1.exibir())
print(pessoa1.imc())
print(pessoa1.iiimc())

print(pessoa2.exibir())
print(pessoa2.imc())
print(pessoa2.iiimc())

print(pessoa3.exibir())
print(pessoa3.imc())
print(pessoa3.iiimc())
