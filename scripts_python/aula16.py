'''
cindiçoes e controle de fluxo
if, elif, else
se, se não se, se não
'''

entrada = input('Você quer "entrar" ou "sair": ')

if entrada == 'entrar': # if pode ser usado sozinho
    print('Você entrou no sistema')
elif entrada =='sair': # elif depende do if para ser executado
    print('Você saiu do sistema')
else: # else depende do if, e é sempre a ultima opção para encerrar um controle.
    print('Você não digitou nem entrar nem sair.')
    
'''
Sempre temos que criar uma condição para depois usar o elif e o else,
para controle do fluxo. E somente um dos blocos de verificação será executado (obloco verdadeiro)
'''