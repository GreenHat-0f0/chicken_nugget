# Desafio 03 — Hiper-tradução
# Bibliotecas no Python
# Até aqui você usou coisas que já vêm com o Python, como print, input, time e os.
# Isso são módulos da biblioteca padrão: ferramentas prontas, sem instalar nada extra.
# Uma biblioteca (ou lib) é um pacote de código que alguém escreveu para você
# reutilizar. Em Python você importa o que precisa no topo do arquivo e usa as funções
# ou classes que ela oferece. Nem toda lib já está na instalação. Para pacotes de
# terceiros existe o pip — o instalador do Python. No terminal, por exemplo:
# pip install nome‐do‐pacote (no Linux do laboratório, se não funcionar, tente pip3).
# Neste desafio você vai instalar a lib deep‐translator, que conversa com um 
# de tradução na internet. Por isso o programa precisa de conexão na hora de rodar.
# O exercício
# Crie um programa em Python chamado desafio03.py que:

# 1. Instale (uma vez na máquina) a biblioteca deep‐translator com o pip;
# 2. Define um texto curto em português direto no código (uma frase simples);
# 3. Traduz esse texto do português para o inglês;
# 4. Imprime o original e a tradução no terminal.

# Use a classe GoogleTranslator. O programa deve ser sequencial (sem funções).
# Forma básica de tradução
# from deep_translator import GoogleTranslator
# texto = "Ola, mundo!"
# traducao = GoogleTranslator(source="pt", target="en").translate(texto)
# print(traducao) 
# Entrega: arquivo desafio03.py + captura de tela mostrando o texto em português e a
# tradução em inglês.


from deep_translator import GoogleTranslator
texto= input("Traduzir: ")
transl=GoogleTranslator(source="pt", target="en").translate(texto)
print(transl)
 