'''
Repetições 
while  = enquanto
Executa uma ação enquanto uma condição for verdadeira

cuidado:
loop infinito => quando um código não tem a condição de parada, ele fica executando o laço até travar ou desligar o computador

break procura o laço masi proximo dela e para um possivel loop infinito 

- Um outro mode de parar um loop infinito, é tornar a condição falsa em algum momento
vejamos:
'''
contador = 0


while contador <= 10:# Enquanto o contador for menor que 10 execute o bloco
    contador = contador  + 1 # o contador irá somar mais um nele mesmo reatribuindo a ele mesmo o novo valor que foi somado mais um, e quando chegar no numero 10 a condição será falsa e o loop sera encerrado.
    print(contador)



print('acabou')

