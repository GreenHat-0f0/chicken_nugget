
# Desafio do Desafio
# Existe um fenômeno meio absurdo na internet chamado hiper-tradução: pega-se uma frase,
# traduz para outro idioma, depois para outro, depois para outro… em cadeia — como um
# telefone sem fio passando por dezenas de línguas. Cada tradutor interpreta um pouco
# diferente; erros e nuances se acumulam. No fim, o texto quase não parece o original —
# mesmo quando a última etapa volta para português.
# Monte um programa (pode ser desafio03‐hyper.py ou evoluir o anterior) que:

# 1. Parte de uma frase em português definida no código;
# 2. Passa essa frase por uma lista de 30 idiomas que você escolhe (códigos como en,
# es, ja…);
# 3. A cada passo, o resultado traduzido vira a entrada do idioma seguinte;
# 4. O último idioma da lista deve ser pt, para o texto “voltar” ao português;
# 5. No final, exiba lado a lado (ou em sequência clara) o texto original e o texto
# após as 30 traduções,
# para comparar o quanto a mensagem se perdeu no caminho.

# Pense na ordem dos idiomas: quanto mais longa e variada a cadeia, mais bizarro tende
# a ficar o resultado.
# Esse é o exercício: ver na prática por que traduzir “em rodízio” não é a mesma coisa
# que traduzir direto.


from deep_translator import GoogleTranslator
texto= input("Traduzir: ")
print(texto)
map = {
    1: "pt",     # Inglês
    2: "es",     # Espanhol
    3: "en",  # Português (Brasil)
    4: "fr",     # Francês
    5: "de",     # Alemão
    6: "it",     # Italiano
    7: "ja",     # Japonês
    8: "tl",  # Chinês Simplificado
    9: "ko",     # Coreano
    10: "ru",    # Russo
    11: "ar",    # Árabe
    12: "hi",    # Hindi
    13: "nl",    # Holandês
    14: "tr",    # Turco
    15: "pl",    # Polonês
    16: "sv",    # Sueco
    17: "vi",    # Vietnamita
    18: "th",    # Tailandês
    19: "id",    # Indonésio
    20: "el",    # Grego
    21: "he",    # Hebraico
    22: "uk",    # Ucraniano
    23: "ro",    # Romeno
    24: "da",    # Dinamarquês
    25: "fi",    # Finlandês
    26: "no",    # Norueguês
    27: "cs",    # Checo
    28: "hu",    # Húngaro
    29: "ms",    # Malaio
    30: "sw"  # Chinês Tradicional
}
y=1
for i in (0, 29):
    x=map.get(y)
    z=map.get(y+1)
    y=y+1
    texto=GoogleTranslator(source=f"{x}", target=f"{z}").translate(texto)
texto=GoogleTranslator(source=f"{z}", target="pt").translate(texto)

        
# transl=GoogleTranslator(source="pt", target="af").translate(texto)
# transl=GoogleTranslator(source="af", target="sq").translate(transl)
# transl=GoogleTranslator(source="sq", target="am").translate(transl)
# transl=GoogleTranslator(source="am", target="ar").translate(transl)
# transl=GoogleTranslator(source="ar", target="hy").translate(transl)
# transl=GoogleTranslator(source="hy", target="as").translate(transl)
# transl=GoogleTranslator(source="as", target="az").translate(transl)
# transl=GoogleTranslator(source="az", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
# transl=GoogleTranslator(source="pt", target="en").translate(transl)
print(texto)
