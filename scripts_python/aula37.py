'''
Repetições While
Executando uma ação até que uma condição seja verdadeira
Usando o continue => termina o laço, quando o laço bater no continue ele volta a executar o laço naquele momento deixando de executar o restante do código
'''

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('não vou mostar o 6')
        continue    
    
    if contador >=10 and contador <=29:
        print('pulei o', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break