'''
operadores logicos and (e), or (ou), not (não)

and: todas as condições precisam ser verdadeiras. 

se qualquer valro for considerado falso, 
a expressão inteira será avaliada naquele valor,
São considerados falsy. ex: 0 , 0.0 , '' , False

Tambem existe o tipo None que é usado para representar um Não valor. (geralmente usado como valor de argumentos)

'''

# chegando o passe de entrada e senha do usuario 

#entrada = input('[E]ntrar [S]air: ') # passe de entrada
#senha = input('Senha:') # senha passada de login

#senha_permitida_BD = '1234' # senha cadastrada (geralmente guardada em um banco de dados)

# criando checagens para acesso a um "sistema"
# if só é executado quando toda expressão for True
'''
if entrada == 'E' and senha == senha_permitida_BD:
    print('Você entrou no Sistema')
else:
    print('você escolheu sair.')

'''
# avaliação de curto circuito 
# basta uma condição ser falsa para toda a expressã oser avalaida como falsa!

print(True and True and False) #se uma das condiçoes for false toda condição se torna falsa
print(True and 0 and True) #se uma das condiçoes for false toda condição se torna falsa
print(False and True and False) #se uma das condiçoes for verdadeira toda condição se torna falsa
print(True and True and True) #se uma das condiçoes for verdadeira toda condição se torna falsa


