from sessao import Sessao

class Filme:
    def __init__(self, titulo, duracao, diretor, sessoes = None):
       self.__titulo = titulo
       self.__duracao = duracao
       self.__diretor = diretor
       if sessoes is None:
        self.__sessoes = []
       else:
        self.__sessoes = sessoes

    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def diretor(self):
        return self.__diretor
    
    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def sessoes(self):
        return self.__sessoes

    @sessoes.setter
    def sessoes(self, sessoes):
        self.__sessoes = sessoes

    def adicionarSessao(self, id, horario, sala):
        sessao = Sessao(id, self.__titulo, horario, sala)
        self.__sessoes.append(sessao)
    
    def removerSessao(self, id):
        for sessao in self.__sessoes:
            if sessao.id == id:
                self.__sessoes.remove(sessao)

    def poltronasDisponiveis(self, numeroSessao):
        return self.__sessoes[numeroSessao].poltronasDisponiveis()

    def ocuparPoltrona(self, cliente, entrada, numeroSessao, numero, dia):
        try:
            self.__sessoes[numeroSessao].ocuparPoltrona(numero, "Myck")
            cliente.adicionarReserva(self.__sessoes[numeroSessao], entrada, dia, numero)
        except:
            print("Error")

    def informarSessoes(self):
        for sessao in self.__sessoes:
            text = f'''
Sessao: {sessao.id}
Filme: {sessao.nomeFilme}
Horario: {sessao.horario}
Sala: {sessao.sala.id}
'''
            print(text)
    