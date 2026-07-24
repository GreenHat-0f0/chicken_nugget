# 12 – Implemente um programa que funcione como uma calculadora entre dois números
# informados. Seu programa deve exibir um menu que solicite a operação a ser realizada
# entre dois números (adição, subtração, divisão e multiplicação) e os dois números a
# serem utilizados no cálculo. Se o usuário digitar uma opção inválida, deve alertar o
# usuário e exibir o menu novamente. Utilize um menu, como o abaixo, no seu programa:
# Menu
# -------
# 1 – Adição
# 2 – Subtração
# 3 – Divisão
# 4 – Multiplicação
# 0 - Sair
# Digite a opção:
# Alguns desses exercícios são de autoria do professor e outros foram selecionados pelo no
# livro Introdução à Programação com Python de Nilo Ney Coutinho Menezes. Para mais
# exercícios, consulte os capítulos 3 e 4 do livro.

while True:
    print("""
    Menu
    -------
    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    0 - Sair
    Digite a opção:""")
    
    opcao = input("Digite a opção: ")
    
    if opcao == '0':
        print("Programa encerrado.")
        break
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválidaaaaaaaaaaaaaaaaa!")
        continue 
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida!")
        continue
    if opcao == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
        
    elif opcao == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
        
    elif opcao == '3':
        if num2 == 0:
            print("\n[ERRO] Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
            
    elif opcao == '4':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")


