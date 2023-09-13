'''
Exercicio com fatiamento de estring e logica condicional if
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome != '' and idade != '': # checando se o usuario passou ou não dados de entrada
    print(f'seu nome é {nome}')

    nome_invertido = nome[::-1]

    print(f'Seu nome invertido é {nome_invertido}')

    primeira_letra_nome = nome[0] # primeiro caractere da string
    print(f'primeira letra do nome é {primeira_letra_nome}')

    ultima_letra_nome = nome[-1] # ultimo caractere da string
    print(f'ultima letra do nome é {ultima_letra_nome}')
    
    tamanho_string = len(nome)
    print(f'Seu nome tem {tamanho_string} letras')
    
    if ' ' in nome: # verificando se existe espaços vazios na string nome do usuário
        print('Seu nome TEM espaços vazios')
    else:
        print('Seu nome NAO tem espaços vazios')
    
else:
    print("Desculpe você deixou campos vazios")