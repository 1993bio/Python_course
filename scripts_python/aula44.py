'''

No for não precisamos nos preocupar com o indice para iterar sobre uma string
for + range
                inicio, até, passo 
range ---> range(start, stop, step)
o passo funciona como multiplos de um numero, ou saber os numeros parede quando utilizado passo 2
'''

# criando um contador com o for 

numeros = range(0, 10, 2) # criando numeros de 0 a 10 pulando de 2 em 2
#numeros__ = range(-10, 0, 2) # criando numeros de 0 a 10 pulando de 2 em 2
#numeros__ = range(0, -10, -2) # criando numeros de 0 a 10 pulando de 2 em 2

for numero in numeros:
    print(numero)
