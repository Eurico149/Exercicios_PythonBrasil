dinheiro = int(input("Dinheiro: "))

if dinheiro >= 100:
    print("Notas de 100: " + str(dinheiro // 100))
    dinheiro -= (dinheiro // 100) * 100
if dinheiro >= 50:
    print("Notas de 50: " + str(dinheiro // 50))
    dinheiro -= (dinheiro // 50) * 50
if dinheiro >= 10:
    print("Notas de 10: " + str(dinheiro // 10))
    dinheiro -= (dinheiro // 10) * 10
if dinheiro >= 5:
    print("Notas de 5: " + str(dinheiro // 5))
    dinheiro -= (dinheiro // 5) * 5
if dinheiro >= 1:
    print("Notas de 1: " + str(dinheiro // 1))
    dinheiro -= dinheiro // 1


