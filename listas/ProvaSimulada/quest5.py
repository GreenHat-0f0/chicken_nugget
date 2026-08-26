# 5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
# • 1 – Adição;
# • 2 – Subtração;
# • 3 – Multiplicação;
# • 4 – Divisão;
# • 0 – Sair.
# Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
# mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.
# Bom estudo!
def calculadora():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("""
        
    • 1 – Adição;
    • 2 – Subtração;
    • 3 – Multiplicação;
    • 4 – Divisão;
    • 0 – Sair.
        
    escolha uma opção: 
        """)
    a = int(input())
    if a == 1:
        print(x+y)
    elif a == 2:
        print(x-y)
    elif a == 3:
        print(x*y)
    elif a == 4:
        print(x/y)
    elif a != 0:
        print("Opção inválida")
    if a != 0:
        calculadora()
calculadora()
