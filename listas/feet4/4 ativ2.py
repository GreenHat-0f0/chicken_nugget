# 2 – Crie um programa que registrará as notas de um estudante. O programa deve
# perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
# notas e, ao final, exibir todas as notas digitadas na tela.

notas = []
y = 1
x = int(input("Quantas notas? "))
for i in range(x):
    notas.append(int(input(f"Digite a nota {y}: ")))
    y += 1
print(notas)