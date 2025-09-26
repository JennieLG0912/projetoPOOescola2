class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} Km/h!")

    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - " f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")

moto1 = Moto("Honda", "XRE Sahara 300", 2025, "Vermelha")
moto2 = Moto("Honda", "África Twin 1100", 2025, "Preta")

print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(200)
moto2.acelerar(216)

moto1.frear(130)
moto2.frear(116)

print(moto1.detalhes())
print(moto2.detalhes())

if  moto1.velocidade < moto2.velocidade:
   print("A África Twin 1100 ganhou a corrida")
else:
    print("A XRE Sahara 300 ganhou a corrida")