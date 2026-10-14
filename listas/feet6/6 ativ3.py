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
        return self.saldo

conta1 = ContaBancaria("nsei", 100)

conta1.depositar(int(input("Depositar: ")))
print(f"R$ {conta1.mostrar_saldo()}")
conta1.sacar(int(input("Sacar: ")))
print(f"R$ {conta1.mostrar_saldo()}")
