class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def get_cor(self):
        return self.__cor

    def set_cor(self, novacor):
        self.__cor = novacor
