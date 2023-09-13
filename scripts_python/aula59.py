'''
operações ternarias (condicional de uma linha)
<valor> if <condiçaõ> else <outro valor>
'''
#   variavel é igual a (valor) se verdadeiro, se não ela recebe (outro valor)

# condicao = 10 ==11 # condição para operações ternarias
# variavel = 'valor' if condicao else 'outro valor' # operaçã oternaria em apenas uma linha
# print(variavel)

digito = 10 # se <= 9 a variavel recebe 9 se for maior que 9 a variavel recebe 0

novo_digito = digito if digito <= 9 else 0
# condição invertida
novo_digito_ = 0 if digito > 9 else digito


print(novo_digito)
print(novo_digito_)