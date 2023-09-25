# criar uma função que encontre o primeiro duplicado considerando o segundo numero como duplicação, e retorne a duplicação considerada. 

# Requisitos:
     #A ordem dos numeros duplicados é considerada a partir da segunda ocorrencia do numero, ou seja, o numero #dupicado em si.

    # exemplo:
        #[1, 2, 3, ->3<-, 2, 1]  -> 1, 2, 3 são duplicados (retorne 3)
        #[1, 2, 3, 4, 5, 6]  -> retorne -1 (não tem duplicados)
# Se não encontrar duplicados na lsta, retorne -1

# definiçã ode uma lista que será pesquisada pela funçã ode duplicatas
lista_de_listas_de_inteiros = [
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
[1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
]

def check_double(listas_de_inteiros):
        numero_checados = set()
        primeiro_duplicado = -1

        for numero in listas_de_inteiros:
              if numero in numero_checados:
                    primeiro_duplicado = numero
                    break
              

              numero_checados.add(numero)


        return primeiro_duplicado




for lista in lista_de_listas_de_inteiros:
    print(
          lista,
          check_double(lista)
    )


