# Dicionários em python ( tipo dict)

# Dicionários são estruturas de dados do tipo par de "chaves" e "valor""

# chaves podem ser consideradas com oos indices
# que vimos em listas e podem ser de tipos imutaveis como:
# str, int, float, bool, tuple, etc...

# O valor pode er de qualquer tipo, incluindo outro dicionário
# usamos as chaves {} ou classe "dict" para criar dicionarios

#imutavel: str, int, float, bool, tuple
#mutavel: dict, list
# primeira forma 
# Pessoa = {
#     'nome': 'André',
#     'sobrenome': 'Caliari',
#     'idade': '30',
#     'altura': '1.80'
# }

# # segunda forma por meeio da função dict
# Pessoa_2 = dict(nome= 'Andre', sobrenome='Caliari')

# print(Pessoa, type(Pessoa))
# print(Pessoa_2, type(Pessoa_2))

# -----------------------------------------
Pessoa = {
    'nome': 'André',
    'sobrenome': 'Caliari',
    'idade': '30',
    'altura': '1.80'
}
# acessando valores dos dicionarios 
#print(Pessoa['enderecos'])

# ou

#for chaves in Pessoa: # mesmo que keys para pegar valores de chaves
#    print(chaves, Pessoa[chaves])

# metodo 1
print(Pessoa.__len__())

# metodo 2
print(len(Pessoa))
# retornando as chaves do dicionario com o metodo keys
print(Pessoa.keys())

# retornando as chaves em uma lista ou uma tupla
print(list(Pessoa.keys()))
print(tuple(Pessoa.keys()))

# utilizando o metodo values de dicionarios 
print(list(Pessoa.values()))


for valor in Pessoa.values(): # mesmo que values para pegar valores de chaves
    print(valor)

# utilizando o metodo items
print(list(Pessoa.items())) # mostra a chave e os valores das chaves


for chave, valor in Pessoa. items():
    print(chave,valor)