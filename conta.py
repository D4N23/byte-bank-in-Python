class Conta:

    def __init__(self, numero, titular, saldo, limite = 100):
        print("Construindo objeto .. {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def tranferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("O seu saque de R$:{} foi aprovado".format(valor))
        else:
            print("O valor R$:{} passou o limite".format(valor))

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {'BB' : '001', 'Caixa' : '104', 'Bradesco' : '237'}






