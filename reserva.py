class Reserva:
    def __init__(self, cliente, sessao, entrada, dia, cadeira):
        self.__cliente = cliente
        self.__sessao = sessao
        self.__entrada = entrada
        self.__dia = dia
        self.__cadeira = cadeira

    def imprimirReserva(self):
        return f'''
        nome: {self.__cliente.nome} 
        telefone: {self.__cliente.telefone}
        filme: {self.__sessao.nomeFilme}
        horario: {self.__sessao.horario}
        sala: {self.__sessao.sala.id}
        valor da entrada: {self.__entrada.valor} 
        dia: {self.__dia.nome}
        cadeira: {self.__cadeira}
        '''
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        return self.__cliente

    @property
    def sessao(self):
        return self.__sessao
    
    @sessao.setter
    def sessao(self, sessao):
        return self.__sessao

    @property
    def entrada(self):
        return self.__entrada
    
    @entrada.setter
    def entrada(self, entrada):
        return self.__entrada

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def cadeira(self):
        return self.__cadeira

    @cadeira.setter
    def cadeira(self, cadeira):
        self.__cadeira = cadeira


