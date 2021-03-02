def passo_1():
   pergunta_3 = int(input(
                 
                       "Surge um estudo que na mata Amazônica há uma planta chamada Xirus que pode ser a cura."
                       "\nVocê vai até lá verificar qual planta é?"
                       "\n1- sim."
                       "\n2 - não.\n"))
   while True:
         if pergunta_3 == 1 or pergunta_3 ==2:
             break
         else:
             print("Valor inválido. Por favor, digite novamente.\n")
             pergunta_3 = int(input(
                 
                    "Surge um estudo que na mata Amazônica há uma planta chamada Xirus que pode ser a cura."
                    "\nVocê vai até lá verificar qual planta é?"
                    "\n1- sim."
                    "\n2 - não.\n"))
            
   if pergunta_3 ==1:
      pergunta_4 = int(input(
               "Realmente há indícios de ser a cura. Você deseja coletar e levar até o centro de pesquisa?"
               "\n1 - sim."
               "\n2 - Não\n:"
          
            ))
      while True:
         if pergunta_4 == 1 or pergunta_4 ==2:
             break
         else:
             print("\nValor inválido. Favor repita a ação!")
             pergunta_4 = int(input(
                                "\nRealmente há indícios de ser a cura. Você deseja coletar e levar até o centro de pesquisa?"
                                "\n1 - sim."
                                "\n2 - Não.\n:"))

      if pergunta_4 == 1:
          print("\nInfelizmente concluísse que não há eficácia!")
        
      else:
          print("\nOk!")
   else:
      print("Ok!")
def acao_1():
    pergunta_1 = int(input(
                     "\nQual o próximo passo?"
                     "\n1 - Obrigar a todos os Estados façam Lockdown por 20 dias e preparar uma equipe p/ que estude vírus" "e busque a cura?"
                     "\n2 - Não fazer Lockdown e preparar uma equipe para que se estude sobre o vírus e busque a cura.\n:"
                     ))
    while True:
        if pergunta_1 == 1 or pergunta_1 ==2:
               break
        else:
               print("\nValor inválido!\n")
               pergunta_1 = int(input(
                     "\nFavor, diga qual o próximo passo?"
                     "\n1 - Obrigar a todos os Estados façam Lockdown por 20 dias e preparar uma equipe p/ que estude vírus" "e busque a cura?"
                     "\n2 - Não fazer Lockdown e preparar uma equipe para que se estude sobre o vírus e busque a cura.\n:"
                     ))
    print("\nVocê viajou até o RJ onde está o Centro de pesquisa do estudo da Jacaris2020.\n")

    pergunta_2 = int(input(
                            "\nO pesquisador Átila Tamarindo informou que os estudos estão avançando, mas que precisaria de mais investimento."
                        "\nO que você diz?"
                        "\n1-Ok, investirei 4 bilhoes."
                        "\n2- Não temos como investir, precisamos encontrar parceiros.\n:"))
    while True:
        if pergunta_2 == 1 or pergunta_2 ==2:
            break
        else:
            print("\nValor inválido!\n")
            pergunta_2 = int(input(
                            "\nO pesquisador Átila Tamarindo informou que os estudos estão avançando, mas que precisaria de mais" "investimento."
                        "\nO que você diz?"
                        "\n1-Ok, investirei 4 bilhoes."
                        "\n2- Não temos como investir, precisamos encontrar parceiros.\n:"))
    if pergunta_2 ==1:
        print("\nÓtima escolha!")
        print("O Lockdown surge efeito e a taxa de transmissão vem diminuindo.\n")
        passo_1()
    else:
        print("\nEscolha complicada!")
        print("O ministério não consegue investidor.\nO virus chega a outros países.\n")
        passo_1()


    pergunta_5 = int(input(
                            "\nSurge outra fonte que poderá se a cura. Uma planta chamada empatia, que está no interior do Acre. Ir até lá para verificar e coletar?"
                            "\n1 - Sim."
                            "\n2 - Não.\n:"))
    while True:
        if pergunta_5 == 1 or pergunta_5 ==2:
            break
        else:
            print("Valor inválido. Favor digitar novamente.\n")
            pergunta_5 = int(input(
                            "\nSurge outra fonte que poderá se a cura. Uma planta chamada empatia, que está no interior do Acre. Ir até lá para verificar e coletar?"
                            "\n1 - Sim."
                            "\n2 - Não.\n:"))

    if pergunta_5 ==1 and pergunta_1 ==2 and pergunta_2 ==2:
        print(
            "Você achou a cura, mas o vírus se espalhou pelo planeta!"
            "\nVocê perdeu!\n")
    elif pergunta_5 ==1 and pergunta_1==1 and pergunta_2 ==1:
        print("VocÊ achou a cura e o virus não se espalhou! Você venceu!!!!!\n")
    elif pergunta_5 ==2 and pergunta_1 ==2 and pergunta_2==2:
        print("Infelizmente essa era sua ultima chance. Não conseguimos a cura e o virus se espalhou pelo planeta.")
        print("\nVocê PERDEU!")
    elif pergunta_5 ==2 and pergunta_1 == 1 and pergunta_2 ==1:
        print("Apesar do virus não se  espalhar, essa era a sua ultima chance de achar cura! Você perdeu!")
        print("\nVocê PERDEU!")
    elif pergunta_5 ==1 and pergunta_1 ==1 and pergunta_2 ==2:
        print("Você achou a cura, mas o vírus se espalhou pelo planeta!")
        print("\nVocê PERDEU!")
    elif pergunta_5 == 1 and pergunta_1 == 2 and pergunta_2 ==1:
        print("Você achou a cura, mas o vírus se espalhou pelo planeta!")
        print("\nVocê PERDEU!")
    elif pergunta_5 ==2 and pergunta_1 == 2 and pergunta_2 ==1:
        print("Infelizmente essa era sua ultima chance. Não conseguimos a cura e o virus se espalhou pelo planeta.")
        print("\nVocê PERDEU!")
    else:
        print("Infelizmente essa era sua ultima chance. Não conseguimos a cura e o virus se espalhou pelo planeta.\n")
        print("\nVocê PERDEU!")      
