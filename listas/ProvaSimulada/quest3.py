# 3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
# da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
# exiba o valor a ser pago.

prec = int(input("Preço: "))
quant = int(input("Quantidade: "))
total = prec * quant
if total >=100:
    total *= 0.9
print("Total a ser pago: ", total)
