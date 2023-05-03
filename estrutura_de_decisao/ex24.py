num1 = float(input("Numero(1/2): "))
num2 = float(input("Numero(2/2): "))
print("\nOperacoes\nsom = Soma\nsub = Subtracão\nmul = Multiplicacão\ndiv = Divisão")
opera = input("Digite a operacão: ")
resu = 0

if opera == "som":
    resu = num1 + num2
else:
    if opera == "sub":
        resu = num1 - num2
    else:
        if opera == "mul":
            resu = num1 * num2
        else:
            if opera == "div":
                resu = num1 / num2
            else:
                print("Operação invalida!")

if resu % 2 == 0:
    print("\nPar")
else:
    print("\nImpar")
if resu > 0:
    print("Positivo!")
else:
    print("Negativo!")
if int(resu) == resu:
    print("Inteiro!")
else:
    print("Decimal!")
