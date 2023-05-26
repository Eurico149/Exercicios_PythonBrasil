def veri(endereco):
    aux = False

    def ponto(lista):
        tupla = []
        for j in range(len(lista)):
            if lista[j] == ".":
                tupla.append(j)
        return tuple(tupla)

    pontos = ponto(endereco)
    if len(pontos) == 3:
        if endereco[0:pontos[0]] and endereco[pontos[0] + 1:pontos[1]].isnumeric():
            if endereco[pontos[1] + 1:pontos[2]].isnumeric() and endereco[pontos[2] + 1:endereco.index("\n")].isnumeric():
                if int(endereco[0:pontos[0]]) < 256 and int(endereco[pontos[0] + 1:pontos[1]]) < 256:
                    if int(endereco[pontos[1] + 1:pontos[2]]) < 256 and int(endereco[pontos[2] + 1:endereco.index("\n")]) < 256:
                        aux = True
    return aux


with open("arquivo.txt", "w") as arquivo:
    arquivo.write("200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256\n")

with open("arquivo.txt", "r") as arquivo:
    ips = arquivo.readlines()

validos = []
invalidos = []
for i in range(len(ips)):
    if veri(ips[i]):
        validos.append(ips[i])
    else:
        invalidos.append(ips[i])

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("[Enderecos validos:]\n")
    for e in range(len(validos)):
        arquivo.write(validos[e])
    arquivo.write("\n[Enderecos invalidos:]\n")
    for e in range(len(invalidos)):
        arquivo.write(invalidos[e])

print(validos)
print(invalidos)
