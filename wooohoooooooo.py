def converter_hora(hora):
    partes = hora.split(":")
    h = int(partes[0])
    m = partes[1]

    if h >= 12:
        periodo = "P"
    else:
        periodo = "A"

    if h == 0:
        h = 12
    elif h > 12:
        h = h - 12

    return h, m, periodo


def imprimir_hora(hora, minutos, periodo):
    print(f"{hora}:{minutos} {periodo}.M.")


while True:
    entrada = input("Digite a hora no formato HH:MM: ")

    hora, minutos, periodo = converter_hora(entrada)

    imprimir_hora(hora, minutos, periodo)

    continuar = input("Deseja converter outra hora? (s/n): ")

    if continuar.lower() != "s":
        break
