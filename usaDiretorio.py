from dirContinuo import dirContinuo;
from dirDiscreto import dirDiscreto;

class usaDiretorio:
    def __init__(self):
        self.tabela = []
        self.dirAutor = dirDiscreto()
        self.dirAno = dirContinuo()
        self.dirGenero = dirDiscreto()

    def insere(self, chavePrinc, elemento):
        self.tabela.append([chavePrinc, elemento])
        if elemento.autor in self.dirAutor.ref:
            self.dirAutor.ref[elemento.autor].append(chavePrinc)
        else:
            self.dirAutor.ref[elemento.autor] = [chavePrinc]
        if elemento.ano in self.dirAno.ref:
            self.dirAno.ref[elemento.ano].append(chavePrinc)
        else:
            self.dirAno.ref[elemento.ano] = [chavePrinc]
        if elemento.genero in self.dirGenero.ref:
            self.dirGenero.ref[elemento.genero].append(chavePrinc)
        else:
            self.dirGenero.ref[elemento.genero] = [chavePrinc]

    def buscaPorId(self, identificador):
        for i in range(len(self.tabela)):
            if identificador in self.tabela[i]:
                item = self.tabela[i]
                return {'ID': item[0],
                        'Elemento': {
                            'Título': item[1].titulo,
                            'Autor': item[1].autor,
                            'Ano': item[1].ano,
                            'Gênero': item[1].genero
                        }}
        return 'Não existe item com esse identificador'
    
    def excluiPorId(self, identificador):
        for i in range(len(self.tabela)):
            if identificador in self.tabela[i]:
                item = self.tabela[i]
                self.dirAno.exclui(item[1].ano, item[0])
                self.dirAutor.exclui(item[1].autor, item[0])
                self.dirGenero.exclui(item[1].genero, item[0])
                self.tabela.pop(i)
                return 'Item removido'
        return 'Não existe item com esse identificador'
    
    def retornaItens(self):
        tabela = []
        for i in range(len(self.tabela)):
            item = self.tabela[i]
            tabela.append(f"ID: {item[0]}\n"
                         f"Título: {item[1].titulo}\n"
                         f"Autor: {item[1].autor}\n"
                         f"Ano: {item[1].ano}\n"
                         f"Gênero: {item[1].genero}\n"
                         "-------------------------")
        return '\n'.join(tabela)

            

    def buscaSimples(self, chaveSec):
        if chaveSec in self.dirAutor.ref:
            return self.dirAutor.ref[chaveSec]
        elif chaveSec in self.dirAno.ref:
            return self.dirAno.ref[chaveSec]
        elif chaveSec in self.dirGenero.ref:
            return self.dirGenero.ref[chaveSec]
        else:
            return 'Chave não existe'

    def buscaCombinada(self, chaveSec, chaveSec2):
        chaves1 = set()
        chaves2 = set()
        resultado = []

        if chaveSec in self.dirAutor.ref:
            chaves1 = set(self.dirAutor.ref[chaveSec])
        if chaveSec in self.dirAno.ref:
            chaves1 = set(self.dirAno.ref[chaveSec])
        if chaveSec in self.dirGenero.ref:
            chaves1 = set(self.dirGenero.ref[chaveSec])

        if chaveSec2 in self.dirAutor.ref:
            chaves2 = set(self.dirAutor.ref[chaveSec2])
        if chaveSec2 in self.dirAno.ref:
            chaves2 = set(self.dirAno.ref[chaveSec2])
        if chaveSec2 in self.dirGenero.ref:
            chaves2 = set(self.dirGenero.ref[chaveSec2])

        intersecao = chaves1.intersection(chaves2)

        if not intersecao:
            return 'Nenhum resultado encontrado'
        
        for chave in intersecao:
            if chave < (len(self.tabela) - 1):
                item = self.tabela[chave-1]
                resultado.append(f"ID: {chave}\n"
                                 f"Título: {item[1].titulo}\n"
                                 f"Autor: {item[1].autor}\n"
                                 f"Ano: {item[1].ano}\n"
                                 f"Gênero: {item[1].genero}\n"
                                 "-------------------------")
        return '\n'.join(resultado) if resultado else 'Nenhum resultado encontrado'
