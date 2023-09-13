pessoa1 = {
    'nome': 'Andre',
    'sobrenome':'caliari'
}

# o metodo get busca a chave que vc apresentar

#print(pessoa1.get('nome'))
#print(pessoa1.get('sobrenome'))


# pop apaga um item com a chave especificada tipo del
# nome = pessoa1.pop('sobrenome')
# print(nome)
# print(pessoa1)


# ultima_chave = pessoa1.popitem()
# print(ultima_chave)
# print(pessoa1)


# update altera um dicionario
# 1º forma 
pessoa1.update({
    'nome': 'Pedro',
    'idade': 25,
    'peso': 65
    })

print(pessoa1) 

# 2º forma
pessoa1.update(nacionalidade= 'Brasil', sexo='masculino') # isso tbm atualiza novas chaves com valores na lispa pessoa1

# podeos criar variaveis com iteravel do tipo tupla e lista e passar para o metodo update e atualizar um dicionario.
tupla = (('altura', 1.32), ('profissão', 'estudante'))

lista = [['escola', 'sagrado'], ['serie', 'pre-5']]

pessoa1.update(tupla)
pessoa1.update(lista)
print(pessoa1)
               