def criar(x):
    print("\nOk!Você viajou até o RJ para conhecer o Centro de pesquisas que foi criado e entender mais do Vírus.")
    pergunta_3 = int(input(
                           "Átila Tamarindo, médico responsável pelos estudos da Jacaris2020, informou que os estudos estão avançando, mas que precisaria de mais investimento. Precisamente 4Bilhões."
                           "\n1 - Investir 4 Bilhões."
                           "\n2 - Não investir e tentar buscar parceiros."
    ))
    while True:
        if pergunta_3 == 1 or pergunta_3 ==2:
            break
        else:
            print("\nValor inválido! Por favor, responda com 1 ou 2.\n")
            pergunta_3 = int(input(
                           "Átila Tamarindo, médico responsável pelos estudos da Jacaris2020, informou que os estudos estão avançando, mas que precisaria de mais investimento. Precisamente 4Bilhões."
                           "\n1 - Investir 4 Bilhões."
                           "\n2 - Não investir e tentar buscar parceiros."))

    if pergunta_3 == 1:
        print("\nSurge um estudo que no interior da Bahia há uma planta chamada Rosa Braca como possível cura.")
        pergunta_4 = int(input(
                            "\nVocê quer ir lá verificar?"
                            "\n1 - sim."
                            "\n2 - não."
                            ))
        while True:
            if pergunta_4 == 1 or pergunta_4 ==2:
                break
            else:
                print("\nValor inválido! Por favor, responda com 1 ou 2.\n")
                pergunta_4 = int(input(
                                "\nVocê quer ir lá verificar?"
                                "\n1 - sim."
                                "\n2 - não."
                    ))

        if pergunta_4 == 1:
            print("Ok! Há indícios.Vamos levar para o Centro.")
            print("")
            print("Infelizmente não foi eficaz. Não é a cura. :(")
            pergunta_6 = int(input(
                        "\nSurge outro estudo que a Água de uma Nascente chamada Esperança em Petrópolis como possível cura. Você que ir lá verificar?"
                        "\n1- Sim."
                        "\n2 - Não."
            ))
    
            if pergunta_6 == 1 and x == 1:
                print("Realmente há indícios!")
                print("O centro de pesquisa informou que Realmente é a Cura.")
                print("Você venceu!")
            elif pergunta_6 ==2 and x == 2:
                print("Infelizmente não foi possível achar a cura a tempo!")
                print("O Vírus se espalhou pelo planeta.")
                print("Você virou jacaré!")
                print("Você perdeu.")
            elif pergunta_6 ==1 and x == 2:
                print("Você achou a cura, mas o virou se espalhou!")
                print("Você virou jacaré!")
                print("Você perdeu!")
            else:
                print("Infelizmente não foi possível achar a cura a tempo!")
                print("O Vírus se espalhou pelo planeta.")
                print("Você virou jacaré!")
                print("Você perdeu.")
        else:
            print("Ok")
            pergunta_6 = int(input(
                        "\nSurge outro estudo que a Água de uma Nascente chamada Esperança em Petrópolis como possível cura. Você que ir lá verificar?"
                        "\n1- Sim."
                        "\n2 - Não."
             ))
    
            if pergunta_6 == 1 and x == 1:
                print("Realmente há indícios!")
                print("O centro de pesquisa informou que Realmente é a Cura.")
                print("Você venceu!")
            elif pergunta_6 ==2 and x == 2:
                print("Infelizmente não foi possível achar a cura a tempo!")
                print("O Vírus se espalhou pelo planeta.")
                print("Você virou jacaré!")
                print("Você perdeu.")
            elif pergunta_6 ==1 and x == 2:
                print("Você achou a cura, mas o virou se espalhou!")
                print("Você virou jacaré!")
                print("Você perdeu!")
            else:
                print("Infelizmente não foi possível achar a cura a tempo!")
                print("O Vírus se espalhou pelo planeta.")
                print("Você virou jacaré!")
                print("Você perdeu.")
                    
    else:
        print("\nInfelizmente Não conseguimos parceiros.")
        print("\nO vírus acabou se espalhando!")
        print("\nVocê virou Jacaré")
        print("\nVocê perdeu!")
