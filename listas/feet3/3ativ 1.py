# 1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
# programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
# apresentar apenas as idades que forem maiores ou iguais a 16.

alunos=[]
for i in range(6):
    alunos.append(int(input(f"Aluno {i+1}: ")))

print("Alunos com 16 anos ou mais: ")
for i in range(6):
    if alunos[i]>=16:
        print(alunos[i])

