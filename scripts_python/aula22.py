'''
Na consição OR qualquer condição avalaida como
verdadeira toda expressão será verdadeira mesmo que existam condições false.
'''


#entrada = input('[E]ntrar [S]air: ') # passe de entrada
#senha = input('Senha:') # senha passada de login

#senha_permitida_BD = '1234' # senha cadastrada (geralmente guardada em um banco de dados)

# criando checagens para acesso a um "sistema"
# if só é executado quando toda expressão for True

# aqui permitimos "E" (ou) 'e' para avalair a condição  de entrada.
# o que ta entro do parenteses é avalaido somente como uma condição.
'''
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida_BD:
    print('Você entrou no Sistema')
else:
    print('você escolheu sair.')
    
'''
#avaliaçã ode curto circuito:

'''
Se qualque expressão for considerado como verdadeiro,
a expressão interira será avaliada naquele valor (somente condição OR)
'''
senha = input('Senha: ') or 'Sem senha'
print(senha)


#print(True or False or False) # se um valor de condição for considerado verdadeiro toda expressão será verdadeira.
#print(False or False or False or 'abc') # qualquer valor dentro de '' é verdadeiro, e se um valor de condição for considerado verdadeiro toda expressão será verdadeira.
    

