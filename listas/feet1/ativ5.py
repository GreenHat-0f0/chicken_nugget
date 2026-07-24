x = float(input("Qual a temperatura de hoje?: "))
if x<10:
    print("Está muito frio! Use roupas quentes.")
elif x<=20:
    print("Frio. Vista-se bem!")
elif x<=25:
    print("Temperatura agradável.")
elif x<=30:
    print("Está ficando quente!")
else:
    print("Está muito quente! Fique hidratado.")
