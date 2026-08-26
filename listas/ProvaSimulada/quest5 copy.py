# 5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
# • 1 – Adição;
# • 2 – Subtração;
# • 3 – Multiplicação;
# • 4 – Divisão;
# • 0 – Sair.
# Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
# mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.
# Bom estudo!
sinal = {
    1 : "+",
    2 : "-",
    3 : "*",
    4 : "/"
}
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
    if a != 1 and a != 2 and a != 3 and a != 4 and a != 0:
        print("Opção inválida")
    else:
        res = (eval(f"{x} {sinal(a)} {y}"))
        print(res)
    if a != 0:
        calculadora()
calculadora()
