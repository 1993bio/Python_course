'''
split e join com list e str

split -> divide uma string

join -> une uma string
'''

frase = '  Olha essa string,   como é grande   ' # string com muitos espaços (ruim)
lista_de_palavras_cruas = frase.split(', ') # partindo a string nos espaços, é possivel quebrar especificando onde por exemplo uma virgula com ose segue o exemplo
lista_frase = []

# alterando e modificando a lista
for i, frase in enumerate(lista_de_palavras_cruas):
    lista_frase.append(lista_de_palavras_cruas[i]. strip()) # strip é um metodo que permite tirar espaços entre string presente em uma lista mutavel

#print(lista_de_palavras_cruas) # lista gerada com cada partição da frase
#print(lista_frase) # nova frase corrigida

frases_unidas = '-'.join(lista_frase)# o separador '-' é aplicado ao iteravel e o join une o iteravel ao separador
print(frases_unidas)