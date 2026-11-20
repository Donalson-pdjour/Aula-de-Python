
# cria um programa em python que simule um sistema de cadastro de 5 produtos, onde o usário pode inserir o nome  do produto,
# o preço unitario de cada produto e a quantidade em estoque e calcule o valor total do produto. O programa deve armazenar essas informações em uma lista de dicionários 
# e permitir que o usuário visualize os produtos cadastrados e o valor total de cada um e depos mostrar o valor toal de compra.
# # Lista para armazenar os produtos   

produtos = []
qty_produtos = []
valor_total_compra = 0
cont = 0

while cont <= 5:
    print(f"Produto {cont + 1}")
    while True:
        nome_produto = input("Digite o nome do produto: ")
        if len(nome_produto) >= 3 and nome_produto.isalpha():
            nome_produto = nome_produto.upper()  # Converte para maiúsculas
            break
        else:
            print("O nome do produto deve conter pelo menos 3 caracteres e ser composto apenas por letras. Tente novamente.")
    while True:
        try:
            preco_produto = float(input("Digite o preço do produto: "))
            if preco_produto >= 0 and isinstance(preco_produto, (int, float)):
                break
            else:
                print("O preço do produto deve ser um número positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o preço.")
    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            if quantidade_produto >= 0:
                break
            else:
                print("A quantidade do produto deve ser um número positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a quantidade.")

    # Calcula o valor total do produto
    valor_total_produto = preco_produto * quantidade_produto
    valor_total_compra += valor_total_produto

    # Armazena as informações do produto em um dicionário
    produto = {
        "nome": nome_produto,
        "preço": preco_produto,
        "quantidade": quantidade_produto,
        "valor_total": valor_total_produto
    }
    produtos.append(produto)

    cont += 1

# Exibe os produtos cadastrados e seus valores totais
print("\nProdutos cadastrados:")
for i, produto in enumerate(produtos, start=1):
    print(f"Produto {i}: {produto['nome']} - Preço: R$ {produto['preço']:.2f} - Quantidade: {produto['quantidade']} - Valor Total: R$ {produto['valor_total']:.2f}")

print(f"\nValor total da compra: R$ {valor_total_compra:.2f}")
