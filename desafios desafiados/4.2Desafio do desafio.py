# Desafio do Desafio

# Esconder texto na imagem não é criptografia. Quem souber usar lsb.reveal lê a mensagem — só não
# vê de cara. Para quem interceptar a foto não entender o conteúdo, falta uma camada a mais: cifrar o texto
# antes de esconder, e decifrar depois de revelar, com a mesma chave.
# Evolua os dois programas (ou crie desafio04‐esconder‐cifra.py e desafio04‐revelar‐cifra.py) assim:
# 1. Peça a chave com input() — um número inteiro que só quem envia e quem recebe conhece;
# 2. No esconder: leia a mensagem, cifre o texto com essa chave, depois passe o resultado para lsb.hide
# (nunca esconda o texto puro);
# 3. No revelar: use lsb.reveal, pegue o texto cifrado, decifre com a mesma chave e só então imprima a
# mensagem original;
# 4. Teste com um colega: sem a chave, o reveal deve mostrar lixo legível, não a frase real.
# Cifra de César (recomendada)
# Desloque cada letra do alfabeto chave posições (use % 26 para voltar ao início). Espaços, números e
# pontuação podem ficar como estão. Percorra a string com for letra in texto: e monte a saída letra a letra.
# Para decifrar, desloque na direção oposta (subtraia a chave em vez de somar). Maiúsculas e minúsculas
# devem ser tratadas separadamente (ord, chr, ou uma string alfabeto = "abc…z").
# Base64 (camada extra, opcional)
# O módulo base64 da biblioteca padrão embaralha o texto em outro formato — útil como segunda camada
# depois da César. Sozinho não tem chave secreta; por isso a César com chave numérica é obrigatória neste
# desafio.
# import base64
# embaralhado = base64.b64encode(texto.encode()).decode()
# original = base64.b64decode(embaralhado.encode()).decode()
# Ordem sugerida se usar as duas: César → base64 → lsb.hide. Na leitura, inverta: reveal → base64 →
# César.
# Entrega extra: os dois arquivos com cifra + captura mostrando que, sem a chave correta, o texto revelado
# não faz sentido — e que, com a chave, a mensagem original volta.