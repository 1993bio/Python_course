'''
Variaveis:
são usadas para salvar valores dos dados na memoria do computador:
PEP8 (guias de estilos do python): Diz para iniciar as variaveis com letras minusculas, podendo usar numeros e underline _
O sinal de = é o operador de atribuiçã ode valroes a variaveis
'''
#Uso do PEP8: 
'''
ex: nome_variavel = expresão, valor, dado
o nome da variavel usando o underline é conhecido como snake_case.add()

Variaveis precisam ser descritivas autoexplicativo ao qual valor ela possui.

'''

# Exemplo de variáveis

nome_completo = 'André Luiz Caliari' # Atribuindo a string 'andré luiz calairi a variavel nome_completo
soma = 2+2
print(nome_completo) # podemos printar a variavel definida anteriormente e verificar o valor atribuido.
print(soma) # podemos printar o resultadode uma operação atribuida a varival soma

'''
variaveis ajudam a evitar repetições de valores, códigos (processos(operações))
vejamos um exemplo:
'''
# exemplo de código repetitivo com valores 1
'''
se eu precisar alterar o valor, eu precisaria alterar em mais de um lugar diferente, 
isso fica tedioso, e programação não funciona dessa forma. 
'''
print('------repetitivo sem variaveis-----')
print(int('1'), type(int('1'))) # convertendo str em int


# exempl ode código com variaveis
print('------resultado com uso de variaveis-----')

um = int('1') 
'''se eu precisar mudar os valores da variavel 
eu n preciso mudar em 5, 10 lugares diferentes,
e sim em apenas um lugar e atualizo todos os valor de uma só vez. 
'''
print(um, type(um)) # convertendo str em int


nome = 'André' # variavel que recebe uma string
idade = 29 # variavel que recebe um numero int ou quaqluer outro tipo de dados.
maior_de_idade = idade >= 18 # variavel que recebe uma operação matemática. 

# printando resultados das variaveis como exemplos:
print('Nome:', nome, ', Idade:', idade, )
print('É maior de idade?', maior_de_idade)
