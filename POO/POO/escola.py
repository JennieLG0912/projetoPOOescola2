def escola():
    area = int(input(" Qual sua area? \n1-Aluno\n 2-Professor\nEscolha: "))
    if area == 1:
        print("Você é um aluno, realize seu cadastro")

        def cadastroAluno():
            nome = input("Qual seu nome:")
            idade = input("Qual sua idade: ")
            cpf = input("Qual seu cpf: ")
            rg = input("Digite seu RG: ")
            nomep = input("Digite o nome do seu pai: ")
            nomem = input("Digite o nome da sua mãe: ")
            dtn = input("Digite sua data de nascimento: ")
            curso = int(input("qual seu curso? \n1-Desenvolvimento de Sistema\n2-Enfermagem\n3-Administração\n4-Finanças\nescolha: "))

            print("Seu nome é: ", nome)
            print("Sua idade é: ", idade)
            print("Seu CPF é: ", cpf)
            print("Seu RG é: ", rg)
            print("Nome do seu pai é: ", nomep)
            print("Nome da sua mãe é: ", nomem)
            print("Sua Data de Nascimento é: ", dtn)
            print("Seu curso é ", curso)
            if curso ==1:
                print("Seu curso e DS-Desenvolvimento de Sistema ")
            if curso == 2:
                print("Seu curso e ENF-Enfermagem ")
            if curso == 3:
                print("Seu curso e ADM-Administração ")    
            if curso == 4:
                print("Seu curso e FN-Finanças ")
        cadastroAluno()
    if area == 2:    
        def cadastroProf():
            nome = input("Qual seu nome:")
            idade = input("Qual sua idade: ")
            cpf = input("Qual seu cpf: ")
            rg = input("Digite seu RG: ")
            dtn = input("Digite sua data de nascimento: ")
            fa = int(input("qual sua formação acadêmica? \n1-Desenvolvimento de Sistema\n2-Enfermagem\n3-Administração\n4-Finanças\nescolha: "))
        cadastroProf()


escola()
