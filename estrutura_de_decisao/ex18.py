def veri(aux):
    c = False
    a = (aux[2] == "/" and aux[5] == "/") and (len(aux) == 10)
    b = (aux[0:2].isnumeric() and aux[3:5].isnumeric() and aux[6:].isnumeric())

    if b:
        if int(aux[0:2]) < 29 and int(aux[3:5]) < 13:
            c = True
    if a and b and c:
        return True
    else:
        return False


data = input("Digite a data: ")

while not(veri(data)):
    print("\nData invalida!")
    data = input("Digite a data: ")

print("Formato correto!")
