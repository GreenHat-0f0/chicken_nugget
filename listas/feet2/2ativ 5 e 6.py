#   Faça um programa que exiba na tela a tabuada de um número informado pelo 
# usuário. Vamos supor que o número informado seja o 2, então o programa deve exibir o
# seguinte resultado na tela:
# Tabuada do número 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

#6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
# tabuada, em vez de começar iniciar no 1 e terminar no 10.

x=int(input("Digite um número: "))
y=int(input("Digite um início: "))
z=int(input("Digite um fim: "))

while y!=z:
  print(str(x)+ " x "+str(y)+" = "+str(x*y))
  y=y+1

print(str(x)+ " x "+str(y)+" = "+str(x*y))
