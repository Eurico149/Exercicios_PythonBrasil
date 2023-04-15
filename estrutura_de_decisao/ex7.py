num1 = float(input("Digite um numero(1/3): "))
num2 = float(input("Digite um numero(2/3): "))
num3 = float(input("Digite um numero(3/3): "))
maior = num1
menor = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
print(f"Maior = {maior}")

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
print(f"Menor = {menor}")

