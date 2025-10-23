class Pessoa:
    def _init_(self, nome = None):
        if nome is None:
            nome = input("Digite o nome da Pessoa: ")
        self.nome = nome

    def apresentar(self):
        return f"Olá, eu sou {self.nome}"
    
class Aluno(Pessoa):
    def _init_(self, nome = None, matricula = None ):
        if nome is None:
            nome = input("Digite o nome do Aluno: ")
        if matricula is None:
            matricula = input("Digite a matrícula do Aluno: ")

        super()._init_(nome)
        self.matricula = matricula

    def apresentar(self):
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula}"
    
class Professor(Aluno):
    def _init_(self, nome = None, matricula = None, disciplina = None):
        if nome is None:
            nome = input("Digite o nome do Professor: ")
        if matricula is None:
            matricula = input("Digite a matrícula do Professor: ")
        if disciplina is None:
            disciplina = input("Digite qual diciplina o professor leciona: ")
        
        # usar o _init_ da superclasse (Aluno) que aceita nome e matrícula
        super()._init_(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        # chamar o método apresentar() com parênteses
        base = super().apresentar()
        return f"{base}, e sou professor da disciplina {self.disciplina}, matrícula {self.matricula}"
   
pessoa = Pessoa()
aluno = Aluno()
professor = Professor()

print(pessoa.apresentar())
print(aluno.apresentar())
print(professor.apresentar())