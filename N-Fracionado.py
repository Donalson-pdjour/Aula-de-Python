import math

EPS = 1e-9  # tolerância para erros de ponto flutuante

def eh_inteiro(x: float) -> bool:
    return abs(x - round(x)) < EPS

def eh_cubo_perfeito(x: float) -> bool:
    # Cubo perfeito só faz sentido para inteiros
    if not eh_inteiro(x):
        return False
    n = int(round(x))
    # raiz cúbica aproximada do valor absoluto
    r = round(abs(n) ** (1/3))
    # reconstrói com o sinal original
    cubo = r ** 3
    cubo = cubo if n >= 0 else -cubo
    return cubo == n

def classificar_numero(x: float) -> str:
    if eh_cubo_perfeito(x):
        return "cubo perfeito (elevado à potência 3 de um inteiro)"
    elif eh_inteiro(x):
        return "inteiro"
    else:
        return "fracionado"

# --- Programa principal ---
entrada = input("Digite um número (ex.: 5, -8, 2.5): ").strip()

try:
    x = float(entrada.replace(",", "."))  # aceita vírgula como separador decimal
    tipo = classificar_numero(x)
    print(f"O número {x} é: {tipo}.")
except ValueError:
    print("Entrada inválida. Digite um número válido.")