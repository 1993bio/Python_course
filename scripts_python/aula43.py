'''
loop for, é um laço de repetição 
UTILIZAMOS O WHILE QUANDO N SABEMOS O NUMERO DE REPETIÇÕES,
EX: UM USUARIO PODE ERRAR INFINITAS VEZES UMAS SENHA ATÉ QUE ACERTE A SENHA 
'''
# exemplo de while com infinitas repetições com lool controlado até o acerto da condição
'''
senha_salva = '123456'
senha_digitada = ''
repetições = 0

while senha_digitada != senha_salva:
    senha_digitada = input(f'Sua senha({repetições}x): ')
    
    repetições += 1

print(f'Você acertou na {repetições}ª repetição')
print('o laço acima pode ter infinitas repetições')

'''
# No for não precisamos controlar a iteração como é feita no laço while

texto = 'Python' # string para ser iterada

novo_txt = '' 

for letra in texto: # para cada letra na string faça:
    novo_txt += f'-{letra}'
    print(letra)
print(novo_txt + '-') # exiba a letra que correspomde a cada passo o laço
    




























