'''
interpolação basica de string com (%)
s - string
 d e i - int
 f - float
 x e X - hexadecimal (ABCDEF0123456789)
'''



'''
usamos dentro da string o caractere % seguido do item que queremos
(s) para string, (f) para float ou (i) para int
apos o fechamento das aspas devemos indicar na ordem as variáveis
que contem os valores que queremos por exe: %(x,y,z)
%.2f usamos para pegar apenas 2 casas decimais depois do ponto separador.

'''
nome = 'André'

preco = 100.08547532

variavel = '%s, o preço é R$ %.2f' %(nome, preco) 

print(variavel)


print('o Hexadecimal de %d é %04x' %(1504 , 1504)) # %d se refere ao numero inteiro 15, e %04x o seu exadecimal de 4 digitos. 
