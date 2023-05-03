nota1 = float(input("Nota(1/3): "))
nota2 = float(input("Nota(2/3): "))
nota3 = float(input("Nota(3/3): "))
media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("\nAprovado com distinção!")
else:
    if media >= 7:
        print("\nAprovado!")
    else:
        print("\nReprovado!")

print("Media: " + str(media))
