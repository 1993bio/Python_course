'''
cindiçoes e controle de fluxo
if, elif, else
se, se não se, se não
'''

condicao1 = False
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('codigo condição 1')
elif condicao2:
    print('código condição 2')
elif condicao3:
    print('código condição 3')
elif condicao4:
    print('código condição 4')
else: 
    print('Nenhuma condição foi satisfeita')


if 10 == 10:
    print('bloco do segundo if')
    
    
print('fora do bloco if')


    
'''
Sempre temos que criar uma condição para depois usar o elif e o else,
para controle do fluxo. E somente um dos blocos de verificação será executado (obloco verdadeiro)

ao existir masi de uma condição verdadeira ele ira executar somente a primeira e seguira o código adiante. 
'''