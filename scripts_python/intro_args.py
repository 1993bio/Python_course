# empacontamento e desempacontamento de funções com o uso de args
# ou seja, uso de multiplos argumentos sem retornar erro
# def soma (*args): # local que recebra multipos argumentos 
#     acumulador = 0 # varivale que recebera o valor acumulado da soma para fazer a soma com o proximo numero
#     for numero in args: # laço para iterar os multiplos argumentos 
#         print('total', acumulador, numero)
#         acumulador += numero # realizando a soma do numero anterior com o proximo numero 
#         print('Total', acumulador)
#     print(acumulador) # mostrando a soma de todos os valores



# def soma (*args): # local que recebra multipos argumentos 
#     acumulador = 0 # varivale que recebera o valor acumulado da soma para fazer a soma com o proximo numero
#     for numero in args: # laço para iterar os multiplos argumentos 
#         acumulador += numero # realizando a soma do numero anterior com o proximo numero 
#     return acumulador # mostrando a soma de todos os valores


# soma_1_ate_n = soma(1,2,3,4,5,6) # variavel recebe a função que retorna a soma de varios numeros 
# print(soma_1_ate_n) # printamos a variavel para mostrar o valor

# # exem0lo pronto do python
# print(sum((1,2,3,4,5,6))) # sum é a função pthon que realia a soma de varios iteraveis


# função que retorna a multiplicaçã ode varios numeros 

def mult(*args):
    total = 1
    for i in args:
        total = total * i
    return total


#numeros= 2,4,6,8,10 
res = mult(1,2,3,4,5)
print(res)

# função que verifica se um numero é par ou impar 
def par_impar(x):
    multiplo_de_dois = x % 2 == 0

    if multiplo_de_dois:
        return f'{x} é par'
    return f'{x} é impar'

print(par_impar(3))
print(par_impar(2))
print(par_impar(10))
print(par_impar(7))
print(par_impar(1))
