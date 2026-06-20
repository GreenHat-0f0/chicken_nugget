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
    # Exibição do Menu conforme o enunciado
    print("\nMenu")
    print("-------")
    print("1 – Adição")
    print("2 – Subtração")
    print("3 – Divisão")
    print("4 – Multiplicação")
    print("0 - Sair")
    
    opcao = input("Digite a opção: ")
    
    # Verifica se o usuário deseja sair do programa
    if opcao == '0':
        print("Programa encerrado. Até logo!")
        break
        
    # Verifica se a opção digitada é inválida
    if opcao not in ['1', '2', '3', '4']:
        print("\n[ERRO] Opção inválida! Por favor, escolha uma opção do menu.")
        continue  # Exibe o menu novamente sem pedir os números
        
    # Solicita os números apenas se a opção for válida
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("\n[ERRO] Entrada inválida! Por favor, digite números válidos.")
        continue

    # Executa a operação escolhida
    if opcao == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
        
    elif opcao == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
        
    elif opcao == '3':
        # Validação para evitar a divisão por zero
        if num2 == 0:
            print("\n[ERRO] Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
            
    elif opcao == '4':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")



print("""
Menu
-------
1 – Adição
2 – Subtração
3 – Divisão
4 – Multiplicação
0 - Sair
Digite a opção:""")