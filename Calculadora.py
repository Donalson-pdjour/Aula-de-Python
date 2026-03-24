# Cria um programa de calculadora que permita soma, subtração, multiplicação e divisão,
# de 2 numeros, usando input:
#     1- é necessário realizar a multiplicação  de 2 numeros + a soma de 1 numero;
#     2- é necessário realizar a divisão de 2 numeros - a subtração de 1 numero;
#     3- é necessário realizar a soma de 2 numeros * a multiplicação de 1 numero;
#     4- é necessário realizar a subtração de 2 numeros / a divisão de 1 numero.

# Função para realizar as operações
def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Saindo da calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            print("Resultado: ", resultado)
        elif escolha == '2':
            resultado = num1 - num2
            print("Resultado: ", resultado)
        elif escolha == '3':
            resultado = num1 * num2
            print("Resultado: ", resultado)
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado: ", resultado)
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")

# Chamada da função para iniciar a calculadora
calculadora()

