# 10 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os
# números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
# números digitados, assim como a soma e a média aritmética.

# should 0 be counted as a numero digitado?

x=None
y=0
z=0
while x!=0:
    x=int(input("Digite um numero: "))
    if x!=0:
        y=y+1
    z=z+x
print()
print(str(y)+" números digitados.")
print(str(z)+" é a soma.")
print(str(z/y)+" é a média.")