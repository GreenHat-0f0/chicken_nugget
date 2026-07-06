text = input()
chave=int(input())
cifra = ""
for letra in text:
    num = (ord(letra) + chave)
    cifra += [chr(num)]
    print(cifra)
    # aaa = aaa+cifra
# print(aaa)
# for letra in 