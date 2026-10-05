# 6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
# que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
# usuário para inserir as horas e minutos, e exiba o tempo total em minutos.
x = int(input("Digite as horas: "))
y = int(input("Digite os minutos: "))
def tempo_total(x, y):
    print((x*60)+y)    
tempo_total(x, y)

