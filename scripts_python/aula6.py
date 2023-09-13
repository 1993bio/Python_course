'''
Conversão de tipos
    coerção, type convertion, typecasting, coercion.
 É o ato de converter um tipo em outro
 Tipos imutaveis e primitivos são: (str, int, float, bool).
 
'''
print(1+1) # o python soma os numeros 

print('a'+'b') # o python concatena as strings

#print('1'+ 1) # retorna o erro (can only concatenate str (not "int") to str). 
# ou seja o python nao pode concatenar uma string com um numero.
# por exemplo no java script que é uma linguagem tipada como dinamica e fraca ele conert altomaticamente e faz a operação.

'''
como o python é tipado como dinamico e forte, 
existem funções para que possamos fazer a conversão entre tipos de dados. 
'''
# Exemplo
'''
Ao usarmos a função int() antes do dado caso for uma string "1", 
nos estamos convertendo de string para o numero (1) do tipo (int)
'''
print(int('1'), type(int('1'))) # convertendo str em int

'''
Podemos ver que abaixo temos um numero do tipo int dentro do print,
e seu tipo será convertido em string
'''
print(str(1), type(str(1))) # convertendo int em str

print(str(11) + 'b') # convertendo  e somando string em str

'''
Abaixo eu utilizei uma conversão de um numero do tipo int, para 
um dado do tipo boleano retornanto true ou false
'''

print(bool(1), type(bool(1))) # convertendo int para booleano, 1 retorna true
print(bool(0), type(bool(0))) # convertendo int para booleano, 0 retorna false

'''
o mesmo vale para converter string para booleanos
'''
print(bool('A'), type(bool('A'))) # convertendo int para booleano, 0 retorna false



print(int('1')+ 1) # converte string em numero e realiza a operação de soma.

print(type(float('5')+ 5)) # converte string em numero flutuante e realizando a operação de soma.
# a soma de um float e um inteiro retorna um float.








