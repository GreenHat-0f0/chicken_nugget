# 5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
# numéricas:
# a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
# possua um ou mais elementos;
# b) uma função que receba uma lista e retorne o maior valor;
# c) uma função que receba uma lista e retorne o menor valor;
# d) uma função que receba uma lista e retorne o valor médio.
# As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
# programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
# (comprove) o funcionamento de cada uma das funções.


# a)
def vazio(lista):
    return len(lista) == 0


# b)
def maior(lista):
    if vazio(lista):
        return -1
    return max(lista)


# c)
def menor(lista):
    if vazio(lista):
        return -1
    return min(lista)


# d) Retorna o valor médio da lista
def media(lista):
    if vazio(lista):
        return -1
    return sum(lista) / len(lista)


#/////////////////
lista1 = []
lista2 = [10, 20, 30, 40, 50]


print("Lista 1:", lista1)
print("Vazia:", vazio(lista1))
print("Maior valor:", maior(lista1))
print("Menor valor:", menor(lista1))
print("Valor médio:", media(lista1))
print()

print("Lista 2:", lista2)
print("Vazia:", vazio(lista2))
print("Maior valor:", maior(lista2))
print("Menor valor:", menor(lista2))
print("Valor médio:", media(lista2))
