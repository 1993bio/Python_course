lista = [1]

inteiro = 0

falso = False

flutuante = 0.0

nada = None

string = ''

intervalo = range(0)

tupla = ()

dicio = {}

conjunto = set()



def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE')) 
print(f'{lista=}', falsy(lista))
print(f'{dicio=}', falsy(dicio))
