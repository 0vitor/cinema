from poltrona import Poltrona
from reserva import Reserva
class Sessao:
    def __init__(self, id, nomeFilme, horario, sala, listaPoltronas = None):
        self.__id = id
        self.__nomeFilme = nomeFilme
        self.__horario = horario
        self.__sala = sala
        if listaPoltronas is None:
            self.__listaPoltronas = []
        else:
            self.__listaPoltronas = listaPoltronas
        self.criarPoltronas(sala.numeroPoltronas)

    def criarPoltronas(self, numeroPoltronas):
        self.listaPoltronas = []
        for i in range(0, numeroPoltronas+1):
            self.listaPoltronas.append(Poltrona(i, False))

    def ocuparPoltrona(self, numero, cliente):
        if self.listaPoltronas[numero].ocupada == False:
            self.listaPoltronas[numero].ocupada = True
            self.listaPoltronas[numero].cliente = cliente
            print(f'''Poltrona {numero} ocupada.''')
        else:
            raise KeyError('Cadeira ja esta ocupada')
    
    def ocuparPoltronasSequenciais(self, inicio, fim, cliente):
        for i in range(inicio, fim+1):
            self.ocuparPoltrona(i,cliente)

    def poltronasDisponiveis(self):
        disponiveis = []
        for poltrona in self.listaPoltronas:
            if poltrona.ocupada == False:
                disponiveis.append(poltrona.id)
        return disponiveis

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def nomeFilme(self):
        return self.__nomeFilme
    
    @nomeFilme.setter
    def nomeFilme(self, nomeFilme):
        self.__nomeFilme = nomeFilme

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def sala(self):
        return self.__sala
    
    @sala.setter
    def sala(self, sala):
        self.__sala = sala
        criarPoltronas(sala.numeroPoltronas)
