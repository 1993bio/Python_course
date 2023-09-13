'''
Verificando qual letra apareceu mais de uma vez na frase

a função do python (count()) realiza a operação com sucesso, mas queremos uilizar a logica por traz dela
'''
# exemplo de contagem com count()
frase_ex = 'andree'
# no exemplo preciso especificar a letra, no codigo abaixo eu deixo o programa descobrir para o usuario
print(frase_ex.count('e')) # função count retorna a contagem do argumento passada, geralmente uma palavra ou uma letra em uma string


#------------------------INICIO DO CONTADOR DE LETRAS -----------------------------------------

frase = 'AAndre' # setando a frase inicial

i = 0 # VARIAVEL ITERADORA

qtd_apareceu_mais_vezes = 0 # VARAVEL QUE VAI GUARDAR A QUANTIDADE EM NUMEROS EM QUE UM CARACTERE APARECEU NA FRASE
letra_que_apareceu_mais_vezes = '' # VARIAVEL QUE VAI GUARDAR A LETRA (CARACTERE QUE MASI APARECEU)

while i < len(frase): # ENQUANTO O ITERADOR FOR MENOR QUE FRASE, EXECUTE O BLOCO
    letra_atual = frase[i] # LETRA ATUAL GUARDA O CARACTERE REFERENTE A VEZ QUE O LOOP PASSOU NA STRING
    
    if letra_atual == ' ': # SE A LETRA ATUAL FOR UM ESPAÇO VOLTE PARA O WHILE PARA PEGAR A PROXIMA LETRA DIFERENTE DE ESPAÇO
        i+= 1 # ANDA UM PASSO PARA VERIFICAR SE É ESPAÇO OU NÃO
        continue # SE FOR UM ESPAÇO O CONTINUE VOLTA PARA O INICIO DO WHILE
    qtd_atual = frase.count(letra_atual) # VARIAVEL QUE CONTA O CARACTERE ATUAL DO LAÇO
    
    if qtd_apareceu_mais_vezes <= qtd_atual: # VERIFICANDO O CARACTERE QUE APARECEU MSI VEZES VERIFICANDO O INTEM ANTERIOR PARA PASSSAR PARA O PROXIMO CARACTERE SA STRING
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual
    i+= 1 # DE O PROXIMO PASSO DO LAÇO SE NÃO FOR ESPAÇO
    
print(f'A letra que apareceu masi vezes foi "{letra_que_apareceu_mais_vezes}", apareceu "{qtd_apareceu_mais_vezes}X' )
