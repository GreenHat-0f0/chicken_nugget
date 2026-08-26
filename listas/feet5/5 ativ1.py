# 1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
# notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.
x = int(input("Digite a primeira nota: "))
y = int(input("Digite a segunda nota: "))
z = int(input("Digite a terceira nota: "))
def media():
    med = (x+y+z)/3
    print(med)
media()