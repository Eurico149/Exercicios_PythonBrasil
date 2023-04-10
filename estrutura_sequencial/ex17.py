tamanho = float(input("Tamanho(m2): "))
ass = tamanho / 108
if ass != int(ass):
    ass = round(ass+0.5)
print(f"1.Usando {ass} latas de 18L custara R${ass * 80:.2f}")
ass = tamanho / 21.6
if ass != int(ass):
    ass = round(ass+0.5)
print(f"2.Usando {ass} latas de 3.6L custara R${ass * 25:.2f}")
tamanho *= 1.1
lata18l = tamanho // 108
lata3_6l =  tamanho % 108 / 21.6
if lata3_6l != int(lata3_6l):
    lata3_6l = round(lata3_6l+0.5)
print(f"3.Usando {int(lata18l)} latas de 18L e {lata3_6l} de 3,6L custara R${lata18l * 80 + lata3_6l * 25:.2f}")

