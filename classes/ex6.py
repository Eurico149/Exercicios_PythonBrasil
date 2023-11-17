class TV:
    def __init__(self, codigo: int, modelo, frequencia=(50, 700), volume=(0, 100)):
        self.__volume_faixa = volume
        self.__volume = 0
        self.__codigo = codigo
        self.__modelo = modelo
        self.__frequencia_faixa = frequencia
        self.__canal = frequencia[0]

    def aumentar(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume Invalido")
        if (volume + self.__volume) > 100:
            self.__volume = 100
        else:
            self.__volume += volume

    def diminuir(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume Invalido!")
        if (volume - self.__volume) < 0:
            self.__volume = 0
        else:
            self.__volume -= volume

    def selec_canal(self, frequencia):
        if frequencia < self.__frequencia_faixa[0] or frequencia > self.__frequencia_faixa[1]:
            raise ReferenceError("Frequencia Invalida!")
        self.__canal = frequencia

    def get_codigo(self):
        return self.__codigo

    def get_modelo(self):
        return self.__modelo

    def __eq__(self, other):
        if isinstance(other, TV):
            if self.__codigo == other.get_codigo() and self.__modelo == other.get_modelo():
                return True
        return False

    def __str__(self):
        return f"[{self.__modelo}, {self.__codigo}] - {self.__frequencia_faixa}Mhz | Volume: {self.__volume_faixa}"
