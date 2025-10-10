#Essa parte eu aprendi que self diz que daquilo que se fala se demonstra ser um objeto
#E o None ele representa a falta de valor 
class Casa:
    def __init__(self, cor = None, quartos = None, banheiros = None, tamanho = None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Qual a cor da casa? ")
        self.quartos = input("Quantos quartos tem a casa? ")
        self.banheiros = input("Quantos banheiros tem na sua casa? ")
        self.tamanho = input("Qual o tamanho da sua casa em m²? ")

        return f"esta casa é {self.cor}, tem {self.quartos} quartos, {self.banheiros} banheiros e {self.tamanho}m²."
    
cs = Casa()
print(cs.descrever())
