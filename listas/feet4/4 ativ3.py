# 3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
# formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
# deve fazer isso de duas formas: com while e com for.
# Exibição com while:
# Nota: 9.0
# Nota: 7.5
# Nota: 8.0
# Exibição com for:
# Nota: 9.0
# Nota: 7.5
# Nota: 8.0

# 2 – Crie um programa que registrará as notas de um estudante. O programa deve
# perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
# notas e, ao final, exibir todas as notas digitadas na tela.

notas = []
y = 1
x = int(input("Quantas notas? "))
for i in range(x):
    notas.append(float(input(f"Digite a nota {y}: ")))
    y += 1
print("\nExibição com for:")
for i in notas:
    print("Nota: ", i)
y = 0
print("\nExibição com while:")
while y!= x:
    print("Nota: ", notas[y])
    y += 1
print("\nExibição com .join:")
print("Nota:", "\nNota: ".join(map(str, notas)))