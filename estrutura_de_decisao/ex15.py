lado1 = float(input("Lado(1/3): "))
lado2 = float(input("Lado(2/3): "))
lado3 = float(input("Lado(3/3): "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("E um triangulo!")
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo equilatero")
    else:
        if lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
            print("Triangulo isosceles")
        else:
            print("Triangulo Escaleno")
