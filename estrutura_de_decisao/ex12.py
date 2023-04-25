horas = int(input("Horas trabalhadas: "))
sala = float(input("Salario por horas: "))
total = sala * horas

aux1 = "Salario Bruto: ({} * {})".format(sala, horas)
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total))

aux1 = "(-) IR (5%)"
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total * 0.05))

aux1 = "(-) INSS (10%)"
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total * 0.10))

aux1 = "FGTS (11%)"
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total * 0.11))

aux1 = "Total de Descontos"
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total * 0.15))

aux1 = "Salario Liquido"
print("{:<32} {:>10} R${:.2f}".format(aux1, ":", total * 0.85))