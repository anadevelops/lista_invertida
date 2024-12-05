class Livro:
    def __init__(self, id, titulo, autor, ano, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__genero = genero
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def ano(self):
        return self.__ano

    @property
    def genero(self):
        return self.__genero

    @property
    def id(self):
        return self.__id

    def criaLivro(self, id, titulo, autor, ano, genero):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__genero = genero
