from reserva import Reserva

class Cliente:
    def __init__(self, nome, telefone, reservas = None):
        self.__nome = nome
        self.__telefone = telefone
        if reservas is None:
            self.__reservas = []
        else:
            self.__reservas = reservas

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        return self.__telefone

    @property
    def reservas(self):
        return self.__reservas

    @reservas.setter
    def reservas(self, reservas):
        self.__reservas = reservas
    
    def adicionarReserva(self, sessao, entrada, dia, numero):
        self.__reservas.append(Reserva(self, sessao, entrada, dia, numero))