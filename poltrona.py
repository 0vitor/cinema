class Poltrona:
    def __init__(self, id, ocupada, cliente = ''):
        self.__id = id
        self.__ocupada = ocupada
        self.__cliente = cliente
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,number):
        self.__id = number

    @property
    def ocupada(self):
        return self.__ocupada
    
    @ocupada.setter
    def ocupada(self,boolean):
        self.__ocupada = boolean

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente


