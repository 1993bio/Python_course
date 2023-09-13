'''
Fatiamento de string
 012345678
 olá mundo
-987654321

Fatiamento [i:f:p][::], i = inicio, f = fim, p = passo, 
se omitir o fim ele percorre até o fim da string, 
se precisar ser especififico é necessario colocar o indice do caractere.
Se omitir o inicio da string, o python sabe que eu quero começar do inicio da string
e varrer até o indice final especificado.

OBS: a função len retorna a quantidade de caracteres dentro da string.
strings são iteraveis, ou seja, possa andar item por item em uma string. 

'''

variavel = 'Olá Mundo'
print(len(variavel)) # len verifica o tamanho da variavel

print(len(variavel[0:4])) # fatiando a strind o indice 0 a 4 = 'Olá M'

print(variavel[::-1]) # invertendo uma string, se passar o passo negativo e omitindo inicio e fim ele inverte a string. 

print(variavel[0:len(variavel):3]) # percorrendo a string com passo, por padrão o passo é 1.
