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


# 5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
# • 1 – Adição;
# • 2 – Subtração;
# • 3 – Multiplicação;
# • 4 – Divisão;
# • 0 – Sair.
# Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
# mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.
# Bom estudo!