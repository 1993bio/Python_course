# São tipo de dados mutaveis em python, porem aceitam somente tipos de dados imutaveis como valor interno.

# # criando um set
# s1 = set() # set feito atravéz da classe set
# s1 ={'Andre', 1,2,3} # set com dados, feito sobre a estrutura de dados set
# s2 = {1,1,2,2,3,3,4,5} # verificamos que os dados repetidos são elimiandos
# print(s2)

# removendo valores duplicados de uma lista usanto o set (forma longa)
l1 = [1,2,2,3,3,4,5,6,6,6,6,6,7,8,9,9]
s3 = set(l1)
# convertendo novamente o resultado 
l2 = list(s3)
print(s3)
print(l2)





# removendo valores duplicados de uma lista usanto o set (forma curta)