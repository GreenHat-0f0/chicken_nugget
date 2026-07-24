# 2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
# de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
# reprovado(a)).
media = 0
notas=[]
for i in range(4):
    notas.append(int(input(f"Nota {i+1}: ")))
    media += notas[i]

print("Media: ", media/4)
if media>=6:
    print("Aprovado")
else:
    print("Reprovado")