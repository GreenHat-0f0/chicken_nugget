text = input("Texto: ")
chave=int(input("Chave: "))
cifra = ""
for letra in text:
    num = (ord(letra) + chave)
    if num >122:
        num %= 122
        num += 96
    elif num < 96:
        num += 26
    cifra += (chr(num))

print(cifra)