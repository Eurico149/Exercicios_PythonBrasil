litros = float(input("Litros: "))
print("\ng-Gasolina\na-Alcool")
ope = input("Tipo de combustivel: ")

if ope == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco *= 0.97
        print(f"Valor: R${preco:.2f}")
    else:
        if litros > 20:
            preco *= 0.95
            print(f"Valor: R${preco:.2f}")
else:
    if ope == "a":
        preco = litros * 1.9
        if litros <= 20:
            preco *= 0.96
            print(f"Valor: R${preco:.2f}")
        else:
            if litros > 20:
                preco *= 0.94
                print(f"Valor: R${preco:.2f}")