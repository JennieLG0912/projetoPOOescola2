class Pessoa:
    def __init__(self,nome , idade = 0):
        self.__nome = nome 
        self.__idade = idade
        
    @property
    def num(self):
        return self.__num 
    @num.setter
    def num(self, valor):
        if valor >= 0:
            self.__num = valor
        else:
            print("Erro: o numero da casa nao pode ser negativo! ")

num2 = Casa(1780) 
print("O numero da sua casa é:", num2.num)

num2.num = - 1780
print("Numero da casa apos tentativa: ", num2.num)


print("--------------------------------------------------------")

class Casa:
    def __init__(self, num = 0):
        self.__num = num

    @property
    def num(self):
        return self.__num 
    @num.setter
    def num(self, valor):
        if valor >= 0:
            self.__num = valor
        else:
            print("Erro: o numero da casa nao pode ser negativo! ")

num2 = Casa(1780) 
print("O numero da sua casa é:", num2.num)

num2.num = - 1780
print("Numero da casa apos tentativa: ", num2.num)

