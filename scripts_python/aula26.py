''' formatação básica de string 
s - string
d - int
f - float

.<numero de digitos>f

x ou X HEXADECIMAL
(caractere)(><^)(quantidade)

> - esquerda
< - direita
^ - centro
= - Força o numero a aparecer antes dos zeros

sinal - + ou -

ex: 0>-100,.1f

conversion flags - !r !s !a
'''

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel:_>10}') # adicionado underline a esquerda da string 
print(f'{variavel:-<10}.') # adicionando underline a direita da string
print(f'{variavel:_^10}.') # colocando a string ao centro e adicionando underline a direita e a esquerda da string. 

print(f'{1546.8546321:0=+10,.1f}') # deixando o numero apenas com uma casa decimal (existem bibliotecas para isso)

print(f'o Hexadecimal de 1500 é {1500:08x}')

