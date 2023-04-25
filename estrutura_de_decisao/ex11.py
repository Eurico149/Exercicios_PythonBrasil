salario = float(input("Salario: "))
sala_ajus = 0
per = 0

if salario > 1500:
    per = 0.05
    sala_ajus = salario * 1.05
else:
    if salario > 700:
        per = 0.1
        sala_ajus = salario * 1.1
    else:
        if salario > 280:
            per = 0.15
            sala_ajus = salario * 1.15
        else:
            per = 0.2
            sala_ajus = salario * 1.2

print(f"Salario: R${salario:.2f}\nPercentual de aumento: {int(per * 100)}%\nValor do aumento: R${per * salario:.2f}\nSalario final: R${sala_ajus:.2f}")
