from math import ceil

tamanho = float(input("Tamanho(m2): "))
ass = ceil(tamanho / 108)
print(f"1.Usando {ass} latas de 18L custara R${ass * 80:.2f}")
ass = ceil(tamanho / 21.6)
print(f"2.Usando {ass} latas de 3.6L custara R${ass * 25:.2f}")
tamanho *= 1.1
lata18l = tamanho // 108
lata3_6l =  ceil(tamanho % 108 / 21.6)
print(f"3.Usando {lata18l} latas de 18L e {lata3_6l} de 3,6L custara R${lata18l * 80 + lata3_6l * 25:.2f}")

