# intro a generators functions em python

# generator = (n for n in range(10000))  # cria um objeto generator em apenas um espaço na    memória sem ter salvo todos os valores dos 10000 itens.

# ----------- criando uma função geradora ----------

def generator(n=0, maximum =10):
    while True: # entra num loop infinito
        yield n # pausa no primeiro item
        n+=1 # conta mais um

        if n > maximum: #verifica n até que seja verdadeiro e para a função 
            return


# chamando a função geradora numa variavel 

gen = generator(n=0, maximum=10) # isso é a mesma função passada no caput deste código
# printado de forma iterativa os valores 
for n in gen:
    print(n)