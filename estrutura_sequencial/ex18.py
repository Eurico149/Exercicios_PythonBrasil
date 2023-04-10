tamanho = float(input("Tamanho(MB): "))
velocidade = float(input("Velocidade(Mbps): "))
tempo = tamanho / (velocidade * 60)
print(f"Tempo em minutos: {tempo:.2f}")
