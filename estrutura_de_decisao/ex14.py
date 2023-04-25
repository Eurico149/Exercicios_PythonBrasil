nota1 = float(input("Nota(1/2): "))
nota2 = float(input("Nota(2/2): "))
media = (nota1 + nota2) / 2
conceito = ""

if media < 4:
    conceito = "E"
else:
    if media < 6:
        conceito = "D"
    else:
        if media < 7.5:
            conceito = "C"
        else:
            if media < 9:
                conceito = "B"
            else:
                conceito = "A"

if conceito == "a" or conceito == "B" or conceito == "C":
    mensagem = "APROVADO!"
else:
    mensagem = "REPROVADO!"

print(f"\nNota(1/2): {nota1}\nNota(2/2): {nota2}\nMedia: {media}\nConceito: {conceito} {mensagem}")
