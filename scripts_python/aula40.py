'''
Calculadora com o while
'''

while True: # Enquanto for verdadeiro execute o código abaixo
    
#-----------------------------INICIO E VALIDAÇÃO DOS DADOS DE ENTRADA------------------------------------------------------------------------------------------------------------------

    numero_1= input('Digite um numero: ') # entrada do primeiro numero
    numero_2= input('Digite outro numero: ') # entrada do segundo numero
    operador = input('Digite um operador (+ - / *): ') #escolha do operador para realizar o calculo
    
    Numeros_validos = None # flag para verificação da coerção str -> flaot
    
    try: # tente conveter as instrings para float
        numero_1_float = float(numero_1) # convertendo a strigg 1 em float
        numero__float2 = float(numero_2) # convertendo a string 2 em float
        Numeros_validos = True # atualizando a variavel para saber se deu certo a coerção de valores das entradas
    except: # caso os numeros continue invalidos 
        Numeros_validos = None # a flag é atualizada para None e geramos uma correção
    
    if Numeros_validos is None: # casos o usuario digitou algum nuemro errado  e a flag ter valor None, retornará ao inicio do código
        print('Um ou ambos os numeros digitados são invalidos.')
        continue # se ouver valroes invalidos continue volta ao inicio do while e pede novas entradas corretas para o primeiro numero e segundo numero
    
    operadores_permitidos = '+ - / *' # variavel que permite verificar os operados digitados 
    
    if operador not in operadores_permitidos: # se o operador digitado nao estiver entre os operadores permitidos faça o retorno ao inicio do códifo e inicia o while novamente
        print('operador digitado inválido')
        
    if len(operador) > 1: # se o usuario digitar mais de um operador na entrada isso não será permitido e o continue sera executado retornando ao inicio do código
        print('digite apenas um operador!')
        continue
        
#-----------------------------------INICIO DOS CALCULOS-------------------------------------------------------------------------------------------------------------------------------
    if operador == '+':
        res = numero_1_float + numero__float2
        txt = f'{numero_1_float} + {numero__float2} '
        print(f'{txt} = {res}')
    
    elif operador == '-':
        res = numero_1_float - numero__float2
        txt = f'{numero_1_float} - {numero__float2} '
        print(f'{txt} = {res}')
    
    elif operador == '/':
        res = numero_1_float / numero__float2
        txt = f'{numero_1_float} / {numero__float2} '
        print(f'{txt} = {res}')
    
    elif operador == '*':
        res = numero_1_float * numero__float2
        txt = f'{numero_1_float} x {numero__float2} '
        print(f'{txt} = {res}')
    
    else:
        ('Numca deveria ter chegado aqui!')
        
#---------------------------SAIR DEPOIS QUE EXECUTAR OS CODIGOS----------------------------------------------------------------------------------------------------------------------
    sair = input('quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
