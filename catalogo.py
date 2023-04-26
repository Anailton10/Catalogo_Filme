class Catalogo:
    def __init__(self, filme):
        self.filme = filme
        self.filmes= dict()
        self.catalogo = list()

    def menu(self):
        self.filmes['Titulo'] = self.filme.titulo
        self.filmes['Classificação'] = self.filme.classificação
        self.filmes['Genero'] = self.filme.genero
        self.filmes['Sinopse'] = self.filme.sinopse
        self.catalogo.append(self.filmes.copy())
        self.filmes.clear()



