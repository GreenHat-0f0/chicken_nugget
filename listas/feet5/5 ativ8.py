# 8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
# de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
# saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
# “P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar.

def conv(hora):
    x = hora.split(":")
    h = int(x[0])
    m = x[1]

    if h >= 12:
        bleep = "P.M."
    else:
        bleep = "A.M."

    if h == 0:
        h = 12
    elif h > 12:
        h = h - 12

    return h, m, bleep


def asd(hora, minutos, bleep):
    print(f"{hora}:{minutos} {bleep}")


while True:
    temp = input("Digite a hora em HH:MM: ")

    hora, minutos, bleep = conv(temp)

    asd(hora, minutos, bleep)

    continuar = input("Deseja converter outra hora? (s/n): ")

    if continuar.lower() != "s":
        break
