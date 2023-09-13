"""
CÓDIGO PROCEDURAL(EXECUTADO DA ESQUERDA PRA DIREITA, DECIMA PARA BAIXO)

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
'''
CALCULO DO SEGUNDO DIGITO DO CPF
CPF:746.824.890-70
cOLETE A SOMA DOS 9 PRIMEIROS DIGITOS DO CPF, MAIS O PRIMEIRO DIGITO,
MULTIPLICANDO CADA UM DOS VALORES POR UMA CONTAGEM REGRESSIVA COMEÇANDO EM 11
'''
import re # módul ode expressoes regulares
import sys


entrada_cpf = input("Digite o CPF:") # entrada de deados com CPF
#cpf_usuario = '087.661.686-43'.replace('.', '').replace(' ', '').replace('-', '')

#retirando tudo o que nao é numero de uma string ou listas com o re()
cpf_usuario = re.sub(
    r'[^0-9]', # na string encontrando tudo que não é um numero de 0 até 9
    '', # substituindo o que nao é numero para nada com aspas vazias
    entrada_cpf # da pra pedir o cpf para o usuario estando em qualquer formato. Podemos ver que na string tem varias letras e caracteres que são retirados pelo modulo re() deixando somente os numeros que serão utiizados
)

#Verificando se a entrada do cpf é sequencial para controle
entrada_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf) # tretorna um valor booleano

# se o usuario mandou o codigo aqui, ja matamos o codigo aqui e nao executamos o resto 
if entrada_sequencial:
    print('Você digitou um numero sequencial!')
    print('Encerrando programa!')
    sys.exit()
#---------capturando os 9 primeiros digitos e colocando em uma lista ---------
primeiros_nove_digitos = cpf_usuario[:9]

#-----------------------Fazendo o calculo de multiplicação e soma para os 9 primeiro digitos-----------------
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito_1 in primeiros_nove_digitos: # percorrendo os 9 digitos
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 # multiplicando pelo contador regressimo e somando iteraveis
    contador_regressivo_1-=1 # realinado o passo regressivo para a multiplicação
digito_1 = (resultado_digito_1*10)%11 # calculo do resto da divisão
#print('digitos multiplicados e somados: ', digito_1) # printando o resultado e realizando as ultimas operaçõe matematicas 

#-------------------Validando primeiro digito--------------------
# ----------------Usaremos condições ternárias-----------------
digito_1 = digito_1 if digito_1 <= 9 else 0
#print("o primeiro digito do cpf é", digito_1)

#-------- verificando o primeiro digito com if normal-----------------
# if digito_1 <= 9:
#     print("o primeiro digito do cpf é", digito_1)
# else:
#     print('O CPF não é válido')

#-------------------CALCULANDO O SEGUNDO DIGITO----------------------
dez_digitos = primeiros_nove_digitos + str(digito_1) # capturando os 10 digitos


#-----------------------Fazendo o calculo de multiplicação e soma para os 11 primeiro digitos-----------------
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito_2 in dez_digitos: # percorrendo os 9 digitos
    resultado_digito_2 += int(digito_2) * contador_regressivo_2 # multiplicando pelo contador regressimo e somando iteraveis
    contador_regressivo_2-=1 # realinado o passo regressivo para a multiplicação
digito_2 = (resultado_digito_2*10)%11
#print('digitos multiplicados e somados: ', digito_2) # printando o resultado e realizando as ultimas operaçõe matematicas 

#-------------------Validando segundo digito--------------------
# ----------------Usaremos condições ternárias-----------------
digito_2 = digito_2 if digito_2 <= 9 else 0
#print("o Segundo digito do cpf é", segundo_digito)

    
#print('Os dois digitos do cpf são: ', digito_1, digito_2)

#----------------validação do CPF----------------------------
cpf_calculado = f'{primeiros_nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == cpf_calculado:
    print(f'O CPF {cpf_usuario} é valido')
else:
    print('CPF inválido')
