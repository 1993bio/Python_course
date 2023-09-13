'''
introdução ao desempacotamento 
cada variavel antes da lista é referente a um item dentro da lista como se seque o exemplo abaixo.a
o _, significa uma varivel que nao tem importancia e abriga o primeiro valor da lista,
a variavel nome abriga o nome de interesse,
o *resto -> recebe todo restante da lista.

Tipo tuplas = uma lista imutavel vejamos
'''

_, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

#####################################################################