#print(...) # place holder python se vc nao tem codigo pode usar para n gerar erros

nome = "André Luiz Caliari"

altura = 1.80

peso = 70

# imc = peso/altura^2
imc =  peso / altura**2


print(f'{nome} tem {altura:.2f} de altura, e pesa {peso} quilos, e seu imc é: {imc:.2f}')

# ou podemos colocar o texto em uma variavel e formatar o texto e deposis printar a variável.
linha_1 = f'{nome} tem {altura:.2f} de altura, \nPesa {peso} quilos, \nE seu imc é: {imc:.2f}'
print(linha_1)