def acao_2():
    print("\nOk! Poucas pessoas atenderam ao pedido de ficar em casa.O vírus começou a se espalhar pelo Brasil.")
    pergunta_1 = int(input(
                        "\nQual o próximo passo?"
                        "\n1-Lockdown de 20 dias em TODO o Brasil e preparar uma equipe para estudo do Jacaris2020."
                        "\n2- Não fazer Lockdown e preparar uma equipe para estudo do Jacaris2020."
                            ))
    while True:
        if pergunta_1 == 1 or pergunta_1 ==2:
            break
        else:
            print("\nValor inválido!\n")
            pergunta_1 = int(input(
                    "\nPor favor, diga qual o próximo passo?"
                    "\n1-Lockdown de 20 dias em TODO o Brasil e preparar uma equipe para estudo do Jacaris2020."
                    "\n2- Não fazer Lockdown e preparar uma equipe para estudo do Jacaris2020."
                            ))
               
    
    pergunta_2 = int(input(
                        "O Ministério da Saúde decidiu criar um Centro de Pesquisa da Jacaris2020 na Universidade do Estado do RJ e pediu seu aval."
                        "Você deseja criar o Centro de Pesquisa no RJ ou deseja pedir ajuda do Centro de Pesquisa do EUA?"
                        "\n1- Pedir ajuda do Centro de pesquisas EUA."
                        "\n2- Criar o Centro de Pesquisas no RJ."
                        ))
    while True:
        if pergunta_2 == 1 or pergunta_2 ==2:
            break
        else:
            print("\nValor inválido! Por favor, responda com 1 ou 2.\n")
            pergunta_2 = int(input(
                    "O Ministério da Saúde decidiu criar um Centro de Pesquisa da Jacaris2020 na Universidade do Estado do RJ e pediu seu aval."
                    "Você deseja criar o Centro de Pesquisa no RJ ou deseja pedir ajuda do Centro de Pesquisa do EUA?"
                    "\n1- Pedir ajuda do Centro de pesquisas EUA."
                    "\n2- Criar o Centro de Pesquisas no RJ."
                        )) 

    if pergunta_2 ==1:
        print("Chegando lá, Dr.Obama Trump disse que infelizmente os estudos irão demorar para avançar.")
        print("")
        pergunta_5 = int(input(
                            "Você sabe que o tempo é curto e que a demora pode custar caro.O que você faz?"
                            "\n1 - Aceita e espera?"
                            "\n2 - Manda Criar o centro no RJ."
                            ))
        while True:
            if pergunta_5 == 1 or pergunta_5 ==2:
                break
            else:
                print("\nValor inválido! Por favor, responda com 1 ou 2.\n")
                pergunta_5 = int(input(
                                "Você sabe que o tempo é curto e que a demora pode custar caro.O que você faz?"
                                "\n1 - Aceita e espera?"
                                "\n2 - Manda Criar o centro no RJ."
                            ))

        if pergunta_5 == 1:
            print("")
            print("Infelizmente os EUA demoraram demais e o vírus se espalhou.")
            print("Você acabou virando Jacaré!")
            print("Você perdeu!")

        else:
            resul_pergunta_1 = pergunta_1
            criar(resul_pergunta_1)
    else:
        resul_pergunta_1 = pergunta_1
        criar(resul_pergunta_1)





