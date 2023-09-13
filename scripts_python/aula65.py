'''
Introdução a funções (def) em python)
Funções são trechos de códigos utilizados para replicar (não repetir) determinada ação ao longo do seu código
funções podem receber Valores para parâmetros (argumentos) e retornar um valor específco.
Por padrão, funções Python retornam None(nada)

Funções podem usar parâmetros para receber valores. 
Parâmetro é o nome da "variável" dentro dos parênteses, 
argumento é o valor passado para o parâmetro no momento da execução da função.
'''

# def Print(a, b, c): # definindo uma função (a,b,c) são parametros que vao receber valores
#     print('oi') # ação da função


# def imprimir(a, b, c): # os valroes dos parametros podem ser mudados e isso permite fazer coisas incriveis sem ter que reescrever codigo
#     print('Várias', a)
#     print('Várias', b)
#     print('Várias', c)
#     print(a,b,c)
    
# imprimir(1, 2, 3) # a ordem dos valores dos argumentos será a mesma definida na função 
    
def saudacao(nome): # definindo uma dunção
    print(f'Bom dia {nome}!') # ação da função
    
saudacao('Andre') # chamando a função passando o valro do argumento com 'Andre'


def saudacao(nome='Sem nome'): # argumento com valor padrão para replicar a função sem argumentos em uma chamada
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
    
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)