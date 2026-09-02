# 3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
# programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
# e exibir o resultado na tela.


alt = int(input("Digite a altura do cilindro: "))
raio = int(input("Digite o raio do cilindro: "))

def a():
    global vol
    vol = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899 * raio**2 * alt
    return vol
a()
print(vol)