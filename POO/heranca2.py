class Pessoa:
    def __init__(self, nome: str | None = None):
        if nome is None:
            nome = input("Digite o nome da Pessoa: ")
        self.nome = nome

    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}"
    
class Aluno(Pessoa):
    def __init__(self, nome: str | None = None, matricula: str | None = None ):
        if nome is None:
            nome = input("Digite o nome do Aluno: ")
        if matricula is None:
            matricula = input("Digite a matrícula do Aluno: ")

        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula}"
    
class Professor(Aluno):
    def __init__(self, nome: str | None = None, matricula: str | None = None, disciplina: str | None = None):
        if nome is None:
            nome = input("Digite o nome do Professor: ")
        if matricula is None:
            matricula = input("Digite a matrícula do Professor: ")
        if disciplina is None:
            disciplina = input("Digite qual diciplina o professor leciona: ")
        
        # usar o __init__ da superclasse (Aluno) que aceita nome e matrícula
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base}, e sou professor da disciplina {self.disciplina}, matrícula {self.matricula}"
   

# pessoa = Pessoa()
# aluno = Aluno()
professor = Professor()

# print(pessoa.apresentar())
# print(aluno.apresentar())
print(professor.apresentar())