from stegano import lsb
path = input("Digite o nome do arquivo png: ")
mensagem = lsb.reveal(path)
print("A mensagem escondida é: ")
print(mensagem)