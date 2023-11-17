class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self):
        self.__idade += 1
        if self.__idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.__peso += abs(peso)

    def emagrecer(self, peso):
        self.__peso -= abs(peso)

    def crescer(self, cm):
        self.__altura += cm
