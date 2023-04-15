turno = input("Digite seu turno; M para matutino, V para vespertino e N para noturno: ")
if turno == "M":
    print("Bom dia!")
else:
    if turno == "V":
        print("Boa tarde!")
    else:
        if turno == "N":
            print("Boa noite!")
        else:
            print("Valor invalido!")

