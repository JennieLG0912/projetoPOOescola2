class Pet:
    def __init__(self, tipo = None):
        if tipo is None:
            tipo = input("Digite o tipo do seu Pet: ")
        self.tipo=tipo
      
    def apresentar(self) -> str:
        return f"O tipo do Pet é {self.tipo}"
    
class Animal(Pet):
    def __init__(self,tipo=None, nome = None, idade = None, raca = None):
        if tipo is None:
            tipo = input("Digite o tipo do seu Pet: ")
        if nome is None:
            nome = input("Digite o nome do seu Pet:")
        if idade is None:
            idade = input("Digite a idade do Pet: ")
        if raca is None:
            raca = input("Digite a raça do seu pet: ")
        
        
        super().__init__(tipo)
        self.nome=nome
        self.idade = idade
        self.raca = raca
        

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base}, nome do pet é {self.nome} a idade do seu pet é {self.idade}, a raça do seu pet é {self.raca}"
