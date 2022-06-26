class Entrada:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    def mensagem(self):
        return "O valor da entrada é:" + self.__valor