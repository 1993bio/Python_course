'''
O imput permite gravar dados em uma variavel,
e deposi coletar eses dados para outros processos 
'''

'''
toda entrada de dados em input, será uma istring, mesmo que passe um numero,
Dai temos vemos a importancia de conversão de tipos de dados.
'''

#podemos ver que passando um numero ele grava como string (aqui ele vai concatenar os valores)
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# ao passar a função de conversão int() para a funçã input obtemos o tipo de dados que queremos para realizar a operação com sucesso
# no entando se o usuario passar um valro (A) o programa quebra e n faz masi nada.
#assim o método mais prudente seria uma chegagem dos valores passados cujo tipo seria definido, e quando outro dado for passado o programam pede ao usuario o dado no formato correto
numero_3 = (int(input('Digite um número: '))) # aqui no input ja acontece a conversão do tipo de str para numero do tipo int
numero_4 = (int(input('Digite outro número: '))) # aqui no input ja acontece a conversão do tipo de str para numero do tipo int

print(f'A soma dos números do tipo str é: {numero_1 + numero_2}')
print(f'A soma dos números com int é: {numero_3 + numero_4}')

#----------------------------OU-------------------
'''
aqui eu não passo a conversão diretamente no input,
mas sim exrevo uma variavel para recebebr o input e passo a conversão de tipo na variavel,
isso me permite realizar varias operações, inclusive chegar o tipo de dados e fazer a
operaç~ode soma sem ser do tipo string.

'''
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
