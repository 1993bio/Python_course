'''
Criando um gerador de CPF validos

você pode colcoar todo esse codigo dentro de um for 
e gerar 100, 1000, 1000 cpf de uma só vez

'''

import random
#---------criando os 9 primeiros digitos para gerar cpf ---------
#criamos numeros aleatorios para gerar 9 digitos mas pode ser enviado tbm pelo usuario
#gerando 100 cpfs de uma só vex
for _ in range(100): 
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    #-----------------------Fazendo o calculo de multiplicação e soma para os 9 primeiro digitos-----------------
    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for digito_1 in nove_digitos: # percorrendo os 9 digitos
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
    dez_digitos = nove_digitos + str(digito_1) # capturando os 10 digitos


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
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    print('CPF Gerado: ',cpf_gerado)