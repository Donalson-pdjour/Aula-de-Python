import math

a = float(input("Digite a aresta da base (a): "))
h = float(input("Digite a altura da pirâmide (h): "))

# Verifica se os valores são válidos
if a <= 0 or h <= 0:
    print("Os valores devem ser positivos!")
else:
    g = math.sqrt(h**2 + (a/2)**2)
    print("A geratriz da pirâmide é:", g)