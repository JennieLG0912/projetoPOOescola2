class SerVivo: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def respirar(self):
        print(f"{self.nome} está repirando..." )

    def dormir(self):
        print(f"{self.nome} está dormindo..." )

class Pessoa(SerVivo):
    def falar( self, mensagem):
        print(f"{self.nome} diz: {mensagem}")    

    def andar( self, destino):
        print(f"{self.nome} está andando até {destino}.")

    def comer( self, comida):
        print(f"{self.nome} está comendo {comida}.")


# Criando objetos 
p1 = Pessoa ("Jennifer", 16)
p2 = Pessoa("LG",16)

#Chamando ações
p1.respirar()
p1.falar("oiee")
p1.andar("a academia")
p1.comer("um bolo confeitado muito ruim")

print("------")
p2.dormir()
p2.falar("estou enchendo o saco da Jennifer!")
