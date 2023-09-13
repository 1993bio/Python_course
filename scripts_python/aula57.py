'''
Listas de listas e seus indices
'''

salas = [
    #  0         1
    ['Maria', 'Helena'], # 0
    #  0         1        2
    ['André', 'Pedro', 'Anthony'], # 1
    #  0        1      
    ['Ana', 'Vera' ], # 2
] #(0,10,20,30,40)
#acessando os valores de lista dentro de listas
#buscando Anthony
# print(salas[1][2]) # primeira chave acessa a lista 1 em salas, a segunda chave acessa o item dentro da lista 1
# buscando Vera
# print(salas[2][1]) # primeira chave acessa a lista escokhida em salas no caso lista 0 dentro de salas
#buscando maria
# print(salas[0][0]) # primeira chave acessa a lista escokhida em salas no caso lista 0 dentro de salas
# #buscando Andre
# print(salas[1][0]) # primeira chave acessa a lista escokhida em salas no caso lista 0 dentro de salas

#acessando o valor 20 dentro da tupla
# print(salas[2][2][2]) #primeira chave escolha da lista que tem a tupla, segunda chave acessa a tupla dentro da lista 2, e ultima chave acesssa o item dentro da tupla

for sala in salas: # iterando cada lista
    print(f'Asala é: {sala}') #printa as listas acessadas
    for aluno in sala: #iterando cada valor dentro de cada lista
        print(aluno) #printa os alunos acessados