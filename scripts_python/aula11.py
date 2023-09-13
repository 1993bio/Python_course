'''
Precedecia de operadores aritméticos
'''
# 1. (n + n) primeiro é resolvido o que dentro do parenteses, dos mais internos para os mais externos
# mesmo que a ordem de precendencia nao seja a primeira.
# 2. **
# 3. *, /, //,  %
# 4. +, -

# seguindo a ordem de precendencia resolvemos a conta 1
 
conta_1 = 1 + 1 ** 5 + 5  # resultado 7
print(conta_1)

conta_2 = 1 ** 5 #  resultado 1
print(conta_2)

conta_3 = 1 + 1 + 5  # resultado 7
print(conta_3)

# das esquerda para adireita nós resolvemos o calculo dentros dos parenteses
conta_4 = ((1 + int(0.5+0.5)) ** (5 + 5))  # resultado é 1024, resolvemso os parenteses mais internos e deposi os mais externos
print(conta_4)
