import copy

# trabalhando com copia rasa

d1= {
    'nome': 'Andre',
    'sobrenome':'caliari',
    'idade': 2,
    'l1': [0,1,2,3]

}

# criando uma cópia para que d2 não altere o d1
print(d1)

d2 = copy.deepcopy(d1) #deep copy é um metodo que raliza a copia profunda do dicionario em tudo que é mutavel
# permeando por todas as camamadas, ór exemplo se uma chave conter listas de listas ele copia todos e o torna mutavel para acesso e atualizações.
#Assim um dicionario não afetará mais o outro.
# d2 = d1

d2['nome'] = 'Pedro'
d2['l1'][1] = 99999 
print(d2)