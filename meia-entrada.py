from entrada import Entrada

class MeiaEntrada(Entrada):
    def __init__(self, valor):
        Entrada.__init__(self, valor)
    
    def mensagem(self):
        return "O valor da meia-entrada é: " + self.__valor
