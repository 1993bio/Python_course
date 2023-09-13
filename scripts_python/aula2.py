# \r \n faz a quebra de linha no windows mas podemos usar somente a \n.  --> CRLF do windows
# \n LF em sinstemas baseados em linux.


print(12, 34, sep=', ', end='\r\n') # printa 12,34 separado por , e um espaço, end é o tip ode quebra de linha
print(56, 78, sep='; ', end='\n') # printa 56; 78 separado por ; e um espaço, end é o tip ode quebra de linha
print(9, 10, sep='-') # printa 56; 78 separado por - sem espaço entre numeros

'''
OBS: separadores por espaço simples (sep= ' ') e quebra de linhas (end= '\n') são os padrões,
no interpretador vs code no windows. 
'''