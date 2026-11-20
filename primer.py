# Programa para verificar se um número é múltiplo de 2, 4 e 8 usando condicionais

# Solicita ao usuário um número
num = int(input("Digite um número: "))

# Verifica se é múltiplo de 2
if num % 2 == 0:
    # Se for múltiplo de 2, verifica se é múltiplo de 4
    if num % 4 == 0:
        # Se for múltiplo de 4, verifica se é múltiplo de 8
        if num % 8 == 0:
            print(f"{num} é múltiplo de 8 (e também de 2 e 4).")
        else:
            print(f"{num} é múltiplo de 4 (e de 2), mas não de 8.")
    else:
        print(f"{num} é múltiplo de 2, mas não de 4.")
else:
    print(f"{num} não é múltiplo de 2.")
