# lista iteravel
l1 = [1,2,2,3,3,4,5,6,6,6,6,6,7,8,9,9]


# criando uma função de verificaçã ode valores dentro de uma lista de forma muito simples
# pode ser aplicado em uma string para verificaçã ode padrões 

def busca_valor(a, b):
    if a in b:
        print('Existe!')
    else:
        print('Não existe!')
    

busca_valor(0,l1)