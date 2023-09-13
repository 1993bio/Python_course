'''
recurso while/else

'''

string = "Andre Luiz" # string qualquer

i = 0 # variavel que ira contar os indices

while i < len(string): # enquanto o ndice for menor que o tamanho da string execute o bloco
    letra = string[i] #a variavel letra irá receber cada letra referente ao indice da variavel string
    
    if letra == ' ': # procurando uma letra especifica da string, quando encontrar o break funciona e saimos do código.
        break # parando o código

    print(letra)  # printa as letras da variavel string a cada passo do laço
    i += 1 # variavel contadora de laço
else: # se não 
    print('Nã oencontrei um espaço na string') # mostra o print do else
print('fora do while') # mostra o print fora do laço


# OBS Observamos que ao parar o laço no break nos deixamos de executar o else e vamos direto para fora do while.