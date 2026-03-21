# Programa para obter o nome em maiúsculas e verificar se a pessoa é maior ou menor de idade

# Solicita o nome da pessoa
nome = input("Digite o nome da pessoa: ")

# Converte o nome para maiúsculas
nome_maiusculo = nome.upper()

# Solicita a idade
idade = int(input("Digite a idade da pessoa: "))

# Verifica se é maior ou menor de idade
if idade >= 18:
    status_idade = "maior de idade"
else:
    status_idade = "menor de idade"

# Exibe os resultados
print(f"Nome em maiúsculas: {nome_maiusculo}")
print(f"A pessoa é {status_idade}.")
