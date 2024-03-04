# print(
#     'Você importou', __name__
# )

# def dobra(x):
#     return x*2
# disponibilizando funções do modulo.py para outros locais
# tudo que importarmos aqui poderemos utilizar em outros locais dentro do programa,
# o init faz a ponte de seus modulos com outros modulos
#from aula99_package.modulo import nova_variavel, soma_do_modulo, variavel, dobra
# para não precisar passar todos os nomes poderemos usar o all (*), aqui,
# é um dos poucos locais que poderemos usar este modo al
from aula99_package.modulo import *
from aula99_package.modulo_b import *




 