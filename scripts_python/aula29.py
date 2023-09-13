'''
introdução ao try/except

try -> tentar executar o código

except -> ocorreu algum erro ao tentar executar
'''
'''
print(1234) # o python le normalmente
print(4567) # continua lendo normalmente 
int('a') # não convertemos string em inteiro, aqui tem um erro pq passou um inteiro e estamos lendo uma string, a leitura do interpretador para aqui

'''
#aqui ao digitar um numero ele será tranformada=o em string e precisamos fazer a coerção de tipos para int ou float antes de fazer qualquer operação matematica
numero = input("Digite um numero para dobrar o seu valor: ")

'''
if numero.isdigit():
    
    num_float = float(numero)# tipe coercion para fazer a operaçõ corretamente
    print(f' O dobro de {numero} é {num_float*2}')
else:
    print("Você não digitou um número")
'''


# se ocorrer um erro dentro do try pule imediatamente para o except (fail fast)
try:
    print('str: ', numero) # le corretamente 
    num_float = float(numero)# ERRO acorre aqui, mas pula para o except, tipe coercion para fazer a operaçõ corretamente
    print('float:', num_float)
    print(f'O dobro de {numero} é {num_float*2}')
except:
    print("Você não digitou um número")


