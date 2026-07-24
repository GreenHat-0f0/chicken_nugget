#7 – Implemente um programa para calcular sua média final em uma determinada unidade
# curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
# uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
# está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6


x=int(input("Digite a quantidade de notas: "))
y=0
media=0

while x!=y:
  y=y+1
  z=int(input("Digite a nota "+str(y)+": "))
  media=media+z
print("Sua média final é "+str(media/x))
if media/x>=6:
  print("Aprovado(a)")
  print(":D")
else:
  print("Reprovado(a)")
  print(":(")