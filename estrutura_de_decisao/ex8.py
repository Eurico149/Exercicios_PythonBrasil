pro1 = float(input("Valor do produto(1/3): "))
pro2 = float(input("Valor do produto(2/3): "))
pro3 = float(input("Valor do produto(3/3): "))
menor = pro1
ass = "Produto 1"

if pro1 == pro2 and pro2 == pro3:
    print("Todos valem a pena, pois todos são o mesmo preço!")
else:
    if pro1 == pro2:
        print("Os dois primeiros produtos tem o mesmo valor!")
    else:
        if pro2 == pro3:
            print("Os dois ultimos produtos tem o mesmo preço!")
        else:
            if pro1 == pro3:
                print("O primeiro e o ultimo produto tem mesmo valor!")
            else:
                if menor > pro2:
                    ass = "Produto 2"
                if menor > pro3:
                    ass = "Produto 3"
                print(f"Melhor = {ass}")

