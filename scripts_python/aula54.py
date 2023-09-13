'''
Exercicio: fazer uma lista de comprar com listas.

O usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista.

Não permita que o programa quebre com erros de indices inexistentes na lista

'''
import os

Lista_de_compras = []


while True: # Enquanto for verdadeiro execute o código abaixo
    print('selecione uma opção:' )
    opcao = input('[i]nserir [a]pagar [l]istar  [s]air:').lower() # entrada de opções a escolher
    
    # ----------------------adicionando itens a lista------------------- 
    if opcao == 'i':
        os.system('cls')
        valor = input('digite um produto: ')
        Lista_de_compras.append(valor)    
        #-----------------------apagando items da lista--------------------
    elif opcao == 'a':
        indice_str = input('escolha um indice para apagar:') # entrada do indice que deseja excluir
        try:
            indice = int(indice_str) # a entrada é uma string e precisamos converter para passar o indice em int para a função pop(indice int)
            del Lista_de_compras[indice]
        except ValueError: # tratando um erro com excessão com uma valor digitado errado
            print('Por favor digite um numero int.')
        except IndexError: # tratando err ode apagar indice que nao existe
            print('Não foi possivel apagar o item, valor inexistente!')
        except Exception:
            print('Erro descohecido!')
        #--------------------listando os produtos
    elif opcao == 'l':
        os.system('cls')
        
        if len(Lista_de_compras) == 0:
            print('Nada para listar')
        # criando uma lista enumerada
        for indice, valor in enumerate(Lista_de_compras):
            print(indice, valor)         
        # se esiver vazio pedir para que digite uma opção
    elif opcao == '':
        print('Escolha uma opção para continuar')
    elif opcao == 's':
        break
    else:
        ('digite uma opção correta i, a ou lç')

print('você saiu!')