tamanho = float(input("Tamnho(m2): "))
ass = tamanho / 5
if ass == int(ass):
    print(f"Latas: {ass}\nValor: R${ass * 80:.2f}")
else:
    ass = round(ass+0.5)
    print(f"Latas: {int(ass)}\nValor: R${ass*80:.2f}")
