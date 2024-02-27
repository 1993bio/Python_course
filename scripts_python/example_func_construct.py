# criando uma função geradora com yield para a sequencia de fibonacci
# cada novo termo é a soma dos dois antecessores....

import time

def fib_generator(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

def fib_list(max):
    nums = []
    a , b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#-----------------------------------------
# Verificando o tempo de execução da função geradora

start_time_gen = time.time()
for n in fib_generator(1000):
    print(n)
end_time_gen = time.time()

# Verificando o tempo de execução da função gera lista e retorna da lista

start_time_list = time.time()
for n in fib_list(1000):
    print(n)
end_time_list = time.time()

# printando o resultado do tempo de exec.
print(f"Tempo função geradora:{end_time_gen-start_time_gen}")
print(f"Tempo função lista:{end_time_list-start_time_list}")




