# 4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
# significados como valores. Inicie com:
# "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
# situação difícil, ou usar de meios extremos e exagerados"
# Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
# palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
# não encontrada”.
dicionario = {
    "apelar" : "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados",
}
for i in range(0, 4):
    pal = input("Digite uma palavra: ")
    dicionario[pal] = input("Digite o significado: ")
x = input("Qual palavra você deseja consultar?")
if not pal in dicionario:
    print("Palavra não encontrada")
else:
    print(dicionario[pal])