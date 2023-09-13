'''
Repetições 
while  = enquanto
Executa uma ação enquanto uma condição for verdadeira

cuidado:
loop infinito => quando um código não tem a condição de parada, ele fica executando o laço até travar ou desligar o computador

break procura o laço masi proximo dela e para um possivel loop infinito 
'''

condicao = True

while condicao:
    nome = input("qual seu nome?")
    print(f"Seu nome é {nome}")

    if nome == 'sair':
        break
print('acabou')

