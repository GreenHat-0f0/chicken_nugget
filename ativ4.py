import os
os.system("cls" if os.name == "nt" else "clear")
print ("Escolha um superpoder!")
print ("Digite '1' para FORÇA")
print ("Digite '2' para VELOCIDADE")
print ("Digite '3' para VOO")
def guh():
    x = int(input("Qual você escolhe? " ))
    if x ==1:
        print("Você seria o Hulk!")
    elif x==2:
        print("Você seria o Flash!")
    elif x==3:
        print("Você seria o Superman!")
    else:
        print("Isso não é um superpoder válido,")
        print("Escolha outro!")
        guh()
guh()