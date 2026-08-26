# 2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
# Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
# exiba os números do menor para o maior.
bingo = []
cont = 0
def aaa():
    global cont
    for i in range(cont, 15):
        x = int(input(f"Numero {cont+1}: "))
        if x>=1 and x<=75:
            for j in bingo:
                if x == bingo(j):
                    break
            bingo.append(x)
            cont += 1
        else:
            print("Numero invalido. Tente novamente.")
            aaa()
            return cont
aaa()
print(bingo)

# 3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
# da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
# exiba o valor a ser pago.
# 4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
# significados como valores. Inicie com:
# "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
# situação difícil, ou usar de meios extremos e exagerados"
# Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
# palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
# não encontrada”.
# 5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
# • 1 – Adição;
# • 2 – Subtração;
# • 3 – Multiplicação;
# • 4 – Divisão;
# • 0 – Sair.
# Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
# mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.
# Bom estudo!