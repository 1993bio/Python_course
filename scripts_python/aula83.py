# empacotamento e desenpacotamento de dicionários 

a, b = 1, 2 # passando valor para as variaveis 

a, b = b, a # isso muda a ordem das variaveis, sem ter que passar uma nova variavel

# geralmente quando fazemos um for nos dicionario e printamos o reultado ele entrega as chaves 

# pessoa = {
#     'nome': 'Pedo', 'sobrenome': 'Goto',
#     'nome': 'Andre', 'sobrenome': 'Caliari',
# }



# a, b = pessoa.values() # o desempacotamento de dict pode ser  feito dessa forma
# print(a, b)

# for chave, valor in pessoa.items():
#     print(chave, valor


# Dicionário 1
pessoa = {
    'nome': 'Pedo', 'sobrenome': 'Goto',
    'nome': 'Andre', 'sobrenome': 'Caliari',
}

# Dicionário 2

dados_pessoa={
    "idade": 16,
    "peso":60,
}

# para empacotar dicionários devemos estrair os dados ou seja as chaves e os valores para um outro dicionário vazio, da seguinte forma:

pessoa_completa = {**pessoa, **dados_pessoa} # desenpacotamento de um dicionário 

print(pessoa_completa)

# utilizando args (argumentos não nomeados) e Kwargs( argumentos não nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): # função que captura os valores de dicionários 
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(**pessoa_completa)

# Exempl ode configurações de uma função com kargs
configurações = {
    "arg1":1,
    "arg2":2,
    "arg3":3,
    "arg4":4,
    "arg5":5,
}

mostro_argumentos_nomeados(**configurações)
