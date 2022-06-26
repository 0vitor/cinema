class Admnistrador:
    def __init__(self):
       pass

    def adicionarSala(self, cinema, id, numeroPoltronas):
        cinema.adicionarSala(id, numeroPoltronas)

    def removerSala(self, cinema, id):
        cinema.removerSala(id)

    def adicionarFilme(self, cinema, dia, titulo, duracao, diretor):
        cinema.adicionarFilme(dia, titulo, duracao, diretor)

    def removerFilme(self, cinema, dia, titulo):
        cinema.removerFilme(dia, titulo)

    def adicionarSessao(self, cinema, dia, titulo, id, horario, salaId):
        cinema.adicionarSessao(dia, titulo, id, horario, salaId)
    
    def removerSessao(self, cinema, dia, titulo, id):
        cinema.removerSessao(dia, titulo, id)
