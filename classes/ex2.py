class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def get_lado(self):
        return self.__lado

    def set_lado(self, novolado):
        self.__lado = novolado

    def area(self):
        return self.__lado**2
