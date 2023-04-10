peso = float(input("Peso(Kg): "))
if peso > 50:
    excesso = peso - 50
    print(f"Houve {excesso:.2f}Kg de excesso, logo deve-se pagar: R${excesso * 4:.2f}")
else:
    print("Nao houve excesso!")
