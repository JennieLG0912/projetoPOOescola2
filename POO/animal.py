class Animal:
    def __init__(self, nome ):
        self.nome = nome 

    def falar(self): 
        print("Som do animal")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")    

class Gato(Animal):
    def falar(self):
        print("Miau!")


dog = Cachorro("Marcão")
cat = Gato("Preciosa")

dog.falar()
cat.falar()