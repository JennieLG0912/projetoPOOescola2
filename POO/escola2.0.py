class Escola:
    def __init__(self, nomeEscola=None, enderecoEscola=None, telefoneEscola=None, diretorEscola=None, salaEscola=None, alunoEscola=None ):
        self.nomeEscola = nomeEscola
        self.enderecoEscola = enderecoEscola
        self.telefoneEscola = telefoneEscola
        self.diretorEscola = diretorEscola
        self.salaEscola = salaEscola
        self.alunoEscola = alunoEscola

    def descrever(self):
        self.nomeEscola = input("")
        self.enderecoEscola = input("")