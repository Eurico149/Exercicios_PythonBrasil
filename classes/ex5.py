class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def set_nome(self, novonome):
        self.__nome = novonome

    def deposito(self, dinheiro):
        self.__saldo += dinheiro

    def saque(self, dinheiro):
        self.__saldo -= dinheiro
