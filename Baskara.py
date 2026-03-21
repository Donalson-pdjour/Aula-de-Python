import math

# Entrada dos valores
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

# Calcula o discriminante (Delta)
delta = b**2 - 4*a*c

if a == 0:
    print("Isso não é equação do 2º grau, pois a = 0.")
else:
    # Caso Delta seja positivo → duas raízes reais
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)

    # Caso Delta seja zero → raiz única
    elif delta == 0:
        x = -b / (2*a)
        print("Uma raiz real (raiz dupla):")
        print("x =", x)

    # Caso Delta seja negativo → não existe raiz real
    else:
        print("Não existem raízes reais, pois Delta é negativo.")