print("\nA Humanidade corre o risco de ser transformada.Um Plano Maléfico do Dr Bobonaro de transformar a sociedade em Jacarés está sendo implantado. O Vírus está se espalhando pelo Brasil, mas você poderá deter. Suas escolhas poderão lhe tornar um herói ou heroína.\nNeste jogo você poderá escolher entre 3 personagens:\n")
escolha = int(input(
                  "Digite o número correspondente do personagem que você quer:"
                  "\n1) Dr. Odisvaldo Cruz - Graduado em Biologia, Mestre em Microbilogia ambos pela Universidade Federal da" "Bahia. Doutor em Genética Molecular e de Micro - organismos por Harvard."
                  "\n2) Dra. Alessya Bonay -  Graduada em Medicina pela Universidade Federal do Rio de Janeiro. Mestre em" "MIcrobiologia pela Universidade do Estado do Rio de Jneiro. Doutora em Ciências Biométicas pela Stanford" "University."
                  "\n3) Dr Nelson Tati - Graduado em Medicina pela Universidade Federal do Acre. Mestre e Doutor em Ciências" "Biomédicas pela University of Portsmouth.\n:"
                ))
while True:
    if escolha == 1 or escolha == 2 or escolha ==3:
        break
    else:
        print("\nInválido! Digite 1 , 2 ou 3!")
        escolha = int(input(
                  "\nDigite o número correspondente do personagem que você quer:"
                  "\n1) Dr. Odisvaldo Cruz - Graduado em Biologia, Mestre em Microbilogia ambos pela Universidade Federal da" "Bahia. Doutor em Genética Molecular e de Micro - organismos por Harvard."
                  "\n2) Dra. Alessya Bonay -  Graduada em Medicina pela Universidade Federal do Rio de Janeiro. Mestre em" "MIcrobiologia pela Universidade do Estado do Rio de Jneiro. Doutora em Ciências Biométicas pela Stanford" "University."
                  "\n3) Dr Nelson Tati - Graduado em Medicina pela Universidade Federal do Acre. Mestre e Doutor em Ciências" "Biomédicas pela University of Portsmouth.\n:"
                ))

if escolha == 1:
    nome = "Dr. Odisvaldo Cruz"
elif escolha == 2:
    nome = "Dra. Alessya Bonay"
else:
    nome = "Dr Nelson Tati"
print(f"\nMaravilha! Então você será {nome}!")

continuar = input("\nSe você deseja continuar, aperte ENTER:")
while True:
    if continuar == "":
        break
    else:
        continuar = input("Para continuar você precisa apertar ENTER!")
print("\nTudo começou em fevereiro de 2020 quando médicos brasileiros descobrem que um vírus está circulando pelo Brasil transformando as pessoas em répteis.Especificamente em JACARÉS! Já se sabe o criador desse vírus, Dr Bobonaro Jayme. Ele fez essa revelação em um vídeo publicado no Youtube e suicidou - se logo após a revelação.\nVocê foi convidado pelo Presidente do Brasil, Tancredu Neives, e terá o papel de DETER que esse vírus SE ESPALHE pelo Brasil e pelos outros países transformando a Humanidade em Jacarés.\n")

acao = int(input(
            f"Qual a primeira ação {nome}  deseja tomar?"
            "\n1 - Fechar as fronteiras e divisas."
            "\n2 - Dar um comunicado em rede Nacional para que as pessoas fiquem em casa.\n:"
        ))
while True:
    if acao == 1 or acao == 2:
        break
    else:
        print("\nInválido! Você precisa digitar 1 ou 2.")
        acao = int(input(
            f"Diga qual a primeira ação {nome}  deseja tomar?"
            "\n1 - Fechar as fronteiras e divisas."
            "\n2 - Dar um comunicado em rede Nacional para que as pessoas fiquem em casa.\n:"))
if acao ==1:
    acao_1()
else:
    acao_2()
