numero = list(input("Numero: "))
aux = ""

if len(numero) > 2:
    resu = int(numero[-3])
    if resu > 1:
        aux += str(resu) + " Centenas"
    if resu == 1:
        aux += str(resu) + " Centena"

if len(numero) > 1:
    resu = int(numero[-2])
    if int(numero[-1]) == 0 and resu != 0 and len(numero) != 2:
        aux += " e "
    if len(numero) == 3 and resu != 0 and int(numero[-1]) != 0:
        aux += ", "
    if resu > 1:
        aux += str(resu) + " Dezenas"
    if resu == 1:
        aux += str(resu) + " Dezena"

if len(numero) > 0:
    resu = int(numero[-1])
    if len(numero) > 1 and resu != 0:
        aux += " e "
    if resu > 1:
        aux += str(resu) + " Unidades"
    if resu == 1:
        aux += str(resu) + " Unidade"

print(aux)
