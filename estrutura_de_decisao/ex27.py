morango = float(input("Morango(KG): "))
maca = float(input("Maça(Kg): "))
preco = 0

if morango <= 5:
    preco += morango * 2.5
else:
    preco += morango * 2.2

if maca <= 5:
    preco += maca * 1.8
else:
    preco += maca * 1.5

if preco > 25 or morango + maca > 8:
    preco *= 0.9

print(f"Valor: R${preco:.2f}")