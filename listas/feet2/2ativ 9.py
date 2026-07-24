# 9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
# um determinado presente para você mesmo(a). Considere que todo mês você depositará,
# em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
# valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
# durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
# a poupança não possui nenhum saldo inicial. Você pode utilizar uma calculadora de juros
# compostos para validar o cálculo do seu algoritmo, por exemplo o site:
# https://www.idinheiro.com.br/calculadoras/calculadora-juros-compostos/


dep = float(input("Digite o valor do depósito mensal: "))
saldo=0
for mes in range(1, 25):
    saldo=(saldo+dep)
    if mes!=24:
        saldo=saldo*1.005
    print(f"Mês {mes}: R$ {saldo}")
