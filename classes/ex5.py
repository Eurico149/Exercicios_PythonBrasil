class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def set_nome(self, novonome):
        self.__nome = novonome

    def deposito(self, dinheiro):
        if dinheiro <= 0:
            raise ValueError("Valor Invalido!")
        self.__saldo += dinheiro

    def saque(self, dinheiro):
        if dinheiro <= 0:
            raise ValueError("Valor Invalido!")
        if dinheiro < self.__saldo:
            raise ValueError("Valor De Saque Superior Ao Saldo Na Conta!")
        self.__saldo -= dinheiro
