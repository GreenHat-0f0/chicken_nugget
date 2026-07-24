us = (input("Digite seu usuário: "))
pas = int(input("Digite sua senha: "))
if us == "admin" and pas == 12345:
    print("Login bem-sucedido")
else:
    print("Nome de usuário ou senha incorretos")
