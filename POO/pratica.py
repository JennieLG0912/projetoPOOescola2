def cadastro():
    ano = int(input("Qual o ano do seu carro :"))
    modelo = input("Qual o modelo dele: ")
    cor = input("Qual a cor dele: ")

    print("O ano do seu carro é: ", ano)
    print("O modelo carro é: ", modelo)
    print("A cor do seu carro é: ", cor)

    if ano >= 2015:
        print("seu carro e seminovo")
    else:
        print("Seu carro e velho")

cadastro()