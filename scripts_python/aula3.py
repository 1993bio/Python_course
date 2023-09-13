# tipos de dados em python

'''
python = linguagem de programação.
Tipo de tipagem = Dinamica / Forte.
str -> string = texto
    Strings são textos que estão dentro de aspas. 
    ex: "Eu sou uma string de texto em python". 
    
'''

# aspas simples
print('Eu sou uma sdtring de texto')

# Aspas Duplas
print("Sou outra string de texto")

# Escape
print("André \"Luiz\" ") 
'''
a barra invertida é um escape, indica para o interpretador pular a aspas depois da barra
e continuar a leitura da string até encontrar as aspas de fechamento.
'''

#r
print(r"André \"Luiz\" ") # geralmente é usado para expressoe regulares.

#-------------Normalmente------------ podemos:---------------
# o mesmo efeito pode ser conseguido fazendo:

print(1,'André "Luiz" ') # as duplas dentro de aspas simples pode ser usado sem problemas.
print(2,"André 'Luiz' ") # as simples dentro de aspas duplas pode ser usado sem problemas.
    

