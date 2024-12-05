from dirContinuo import dirContinuo;
from dirDiscreto import dirDiscreto;

class usaDiretorio:
    def __init__(self):
        self.__tabela = []
        self.dirAutor = dirDiscreto()
        self.dirAno = dirContinuo()
        self.dirGenero = dirDiscreto()

    def insere(self, chavePrinc, elemento):
        self.__tabela.append([chavePrinc, elemento])
        if elemento.autor in self.dirAutor.ref:
            self.dirAutor.ref[elemento.autor].append(chavePrinc)
        else:
            self.dirAutor.ref[elemento.autor] = chavePrinc
        if elemento.ano in self.dirAno.ref:
            self.dirAno.ref[elemento.ano].append(chavePrinc)
        else:
            self.dirAno.ref[elemento.ano] = chavePrinc
        if elemento.genero in self.dirGenero.ref:
            self.dirGenero.ref[elemento.genero].append(chavePrinc)
        else:
            self.dirGenero.ref[elemento.genero] = chavePrinc

    def buscaSimples(self, chaveSec):
        if chaveSec in self.dirAutor.ref:
            return self.dirAutor.ref[chaveSec]
        elif chaveSec in dirAno.ref:
            return self.dirAno.ref[chaveSec]
        elif chaveSec in dirGenero.ref:
            return self.dirGenero.ref[chaveSec]
        else:
            return 'Chave não existe'

    # def buscaCombinada(self, chaveSec, chaveSec2):