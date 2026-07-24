#8 – Suponha que você recebeu a última fatura do seu cartão de crédito no valor de R$
# 1.000,00 e que você não possa pagá-la. Faça um programa que calcule sua dívida total
# com o banco depois de uma quantidade de meses informada durante a execução do
# programa. Considere que a taxa de juros mensal de um cartão de crédito é de 15,30% ao
# mês. Fonte da taxa de juros utilizada: https://einvestidor.estadao.com.br/educacao-
# financeira/juros-cartao-de-credito-dicas-para-evitar-dividas/
# A título de curiosidade, simule sua dívida final no prazo de 2 anos (24 meses).

t = int(input("Digite a quantidade de meses: "))
d = 1000 * 1.153**t
print(f"Sua dívida após {t} meses será de R$ {d}")
