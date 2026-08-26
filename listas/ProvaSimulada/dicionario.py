# teste = ["ignacio", "waltrik"]
# #            0    ,     1

# print(teste[0])

# pessoa = ["Ignacio Sepulveda", "741.515.778.11", 25]
# #                 0          ,        1        ,  2
# print("A idade do ignacio é ", pessoa[2])

# pessoa = {
#     "nome": "ignacio sepulveda",
#     "cpf": "741.515.778.11",
#     "idade": 25,
# }
# print(pessoa["idade"])

# Forma simplês
professores = {
    "001": "Prof Schalata",
    "002": "Prof Waltrik",
    "607": "Prof Ignacio",
    "333": "Prof Ryan e Cosplay"
}

# professores["123"] = "Prof Thiago Paes"

# print(professores)

# # Forma maiscomplicada
# professores = [{
#     "nome": "Ignacio",
#     "area": "informatica",
#     "idade": 25,
#     "materias": ["PES", "DJO"],
#     "salas": {
#         "PES": "A102"
#     }
# },{
#     "nome": "Ryan",
#     "area": "informatica",
#     "idade": 24,
#     "materias": [],
#     "salas": {}
# }]
# #    [ {...} ][ {...} ]
# #        0        1

# print(  professores[0]["salas"]["PES"]  )
# #     { nome: ignacio }
# print(   professores[0]["materias"][1]  )

print( professores["001"])
# print( professores[])