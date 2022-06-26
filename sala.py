from poltrona import Poltrona

class Sala:  
    def __init__(self, id, numeroPoltronas):
        self.__id = id 
        self.__numeroPoltronas = numeroPoltronas
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, number):
        self.__id = number
    
    @property
    def numeroPoltronas(self):
        return self.__numeroPoltronas

    @numeroPoltronas.setter
    def numeroPoltronas(self, number):
        self.__numeroPoltronas = number




    