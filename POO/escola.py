def escola():
    print("Bem-Vindo ao sistema de uma Escola Profissional")
    area = int(input("Qual sua area? \nDigite 1 para Aluno\nDigite 2 para Professor(a)\nDigite 3 para acessar a Biblioteca\nEscolha: "))
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
            curso = int(input("Qual seu curso? \n1-Desenvolvimento de Sistema\n2-Enfermagem\n3-Administração\n4-Finanças\nEscolha: "))


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
                print("Você concluiu seu cadastro")
                verN = int(input("Você gostaria de ver sua média?\n1-Sim\n2-Não\nDigite: "))
                if verN ==1:
                    n1 = int(input("Digite sua primeira nota: "))
                    n2 = int(input("Digite sua segunda nota: "))
                    n3 = int(input("Digite sua terceira nota: "))
                    n4 = int(input("Digite sua quarta nota: "))
                    media = (n1+n2+n3+n4)/4
                if media >=6:
                    print("Você foi aprovado, com a média: ", media)
                else:
                    print("Você foi reprovado, com a média: ", media)
            if curso == 2:
                print("Seu curso e ENF-Enfermagem ")
                print("Você concluiu seu cadastro")
                verN = int(input("Você gostaria de ver sua média?\n1-Sim\n2-Não\nDigite: "))
                if verN ==1:
                    n1 = int(input("Digite sua primeira nota: "))
                    n2 = int(input("Digite sua segunda nota: "))
                    n3 = int(input("Digite sua terceira nota: "))
                    n4 = int(input("Digite sua quarta nota: "))
                    media = (n1+n2+n3+n4)/4
                if media >=6:
                    print("Você foi aprovado, com a média: ", media)
                else:
                    print("Você foi reprovado, com a média: ", media)
            if curso == 3:
                print("Seu curso e ADM-Administração ")
                print("Você concluiu seu cadastro")
                verN = int(input("Você gostaria de ver sua média?\n1-Sim\n2-Não\nDigite: "))
                if verN ==1:
                    n1 = int(input("Digite sua primeira nota: "))
                    n2 = int(input("Digite sua segunda nota: "))
                    n3 = int(input("Digite sua terceira nota: "))
                    n4 = int(input("Digite sua quarta nota: "))
                    media = (n1+n2+n3+n4)/4
                if media >=6:
                    print("Você foi aprovado, com a média: ", media)
                else:
                    print("Você foi reprovado, com a média: ", media)    
            if curso == 4:
                print("Seu curso e FN-Finanças ")
                print("Você concluiu seu cadastro")
                verN = int(input("Você gostaria de ver sua média?\n1-Sim\n2-Não\nDigite: "))
                if verN ==1:
                    n1 = int(input("Digite sua primeira nota: "))
                    n2 = int(input("Digite sua segunda nota: "))
                    n3 = int(input("Digite sua terceira nota: "))
                    n4 = int(input("Digite sua quarta nota: "))
                    media = (n1+n2+n3+n4)/4
                if media >=6:
                    print("Você está aprovado, com a média: ", media)
                else:
                    print("Você está reprovado, com a média: ", media)
        cadastroAluno()
    if area == 2:    
        def cadastroProf():
            nome = input("Qual seu nome:")
            idade = input("Qual sua idade: ")
            cpf = input("Qual seu cpf: ")
            rg = input("Digite seu RG: ")
            dtn = input("Digite sua data de nascimento: ")
            fa = int(input("qual sua formação acadêmica?\n1-Desenvolvimento de Sistema\n2-Enfermagem\n3-Administração\n4-Finanças\nescolha: "))
            if fa ==1:
                print("Sua formação acadêmica e DS-Desenvolvimento de Sistema ")
            if fa == 2:
                print("Sua formação acadêmica e ENF-Enfermagem ")
            if fa == 3:
                print("Sua formação acadêmica e ADM-Administração ")    
            if fa == 4:
                print("Sua formação acadêmica e FN-Finanças ")
            print("Seu nome é: ", nome)
            print("Sua idade é: ", idade)
            print("Seu CPF é: ", cpf)
            print("Seu RG é: ", rg)
            print("Sua Data de Nascimento é: ", dtn)
            print("Sua formação acadêmica é: ", fa)
            verN = int(input("Você gostaria de ver a média do seu aluno?\n1-Sim\n2-Não\nDigite: "))
            if verN == 1:
                nomea = input("Digite o nome do seu aluno: ")
                n1 = int(input("Digite sua primeira nota: "))
                n2 = int(input("Digite sua segunda nota: "))
                n3 = int(input("Digite sua terceira nota: "))
                n4 = int(input("Digite sua quarta nota: "))
                media = (n1+n2+n3+n4)/4
            if media >=6:
                print("Seu aluno", nomea, "foi aprovado com a média: ", media)
            else:
                print("Seu aluno", nomea,"foi reprovado com a média: ", media)   
        cadastroProf()
    if area == 3:
        print("Bem-Vindo a Biblioteca! Deseja alugar um livro?")
        def biblioteca():
         livro = int(input("\nLivros disponiveis são:\n1- Três porquinhos\n2- Rua do Medo\n3- Harry Potter - A pedra filosofal\n4-Malala\n5- O Pequeno Príncipe\nEscolha: "))
         if livro == 1:
            print("Você escolheu Três Porquinhos, coloque seus dados ")
            nome = input("Digite seu nome: ")
            curso = int(input("qual seu curso?\n1 - DS\n2 - ADM\n3 - FN\n4 - ENF\n escolha: "))
            if curso == 1:
             print ("Seu nome é ", nome,"e seu curso é DS .LIvro alugado com sucesso!!")
            if curso == 2:
             print ("Seu nome é ", nome,"e seu curso é ADM .LIvro alugado com sucesso!!")
            if curso == 3:
             print ("Seu nome é ", nome,"e seu curso é FN .LIvro alugado com sucesso!!")
            if curso == 4:
             print ("Seu nome é ", nome,"e seu curso é ENF .LIvro alugado com sucesso!!")

         if livro == 2:
            print("Você escolheu Rua do Medo, coloque seus dados ")
            nome = input("Digite seu nome: ")
            curso = int(input("qual seu curso?\n1 - DS\n2 - ADM\n3 - FN\n4 - ENF\n escolha: "))
            if curso == 1:
             print ("Seu nome é ", nome,"e seu curso é DS .LIvro alugado com sucesso!!")
            if curso == 2:
             print ("Seu nome é ", nome,"e seu curso é ADM .LIvro alugado com sucesso!!")
            if curso == 3:
             print ("Seu nome é ", nome,"e seu curso é FN .LIvro alugado com sucesso!!")
            if curso == 4:
             print ("Seu nome é ", nome,"e seu curso é ENF .LIvro alugado com sucesso!!")

         if livro == 3:
            print("Você escolheu Harry Potter - A Pedra Filosofal, coloque seus dados ")
            nome = input("Digite seu nome: ")
            curso = int(input("qual seu curso?\n1 - DS\n2 - ADM\n3 - FN\n4 - ENF\n escolha: "))
            if curso == 1:
             print ("Seu nome é ", nome,"e seu curso é DS .LIvro alugado com sucesso!!")
            if curso == 2:
             print ("Seu nome é ", nome,"e seu curso é ADM .LIvro alugado com sucesso!!")
            if curso == 3:
             print ("Seu nome é ", nome,"e seu curso é FN .LIvro alugado com sucesso!!")
            if curso == 4:
             print ("Seu nome é ", nome,"e seu curso é ENF .LIvro alugado com sucesso!!")

         if livro == 4:
            print("Você escolheu Malala, coloque seus dados ")
            nome = input("Digite seu nome: ")
            curso = int(input("qual seu curso?\n1 - DS\n2 - ADM\n3 - FN\n4 - ENF\n escolha: "))
            if curso == 1:
             print ("Seu nome é ", nome,"e seu curso é DS .LIvro alugado com sucesso!!")
            if curso == 2:
             print ("Seu nome é ", nome,"e seu curso é ADM .LIvro alugado com sucesso!!")
            if curso == 3:
             print ("Seu nome é ", nome,"e seu curso é FN .LIvro alugado com sucesso!!")
            if curso == 4:
             print ("Seu nome é ", nome,"e seu curso é ENF .LIvro alugado com sucesso!!")

         if livro == 5:
            print("Você escolheu O Pequeno Príncipe, coloque seus dados ")
            nome = input("Digite seu nome: ")
            curso = int(input("qual seu curso?\n1 - DS\n2 - ADM\n3 - FN\n4 - ENF\n escolha: "))
            if curso == 1:
             print ("Seu nome é ", nome,"e seu curso é DS .LIvro alugado com sucesso!!")
            if curso == 2:
             print ("Seu nome é ", nome,"e seu curso é ADM .LIvro alugado com sucesso!!")
            if curso == 3:
             print ("Seu nome é ", nome,"e seu curso é FN .LIvro alugado com sucesso!!")
            if curso == 4:
             print ("Seu nome é ", nome,"e seu curso é ENF .LIvro alugado com sucesso!!")
        biblioteca()
escola()