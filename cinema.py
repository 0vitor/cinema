from dia import Dia
from sala import Sala

class Cinema:
    def __init__(self, salas = None, dias = None):
        if salas is None:
            self.__salas = []
        else:
            self.__salas = salas
        
        if dias is None:
            self.__dias = [Dia("Domingo"), Dia("Segunda"), Dia("Terca"), Dia("Quarta"), Dia("Quinta"), Dia("Sexta"), Dia("Sabado")]
        else:
            self.__dias = dias

    @property
    def salas(self):
        return self.__salas

    @salas.setter
    def salas(self, salas):
        self.__salas = salas

    @property
    def dias(self):
        return self.__dias

    def adicionarSala(self, id, numeroPoltronas):
        self.__salas.append(Sala(id, numeroPoltronas))
    
    def removerSala(self, id):
        for sala in self.__salas:
            if sala.id == id:
                self.__salas.remove(sala)

    def adicionarFilme(self, dia, titulo, duracao, diretor):
        self.__dias[dia].adicionarFilme(titulo, duracao, diretor)

    def removerFilme(self, dia, titulo):
        for filme in self.__dias[dia].filmes:
            if filme.titulo == titulo:
                self.__dias[dia].filmes.remove(filme)

    def adicionarSessao(self, dia, titulo, id, horario, salaId):
        for sala in self.__salas:
            if sala.id == salaId:
                for filme in self.__dias[dia].filmes:
                    if filme.titulo == titulo:
                        filme.adicionarSessao(id, horario, sala)
                        break
                break

    def removerSessao(self, dia, titulo, id):
        for filme in self.__dias[dia].filmes:
            if filme.titulo == titulo:
                filme.removerSessao(id)

