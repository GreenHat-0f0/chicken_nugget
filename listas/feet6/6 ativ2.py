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
