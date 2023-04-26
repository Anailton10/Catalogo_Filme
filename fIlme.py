class Filme:
    def __init__(self, titulo=None, classificação=None, genero=None, sinopse=None):
        self.__titulo = titulo
        self.__classi = classificação
        self.__sinop = sinopse
        self.__genero = genero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, ti):
        self.__titulo = ti

    @property
    def classificação(self):
        return self.__classi

    @classificação.setter
    def classificação(self, clasi):
        self.__classi = clasi

    @property
    def sinopse(self):
        return self.__sinop

    @sinopse.setter
    def sinopse(self, sim):
        self.__sinop = sim

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, g):
        self.__genero = g
