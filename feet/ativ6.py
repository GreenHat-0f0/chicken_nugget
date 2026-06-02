import os
import random
os.system("cls" if os.name == "nt" else "clear")
print("escolha pedra, papel ou tesoura.")
a = input("Jogador 1, sua vez: ") 
os.system("cls" if os.name == "nt" else "clear")
print("escolha pedra, papel ou tesoura.")
b = input("Jogador 2, sua vez: ")
print( a + " vs " + b )
if a=="pedra" and b=="tesoura" or a=="papel" and b=="pedra" or a=="tesoura" and b=="papel":
    print("Jogador 1 venceu!")
elif a==b:
    print("Empate!")
else:
    print("Jogador 2 venceu!")