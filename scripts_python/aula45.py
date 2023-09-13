'''
COMO O FOR FUNCIONA PRO BAIXO DOS PANOS
iterevael -> str, range, etc... (__iter__)--> metodo
iterador -> quem sabe entregar um valro por vez

next -> me entregue o proximo valor

iter -> me entregue seu iterador

'''

# A função iter() é a mesma coisa que o metodo __iter__ ( dois underline no python é chamado de "dunder")

texto_ex = iter("André") # iterável

# cada vez que eu executar o metodo __next_ ele busca o proximo iteravel
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

# mas tambem podemos usar a propria função next e teremos o mesmo resultado:
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))

#------------------------------------------------------------------------------------------

# for item in texto:
texto = "André" # iterável é a palavra ou texto que tem letras por indices
iterador = iter(texto) # iterator. quando eu solicito a função iter eu estou pedindo o método __iter__ de dentro do elemento iteravel (string)

# quando tentamos chamar o next no iterador ele chama o método __next__ dentro do iterador, e se tiver um proximo valor ele vai retornar o proximo valor,
# se não tiver ele gera um erro chamado stopInteration porque ele não encontrou nehum outro valor iteravel
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration: # geramos uma excessão do erro ou tratamento do erro quando não existir masi elementos iteraveis
        break # quando for True ou seja, não existir mais elementos iteraveis ele sair fora do laço e encerra o programa
print('------------')

# o mesmo acontece com o for, como visto abaixo:

for letra in texto:
    print(letra) 




