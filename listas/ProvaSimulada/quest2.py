# 2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
# Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
# exiba os números do menor para o maior.
bingo = []
cont = 0
def aaa():
    global cont
    for i in range(cont, 15):
        x = int(input(f"Numero {cont+1}: "))
        if x>=1 and x<=75 and not x in bingo:
            bingo.append(x)
            cont += 1
        else:
            print("Numero invalido. Tente novamente.")
            aaa()
            return cont
aaa()
# ordem = []
# for i in bingo:
bingo.sort()
print(bingo)