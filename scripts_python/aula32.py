"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# programa que verifica se um nuemro é par ou impar
print('--------------------- PAR ou Impar ---------------------')

entrada = input('Digite um numero: ' ) # entrando com o numero (str)
'''
if entrada.isdigit(): # esse bloco retorna impar 
    entrada_int = int(entrada)# fazendo a coerção de str para int 
    par_impar = entrada_int % 2 == 0  # verificando se a entrada é um numero par ou impar (resto da divisão tem que ser 0)
    par_impar_txt = 'impar'
    
    if par_impar: # esse retorna par no print de saída
        par_impar_txt = 'par'
    
    print(f'O numero {entrada} é {par_impar_txt}')
else:
    print('Você não digitou um numero inteiro')
'''   
# outro modo de checar se um numero é par o impar

try:
    entrada_int = float(entrada)# fazendo a coerção de str para int 
    par_impar = entrada_int % 2 == 0  # verificando se a entrada é um numero par ou impar (resto da divisão tem que ser 0)
    par_impar_txt = 'impar'
    
    if par_impar: # esse retorna par no print de saída
        par_impar_txt = 'par'
    
    print(f'O numero {entrada} é {par_impar_txt}')
except:
    print('Você não digitou um numero inteiro')
        
print('--------------------------------------------------------')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('--------------------Que Horas São ----------------------')

hora_x = input('Que Horas são em numeros inteiros:? ') # entrando com o numero (str)

try:
    hora_x = int(hora_x) # atualizando o valor de Hora_x para numero inteiro

    manha = hora_x >= 0 and hora_x <= 11 # verificando o espaço de horas da manha
    tarde = hora_x >= 12 and hora_x <= 17 # verificando o espaço de horas da tarde
    noite = hora_x >= 18 and hora_x < 24 # verificando o espaço de horas da noite

    if manha:
        print(f'bom dia, agora são: {hora_x} horas')
    elif tarde:
        print(f'Boa tarde, agora são: {hora_x} horas')
    elif noite:
        print(f'Boa noite, agora são: {hora_x} horas')
    else:
        print('Não conheço essa hora.')
except:
    print('Por favor digite um numero inteiro')
print('---------------------------------------------------------------')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print('----------------TAMANHO DO NOME-------------------------------------')

nome = input('qual seu nome:? ') # entrando com o nome (str)

tamanho_nome = len(nome)

curto = tamanho_nome >= 1 and tamanho_nome <=4
normal = tamanho_nome >= 5 and tamanho_nome <= 6
grande = tamanho_nome > 6

if curto:
    print(f'Seu nome tem {tamanho_nome} letras, é um nome curto')
elif normal:
    print(f'Seu nome tem {tamanho_nome} letras, é um nome de tamanho normal')
elif grande:
    print(f'Seu nome tem {tamanho_nome} letras, é um nome muito grande')
else:
    print("Digite pelo menos uma letra")



