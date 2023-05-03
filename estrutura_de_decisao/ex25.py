cont = 0
a = input("Telefonou para a vítima? ")
b = input("Esteve no local do crime? ")
c = input("Mora perto da vítima? ")
d = input("Devia para a vítima? ")
e = input("Já trabalhou com a vítima? ")

if a == "sim":
    cont += 1
if b == "sim":
    cont += 1
if c == "sim":
    cont += 1
if d == "sim":
    cont += 1
if e == "sim":
    cont += 1

if cont == 5:
    print("Assasino!")
else:
    if cont > 2:
        print("Suspeito!")
    else:
        print("Inocente!")
