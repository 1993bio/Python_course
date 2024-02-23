# criando uma lista com diferentes tipos de dados 
lista = ['André', 0.8, 1, True, [0, 1, 2], (4, 5, 6), {0,1},{'nome': 'Andre'}]

# criando de um jeito mais logico a verificação do tipo de dado na lista
# for i in lista:
#     print(i, type(i))

# Em python temos o isinstance para saber o objeto é de determinado tipo

for i in lista:
    if isinstance(i, set): # isso faz mostrar só o intem ou itens do tipo especificado no caso aq string
        print("SET")
        i.add(6) # o vscode ja identifica os metodos passado para cada tipo de dado por exemplo o add é domente de set
        print(i, isinstance(i, set)) #se um determinadi item da lista é uam string

    elif isinstance(i, str): 
        print('STR')
        print(i.upper())

    elif isinstance(i, (int, float)):
        print('NUM')
        print(i, i * 4)

    else:
        print("Outros") # mostra o tipo de dados que não satisfazem os critérios acima
        print(i)