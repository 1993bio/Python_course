"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5) # utilize todos argumentos nomeados ou não nomeados para um melhor entendimentos
# quando nomeamos um argumento podemos usar ele em qualquer ordem desde que indiquemos seus nomes ou keys
print(1, 2, 3, sep='-')