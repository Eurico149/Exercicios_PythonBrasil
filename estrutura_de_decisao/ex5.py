nota1 = float(input("Nota(1/2): "))
nota2 = float(input("Nota(2/2): "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com distinção!")
else:
    if media > 7:
        print("Aprovado!")
    else:
        print("Reprovado!")

