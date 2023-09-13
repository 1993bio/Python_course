a = 'AAA'

b = 'BBB'

c = 1.1
#podemos utilizar os indices dos argumentos e passalos para a chave de formatação. neste caso eu não dependo da ordem dos argumentos dentro do format()
string = 'a={0} b={1} c={2:.2f}' # variavel de string, com chamada de argumentos
string2 =  'b={1} b={1} b={1} c={2:.2f} c={2:.2f} a={0} a={0} a={0}' # usando a formatação pelo indice dos argumentos da formatação, no entando preciso passar o indice de todos argumentos

formato = string.format(a, b, c) # varival com valor de outra variavel formatando uam string
formato2 = string2.format(a, b, c) # varival com valor de outra variavel formatando uam string

print(formato) # printando uma variavel. 
print(formato2) # printando uma variavel. 
