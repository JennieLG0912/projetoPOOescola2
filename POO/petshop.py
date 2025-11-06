class Adotante:
    def __init__(self, nomea=None, cpf=None, idadea=None):
        print("-------Dados do adotante--------")
        if nomea is None:
            nomea = input("Digite o seu nome: ")
        self.nomea = nomea

        if cpf is None:
            cpf = int(input("Digite o seu cpf: "))
        self.cpf = cpf

        if idadea is None:
            idadea = int(input("Digite sua idade: "))
        self.idadea = idadea

    def apresentar(self) -> str:
        return f"Olá {self.nomea}, bem vindo(a) ao nosso petshop!!"


class Pet:
    def __init__(self, tipo=None):
        print(" -------Dados do pet adotado-------")
        if tipo is None:
            tipo = input("Digite o tipo do Pet que você deseja adotar: ")
        self.tipo = tipo

    def apresentar1(self) -> str:
        return f"Tipo do Pet que deseja: {self.tipo}"


class Animal(Pet):
    def __init__(self, tipo=None, nome=None, idade=None, raca=None):
        if nome is None:
            nome = input("Digite o nome do seu Pet: ")
        if idade is None:
            idade = int(input("Digite a idade do Pet: "))
        if raca is None:
            raca = input("Digite a raça do seu Pet: ")

        super().__init__(tipo)
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def apresentar(self) -> str:
        return f"Nome que você deu ao Pet foi: {self.nome}, a Idade dele é: {self.idade}, e a Raça é: {self.raca}"


class Funcionario:
    def __init__(self, adotante, animal):
        print("-----Confirmação de dados-----")
        self.nomea = adotante.nomea
        self.cpf = adotante.cpf
        self.idadea = adotante.idadea
        self.tipo = animal.tipo
        self.nome = animal.nome
        self.idade = animal.idade
        self.raca = animal.raca

    def apresentar(self):
        print(f"Adotante: {self.nomea}, CPF: {self.cpf}, Idade: {self.idadea}")
        print(f"Nome do Pet é: {self.nome}, a idade do Pet é {self.idade} anos, a Raça do Pet é: {self.raca}, e o Tipo é: {self.tipo}")
        return "Essas informações estão corretas?"
     
