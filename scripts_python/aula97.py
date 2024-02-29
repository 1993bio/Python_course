#módulos python
import sys

#--------------------------
# meus módulos
import aula97_mod
# ou pode ser importado somente a variável
from aula97_mod import variavel_mod, soma


#--------------------------


#print("Este módulo se chama", __name__)
print(variavel_mod)
print(soma(1,1))
# ou
print(aula97_mod.soma(2,2))

