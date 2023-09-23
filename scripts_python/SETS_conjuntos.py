# São tipo de dados mutaveis em python, porem aceitam somente tipos de dados imutaveis como valor interno.

# sets são eficinetes em remover valores duplicados de iteraveis 
# seus valores serão sempre unicos 
# Não aceitam valores mutaveis
# não tem idexes
# Não garantem a ordem
# são iteraveis (for in, not in)

# # criando um set
# s1 = set() # set feito atravéz da classe set
# s1 ={'Andre', 1,2,3} # set com dados, feito sobre a estrutura de dados set
# s2 = {1,1,2,2,3,3,4,5} # verificamos que os dados repetidos são elimiandos
# print(s2)

# valores mutaveis não podem ser adicionados na função SET

# removendo valores duplicados de uma lista usanto o set (forma longa)
#l1 = [1,2,2,3,3,4,5,6,6,6,6,6,7,8,9,9]
#s3 = set(l1)
# convertendo novamente o resultado 
#l2 = list(s3)
#print(s3)
#print(l2)

# verificando item na lista de forma simples 
#print(3 in l1)

# criando uma função de verificaçã ode valores dentro de um set

# def busca_valor(a, b):
#     if a in b:
#         print('Existe!')
#     else:
#         print('Não existe!')
    

# busca_valor(0,l1)

# metodos uteis dentro do SET usados no dia a dia 
#  add, update, clear, discard

S1 = set()
# usando add, apenas um valor por vez
S1.add("André") # só podemos passar um valor por vez com o add
S1.add(2)

# usando o UPdate

#S1.update("ola mundo") # isso ficará iteravel no set mas queremos ele como frase e não como cada letra um iteravel 
S1.update(("ola mundo", "Pedro", 4, 63, 85,74)) # usado para enviar varios valores para fazer o update com masi valores dentro do set 

# Clear
#o metodo clear limpa o set 
#S1.clear() # limpa todo o set, deixa vazio 

# discard elimina um valor,  mesmo que n exitse o indece, nós eliminamos o proprio valor em si. 
S1.discard("ola mundo") # se tiver dois valores iguais e mantidos de formas diferentes os dois serão apagados

#print(S1)

#OPERAÇÕES MATEMATICAS COM SETS 

S2={1,2,3}
S3= {2,3,4}

# utilizando operadores 
#                 União
S4 = S2.union(S3) # podemos fazer de uam forma mais simples 
S5 = S2 | S3
print(S4)
print(S5)

# intersecção 
S6 = S2.intersection(S3)
S7 = S2 & S3
print(S6)
print(S7)

# diferença simetrica entre os SETS
# podemos elaborar um método para verificar a dirença de mutaç~eos em genes ou num genoma total
S8 = S2.difference(S3) # verificando a diferença somente da esquerda ou seja que ocorre somente em S2
S88 = S2 - S3
print(S8)
print(S88)

S9 = S2 ^ S3 # Realiza a diferença simetrica entre os dois sets, ou seja itens que não estão em ambos os sets 
print(S9)





