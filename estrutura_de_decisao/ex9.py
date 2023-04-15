num1 = float(input("Digite um numero(1/3): "))
num2 = float(input("Digite um numero(2/3): "))
num3 = float(input("Digite um numero(3/3): "))
maior = num1
meio = num1
menor = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
if not(num2 == maior or num2 == menor):
    meio = num2
else:
    if not(num3 == maior or num3 == menor):
        meio = num3
print(menor, meio, maior)

