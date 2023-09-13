"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

o modulo os do python permite que eu limpe o terminal, mas precisamos importar ele da linguagem (import os)
"""
import os


palavra_secreta_BD = 'andre' # deve estar fora do while por cada vez que encerrar o while a palavra sera zerada da memoria e as condições nao vão conseguir reconehecr a palavra porque ela n mais irá existir

letras_acertadas = ''

numero_de_tentativas = 0 # variavel que guarda o numero de tentativas

while True: # Enquanto for verdadeiro execute o código abaixo
    
#---------------VALIDAÇÃO DAS PALAVRAS DO JOGO------------------------------------------------------------------------------------------------------------------

    letra_digitada = input('Digite uma letra: ') # entrada do primeiro numero
    numero_de_tentativas += 1 # contagem do numerode tentativas ao entrar no laço novamente quando o usuario errar
    
    if len(letra_digitada) > 1: # Verificando se o usuario usou apenas uma letra e retornamos ao inicio
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta_BD: # se a letra digitada não estiver na palavra secreta faça o retorno ao inicio do códifo e inicia o while novamente
        print('A letra digitada faz parte da palavra secreta!')
        letras_acertadas += letra_digitada # atualizando a variavel com a letra que contém na palavra secreta
    else:
        print("A letra não faz parte da palavra secreta! ") # se a letra nao fizer parte da palavra secreta
        continue
    
    # para cada letra acertada da palavra secreta adicionamos a letra acertada
    # nos asteriscos para mostrar as letras que o usuario ja acertou
    palavra_formada = ''
    for letra_secreta in palavra_secreta_BD: 
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            continue
    print('Palavra_formada:', palavra_formada)
    
    
    continuar = input('quer tentar acertar a palavra toda? [s]im: ').lower().startswith('s')
    
    if continuar is not True:
        print('Saindo do jogo...') 
        letras_acertadas = '' # zerando a variavel se o usuario sair
        numero_de_tentativas = 0 # zerando a variavel se o usuario sair
        break
    else:
        palavra_inteira = input ("digite a palavra inteira e tente acertar: ")    
    
    if palavra_inteira == palavra_secreta_BD:
        
        os.system('cls') #limpando o terminal cada vez que o usuário ganhar o jogo
        
        print('PARABENS VOCÊ GANHOU!')
        print(f'Você acertou a palavra secreta "{palavra_secreta_BD}" na {numero_de_tentativas}º tentativa.')
        
        letras_acertadas = '' # zerando a variavel se o usuario sair
        numero_de_tentativas = 0 # zerando a variavel se o usuario sair
        print('Saindo do jogo...')
        break        
    else:
        print("que pena não foi dessa vez!")
        letras_acertadas = '' # zerando a variavel se o usuario sair
        numero_de_tentativas = 0 # zerando a variavel se o usuario sair
        nova_rodada = input('quer tentar tentar novamente? [s]im: ').lower().startswith('s')
    
    
    if nova_rodada is not True:
        print('Saindo do jogo...')
        letras_acertadas = '' # zerando a variavel se o usuario sair
        numero_de_tentativas = 0 # zerando a variavel se o usuario sair
        break
    else:
        continue
        
    
        
