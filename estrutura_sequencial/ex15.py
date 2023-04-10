valor_hora = float(input("Valor ganho por hora: "))
horas = float(input("Horas trabalhadas no mes: "))
salario_bruto = valor_hora * horas
print(f"\nSalario Bruto: {salario_bruto:.2f}\nIR: {salario_bruto * 0.11:.2f}")
print(f"INSS: {salario_bruto * 0.08:.2f}\nSindicato: {salario_bruto * 0.05:.2f}\nSalario liquido: {salario_bruto * 0.76:.2f}")

