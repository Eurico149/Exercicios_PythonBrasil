a = float(input("Valor de A: "))
if a == 0:
    print("Não é uma equação de segundo grau!")
else:
    b = float(input("Valor de B: "))
    c = float(input("Valor de C: "))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Equaição não possui raizes reais!")
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    if delta == 0:
        print(f"Raiz(1/1): {raiz1}")
    else:
        print(f"Raiz(1/2): {raiz1}\nRaiz(2/2): {raiz2}")
