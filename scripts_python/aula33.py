'''
Revendo a documentação do python

tipos de dados imutaveis (str, int, float, bool)

'''
# string são imutaveis, ou seja ao tentar acessar um caractere e muda-lo,
# não conseguimos trocar seus valores, vejamos um exemplo:

string = 'andré Luiz' # definindo uma string
#string[3] = 'é' # tentando trocar o item r da string por outro é, se desse certo ficaria da seguinte maneira: 'Andéé'


#                        Para isso devemos criar outra variavel formatar a string e adicionar mais textos
outra_variavel = f'{string[:4]}ABC{string[5:]}'#string criando uma variavel para receber uma string e suas modificações.add()
print(string) # acessando valores/caracteres de uma string, e vemos que retorna um erro, dizendo que não pode fazer a mudança
print(outra_variavel)

# exemplo de métodos
#variavel_string.metodo
#string.capitalize()
print(string.capitalize()) #Capitalize permite colocar a primeira letra maiuscula.