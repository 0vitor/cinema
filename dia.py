from filme import Filme

class Dia:
    def __init__(self, nome, filmes = None):
        self.__nome = nome
        if filmes is None:
            self.__filmes = []
        else:
            self.__filmes = filmes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def filmes(self):
        return self.__filmes

    @filmes.setter
    def filmes(self, filmes):
        self.__filmes = filmes
    
    def adicionarFilme(self, titulo, duracao, diretor):
        filme = Filme(titulo, duracao, diretor)
        self.__filmes.append(filme)
    
