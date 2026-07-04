text = input()
chave=int(input())
chave%=26
aaa = ""
for letra in text:
    num = ord(letra) - 97 + chave
    cifra = [chr(num+26)]
    print(cifra)
    aaa = text+cifra
print(text)
# for letra in 