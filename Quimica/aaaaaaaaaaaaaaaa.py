inicial = float(input("Digite a massa inicial da substância: "))
meiaVida = float(input("Digite os tempos de meia vida-transcorridos: "))
final = inicial * (1/2)**meiaVida
print("\nMassa Final =", final, "g")