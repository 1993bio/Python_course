'''
Exercicio de operadores de comparação
'''

primeiro_valor = input('digite um valor: ')

segundo_valor = input('digite um segundo valor: ')

if primeiro_valor == segundo_valor:
    print(f' O primeiro valor {primeiro_valor} é igual que o segundo valor {segundo_valor}')
elif primeiro_valor > segundo_valor:
    print(f' O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f' O segundo valor {segundo_valor} é maior que primeiro valor {primeiro_valor}')
else:
    print('Digite um valor valido')
