import copy
from package_dados import produtos # isso importa oas produtos de uma lista definia no pacote pacage_dados

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda) para n anterar os dados originais
novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    for p in copy.deepcopy(produtos) # dependendo de como o codigo é escrito podemos alterar os preços originais então usamos deepcopy
]



# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')




# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
novos_produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p:p['nome'], # dependendo de como o codigo é escrito podemos alterar os preços originais então usamos deepcopy
    reverse=True
)

print("----------Lista de produtos--------------")
print(*produtos, sep='\n')
print()
print("----------Ordenados com 10% de aumento--------------")
print(*novos_produtos, sep='\n')
print()
print("----------Ordenados por nome--------------")
print(*novos_produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
novos_produtos_ordenados_por_preço = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p:p['preco'] # dependendo de como o codigo é escrito podemos alterar os preços originais então usamos deepcopy
)
print()
print("----------Ordenados por preço--------------")
print(*novos_produtos_ordenados_por_preço, sep='\n')