'''
Flag = Bandeira - marcar um local

None = Não valor 

is e is not =  é ou não é (tipo, valor, identidade)

id = Identidade
'''

'''
v1 = 'a'
v2 = 'b'

# id faz o python monstrar onde ele buscou o elemento na memória do computador
print(id(v1)) # ver a identidade de um elemento alocado na mémoria do computador
print(id(v2)) # ver a identidade de um elemento alocado na mémoria do computador
'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')