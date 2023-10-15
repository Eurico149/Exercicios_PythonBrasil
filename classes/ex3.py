class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, novabase):
        self.__base = novabase

    def get_altura(self):
        return self.__altura

    def set_altura(self, novaaltura):
        self.__altura = novaaltura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return self.__base * 2 + self.__altura * 2


if __name__ == "__main__":
    from math import ceil
    base = float(input("Digite a medida da base(cm): "))
    altura = float(input("Digite a medida da altura(cm): "))
    retangulo = Retangulo(base, altura)
    area_piso = float(input("\nDigite a area do piso(cm2): "))
    tamanho_rodape = float(input("Digite o tamanho do rodape(cm): "))
    print("Pisos =", ceil(retangulo.area() / area_piso))
    print("Rodapes =", ceil(retangulo.perimetro() / tamanho_rodape))
