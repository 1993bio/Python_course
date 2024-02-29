import importlib

import aula98_mod

print(aula98_mod.variavel)

for i in range(10):
    importlib.reload(aula98_mod)
    print(i)
    print('fim')