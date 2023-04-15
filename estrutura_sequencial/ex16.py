from math import ceil

tamanho = float(input("Tamnho(m2): "))
ass = ceil(tamanho / 54)
print(f"Latas: {ass}\nValor: R${ass * 80:.2f}")
