class dirDiscreto:
    def __init__(self):
        self.__ref = dict()

    @property
    def ref(self):
        return self.__ref

    def insere(self, chaveSec, chavePrinc):
        if chaveSec in self.__ref:
            self.__ref[chaveSec].append(chavePrinc)
        else:
            self.__ref[chaveSec] = chavePrinc

    def busca(self, chaveSec):
        if chaveSec in self.__ref:
            return self.__ref[chaveSec]
        else:
            return 'Não existe essa chave'

    def exclui(self, chaveSec, chavePrinc):
        if chaveSec in self.__ref:
            if chavePrinc in self.__ref[chaveSec]:
                self.__ref[chaveSec].remove(chavePrinc)
            else:
                return 'Item não existe'
        else:
            return 'Item não existe'