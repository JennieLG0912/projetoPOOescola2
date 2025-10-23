class Escola:
    def __init__(self, nomeEscola=None, enderecoEscola=None, telefoneEscola=None, diretorEscola=None, salaEscola=None, alunoEscola=None ):
        self.nomeEscola = nomeEscola
        self.enderecoEscola = enderecoEscola
        self.telefoneEscola = telefoneEscola
        self.diretorEscola = diretorEscola
        self.salaEscola = salaEscola
        self.alunoEscola = alunoEscola

    def descrever(self):
        self.nomeEscola = input("Qual o nome da sua escola")
        self.enderecoEscola = input("Qual o endereço da sua escola")
        self.telefoneEscola = input("Qual o telefone da sua escola")
        self.diretorEscola = input("Quem é o diretor(a) da sua escola")
        self.salaEscola = input("Quantas salas tem sua escola")
        self.alunoEscola =input("Quantos alunos tem sua escola")