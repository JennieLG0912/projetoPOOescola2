class Carro:
    def __init__(self, cor=None, estilo=None, marca=None, modelo=None):
        self.cor = cor
        self.estilo = estilo 
        self.marca = marca
        self.modelo = modelo
         

    def descrever(self):
        self.cor = input("Qual a cor do carro? " )
        self.estilo = input("Qual o estilo do carro? ")
        self.marca = input("Qual a marca do carro? ")
        self.modelo = input("Qual o modelo do carro? ")
        
        return f"A cor do carro é {self.cor}, o estilo do carro é {self.estilo}, a marca do carro é{self.marca} e o modelo do carro é {self.modelo}"

cr = Carro()
print(cr.descrever())
