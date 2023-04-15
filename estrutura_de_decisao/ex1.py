num1 = float(input("Digite um numero(1/2): "))
num2 = float(input("Digite um numero(1/2): "))

if num1 > num2:
    print(f"Maior = {num1}")
else:
    if num2 > num1:
        print(f"Maior = {num2}")
    else:
        print("Os dois numeros sao iguais!")
