from stegano import lsb

chave = int(input("Chave: "))

path = input("Digite o nome do arquivo png: ")
text = input("Digite o texto a ser posto na imagem: ")
saida = input("Digite o nome do arquivo novo: ")


nova_imagem = lsb.hide(path, text)
nova_imagem.save(saida)
print("Se não teve mensagem de erro, é porque o código foi executado com sucesso.")