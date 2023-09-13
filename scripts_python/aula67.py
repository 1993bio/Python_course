"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
refatorar = editar o seu código
obs: um código numca esta pronto totalmente, ele sempre pode melhorar 
"""


def soma(x, y, z=0): # sempre que tivermos um parametro com um valor padrão, todos os outros parametros que vierem após, precisam ter valores atribuidos  
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2, 3)
soma(1, y=2, z=5)
soma(100,200)

print(1, 2, 3, sep='-')