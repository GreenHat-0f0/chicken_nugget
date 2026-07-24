# 1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
# do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
# deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
# programa deve exibir o nome de todos os bairros cadastrados na tela.

lista = ["Palhocinha"]
cont = 1
print("Digite o nome de cinco bairros:")
for i in range(5):
    lista.append(input(f"{cont}: "))
    cont += 1
print(lista)