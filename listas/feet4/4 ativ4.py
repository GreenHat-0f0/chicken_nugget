# 4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
# cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
# na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
# remoção dela e imprima a lista novamente.
cidade = []
y = 1
x = int(input("Quantas cidades? "))
for i in range(x):
    cidade.append(input(f"Digite a cidade {y}: "))
    y += 1
print(", ".join(cidade))
bomba = input("Qual cidade você deseja \033[9mbombardear\033[0m exluir? ")
cidade.remove(bomba)
print(", ".join(cidade))