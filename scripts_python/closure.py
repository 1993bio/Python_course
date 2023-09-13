# Um Closure é um objeto de função que lembra valores em escopos delimitadores, mesmo que eles não estejam presentes na memória. Vamos a isso passo a passo

#Em primeiro lugar, uma função aninhada é uma função definida dentro de outra função. 
#É muito importante observar que as funções aninhadas podem acessar as variáveis ​​do escopo envolvente. 
#No entanto, pelo menos em python, eles são somente leitura. 
#No entanto, pode-se usar a palavra-chave "nonlocal" explicitamente com essas variáveis ​​para modificá-las.


# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar

# falar_bom_dia = criar_saudacao('Bom dia')
# Falar_boa_noite = criar_saudacao('Boa noite')

# for nome in ['André','Dayane','Pedro']:
#     print(falar_bom_dia(nome))
#     print(Falar_boa_noite(nome))


# Exercicio referente ao tema

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)


print(duplicar(2))
print(triplicar(2))
# e assim por diante


