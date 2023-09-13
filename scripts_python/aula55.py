"""
Contornando a Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # esse modulo permite envolver numeros para realizar um procedimento de calculos preciso
# usado para numeros de ponto flutuante muito grande. 
# é necesario passar um string, a função usa a entrada como string e ele reconhece e faz a conversão pra numerico automaticamente.
# pode ser usado em operaç~eos de machine learn. 

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3) # 
print(f'{numero_3:.2f}') # formatar para 2 numeros dps da casa decimal
print(round(numero_3, 2)) # round pormove o arredondamento do numero passado o segundo argumento é o numero de casas decimais