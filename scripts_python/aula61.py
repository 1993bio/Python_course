"""
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

cpf = input("Digite o CPF:")


lista_cpf = [] # variavel que vai receber os items no formato str de cpf
lista_int_cpf = [] # variavel que vai receber os itens no formato int de lista cpf
primeiros_nove_digitos = []
dois_ultimos_digitos = []
contador_regressivo_1 = 10

# retirando a string da variavel cpf e criando uma lista em lista_cpf
for i in cpf:
    lista_cpf.append(i)
    
#convertendo  os iteraveis do tipo str de lista_pfc para int
for i in lista_cpf:
    lista_int_cpf.append(int(i))
    
#print('todos os digitos: ',lista_int_cpf) # mostra todos os digitos

#---------capturando os 9 primeiros digitos e colocando em uma lista ---------
for i in range(0,len(lista_int_cpf)-2):
    primeiros_nove_digitos.append(lista_int_cpf[i])
    
#print('Nove digitos: ', primeiros_nove_digitos) # mostra apenas os 9 primeiros digitos

#-----------capturando os 2 ultimos digitos e colocando em uma lista------------
for i in range(9,len(lista_int_cpf)): # lendo os 2 ultimos digitos
    dois_ultimos_digitos.append(lista_int_cpf[i]) # colocando os dois ultimso digitos na lista de 2 digitos
    
#print('Dois ultimos digitos: ',dois_ultimos_digitos) # mostra os dois ultimos digitos

#-----------------------Fazendo o calculo de multiplicação e soma para os 9 primeiro digitos-----------------
resultado_digito_1 = 0
for digito_1 in primeiros_nove_digitos: # percorrendo os 9 digitos
    resultado_digito_1 += (digito_1 * contador_regressivo_1) # multiplicando pelo contador regressimo e somando iteraveis
    contador_regressivo_1-=1 # realinado o passo regressivo para a multiplicação
primeiro_digito = (resultado_digito_1*10)%11
#print('digitos multiplicados e somados: ', primeiro_digito) # printando o resultado e realizando as ultimas operaçõe matematicas 

#-------------------Validando primeiro digito--------------------
# ----------------Usaremos condições ternárias-----------------
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print("o primeiro digito do cpf é", primeiro_digito)

#-------- verificando o primeiro digito com if normal-----------------
if primeiro_digito <= 9:
    print("o primeiro digito do cpf é", primeiro_digito)
else:
    print('O CPF não é válido')