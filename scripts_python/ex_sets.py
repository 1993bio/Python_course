# xempl ode uso do sets

letras = set()

while True:
    letra = input("Digite uma letra: ")
    letras.add(letra.lower()) # a função .lower() deixa qualquer entrada de dados do tipo letras ou palavras na forma de minusculas
    # encerramento do programa
    if 'l' in letras:
        print("programa encerrado!")
        break
    print(letras)