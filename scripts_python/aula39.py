''''
iterando strings com while
'''
#       0123456789
nome = "andre luiz" # string são iteraveis
#      10987654321


indice = 0 # indice para começar o contador 

novo_nome = '' # variavel que irá receber o novo nome modificado

while indice < len(nome): # while para iterar cada indice no tamanho da string
    letra = nome[indice] # cada passada do laço a variavel letra ira receber a letra correspondente ao seu indice até o final
    novo_nome += letra + '_' # a variavel novo nome que é vazia, recebe o nome antigo modificando a cada iteração o caractere underline criando separadores entre as letras da string
    indice += 1 # contador iterador do laço while para repetir a quantidade de vezes do tamanho da string
    
print(novo_nome) # printando o novo nome modificado.



