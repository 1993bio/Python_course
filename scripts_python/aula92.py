# podemos dar continuidade de um generator usando outro generator e acessa valores em diferentes ordens.

def gen1():
    print("inicio gen_1")
    yield 1
    yield 2
    yield 3
    print("fim gen_1")

def gen3():
    print("inicio gen_3")
    yield 10
    yield 20
    yield 30
    print("fim gen_3")

def gen2(gen):
    print("inicio gen_2")
    yield from gen()
    yield 4
    yield 5
    yield 6
    print("fim gen_2")


g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)
for numero in g2:
    print(numero)

