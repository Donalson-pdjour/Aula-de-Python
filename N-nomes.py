# Crie uma lista com 10 nomes: 1- imprimir a lista inteiro; 2- imprimir o indice e valor naquela posição;
# 3- insira mais  um nome no final da lista e imprima; 4- ordenar os nomes em ordem alfabética.

# Lista de nomes
nomes = ["Alice", "Bruno", "Carla", "Diego", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]

# 1- Imprimir a lista inteira
print("Lista de nomes:")
print(nomes)

# 2- Imprimir o índice e valor naquela posição
print("\nÍndice e valor de cada nome:")
for i, nome in enumerate(nomes):
    print(f"Índice {i}: {nome}")

# 3- Insira mais um nome no final da lista e imprima
nomes.append("Larissa")
print("\nLista de nomes após adicionar 'Larissa':")
print(nomes)

# 4- Ordenar os nomes em ordem alfabética
nomes.sort()
print("\nLista de nomes em ordem alfabética:")
print(nomes)

# Crie uma lista com 15 números inteiros: 1- imprimir a lista inteira; 2- imprimir o índice e valor naquela posição;
# 3- insira mais dois números no final da lista e imprima; 4- ordenar os números em ordem crescente.

# Lista de números inteiros
numeros = [10, 5, 20, 15, 30, 25, 50, 40, 35, 45, 60, 55, 70, 65, 80]

# 1- Imprimir a lista inteira
print("\nLista de números inteiros:")
print(numeros)

# 2- Imprimir o índice e valor naquela posição
print("\nÍndice e valor de cada número:")
for i, numero in enumerate(numeros):
    print(f"Índice {i}: {numero}")

# 3- Insira mais dois números no final da lista e imprima
numeros.append(85)
numeros.append(75)
print("\nLista de números inteiros após adicionar 2 novos:")
print(numeros)

# 4- Ordenar os números em ordem crescente
numeros.sort()
print("\nLista de números inteiros em ordem crescente:")
print(numeros)


# crie um lista de produtos, valor unitário e quantidade,
# 1- imprimir em cada lista de 5 itens, 2- imprimir as listas.
# 3- após isso, imprimir o valor totalo dos produtos contidos nas listas:
#     é necessário imprimir o nome do produto, valor total do item e no final o valor total geral.

# Lista de produtos
produtos = []
valor_unitario = []
quantidade = []
valor_total = []
valor_total_geral = 0
# 1- Imprimir em cada lista de 5 itens
for i in range(5):
    produto = input(f"Digite o nome do produto {i + 1}: ")
    valor = float(input(f"Digite o valor unitário do produto {i + 1}: "))
    qtd = int(input(f"Digite a quantidade do produto {i + 1}: "))
    produtos.append(produto)
    valor_unitario.append(valor)
    quantidade.append(qtd)
    valor_total.append(valor * qtd)
    valor_total_geral += valor * qtd

# 2- Imprimir as listas
print("\nLista de produtos:")
for i, produto in enumerate(produtos):
    print(f"{i + 1}. {produto}")

print("\nValores unitários:")
for i, valor in enumerate(valor_unitario):
    print(f"{i + 1}. R$ {valor:.2f}")

print("\nQuantidades:")
for i, qtd in enumerate(quantidade):
    print(f"{i + 1}. {qtd}")

print("\nValores totais:")
for i, total in enumerate(valor_total):
    print(f"{i + 1}. R$ {total:.2f}")

# 3- Imprimir o valor total geral
print(f"\nValor total geral: R$ {valor_total_geral:.2f}")
