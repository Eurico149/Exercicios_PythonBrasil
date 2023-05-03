print("Tipos:\nFile duplo - fd\nAlcatra - al\nPicanha - pc")
tipo = input("Tipo de carne: ")
quan = float(input("Peso(Kg): "))
preco = 0
des = 0
car = "Dinheiro"

if tipo == "fd":
    tipo = "File duplo"
    if quan <= 5:
        preco = quan * 4.9
    else:
        preco = quan * 5.8
else:
    if tipo == "al":
        tipo = "Alcatra"
        if quan <= 5:
            preco = quan * 5.9
        else:
            preco = quan * 6.8
    else:
        if tipo == "pc":
            tipo = "Picanha"
            if quan <= 5:
                preco = quan * 6.9
            else:
                preco = quan * 7.8


if input("Cartão tabajara: ") == "sim":
    car = "Cartao tabajara"
    des = 5

print(f"\nTipo: {tipo}  Quantidade: {quan}Kg\nPreço: R${preco:.2f}  Desconto: {des}%\nForma de pagamento: {car}")
print(f"Total: R${preco * (1 - des / 100):.2f}")
