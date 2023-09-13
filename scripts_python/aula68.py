'''
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir.
Existe escopo local e global.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

'''
x = 1

def escopo():# até parametros das funçeos, são só manipulados dentro das funções. 
    global x # manipulando o x global e flando que x= 10 é o global e nao masi local
    x = 10 # variavel de escopo local, ela atinge somente a função, e só pode ser usado dentro da função, fora a variavel fica como nao definida
    
    def outra_func():
        global x # todas as variaveis x vã oser manipuladas e vai passar a valer 11 porque foi a ultima definida como global
        x = 11
        y=3 # essa variavel só funciona dentro de outra fuc 
        print(x,y)# mas ela pode acessas a variavel de escolo global
    
    outra_func() # ela só pode se chamada dentro da função escopo() pq ela foi definida dento de outra função.
    print(x)

# chamando a função 
print(x) # mostra a variavel x dentro da função escopo x = 10
escopo()
print(x) # mostra a variavel global x = 1