pessoa = {} # cria um dicionario vazio
##

##

##

# pessoa['nome']= 'Andre Luiz' # cria chaves no dicionario no caso aqui nome da pessoa

# print(pessoa) #mostra o que criou 
# print(pessoa['nome']) # cessando  a chave nome no dicionario 
#---------------------------------------------------------------------------------------------
#Trabalhando com chaves dinamicas 
chave = input('digite um valor para chave: ') # recebe qualquer valaor que será atribuido a chave e muda de forma diniamica

pessoa[chave] = 'André Luiz' # valor que será atribuido a chave criada
pessoa['sobrenome'] = 'Caliari'


print(pessoa[chave])
pessoa[chave]= 'Pedro'


print(pessoa)

#deletando uma chave
del pessoa['sobrenome']

print(pessoa)






