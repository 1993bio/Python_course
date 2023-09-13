'''
introdução ao desempacotamento 
cada variavel antes da lista é referente a um item dentro da lista como se seque o exemplo abaixo.a
o _, significa uma varivel que nao tem importancia e abriga o primeiro valor da lista,
a variavel nome abriga o nome de interesse,
o *resto -> recebe todo restante da lista.

Tipo tuplas = uma lista imutavel vejamos

uma tupla é uma sequencia de dados sem estar dentro de colchetes,
diferente da lista que precisa estar dentro de colchetes

'''
# uma tupla

nomes = 'andre', 'luiz', 'caliari'
print(nomes[0])
print(nomes)

nomes_2 = ['pedro', 'felipe', 'ana']

# ou se tivermos uma lista e queremos converter em uma tupla fazemos
nomes_2 = tuple(nomes_2) # convertendo uma tupla em uma lista
print(nomes_2)

# revertendo a tupla para uma lista
nomes_2 = list(nomes_2)
print(nomes_2)