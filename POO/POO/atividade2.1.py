def cadastroacademia():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    numero = input("Digite seu numero para contato: ")
    altura = input("Digite sua altura: ")
    peso = input("Digite seu peso: ")
    idade = int(input("Digite sua idade: "))
       

    print("\n--- Ficha de cadastro ---")
    print("seu nome é : ", nome)
    print("seu cpf é: ", cpf)
    print("seu numero para contato é:", numero)
    print("sua altura é: ", altura )
    print("seu peso é: ", peso )
    print("sua idade é: ", idade)

    if idade < 18:
        print(" Voce é menor de idade, nao pode fazer academia")
    else:
        print("Voce é maior de idade, esta apropriado para fazer academia.Agradeçemos sua preferencia, mais tarde irá receber sua ficha de treino") 

cadastroacademia()

