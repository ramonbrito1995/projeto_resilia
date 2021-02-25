
print("")
print("2020...")
print("O ano que marcou a história da Humanidade. A sociedade está em perigo e com risco de ser extinta. Mas você poderá resolver esse problema. Estará em suas mãos escolhas que podem mudar o rumo da humanidade."
      "Respire fundo e concentre - se,pois embarcaremos em uma história incrível onde você é o herói.")
print("")

nome = input("Qual é o seu nome? ")
print("")

print(nome,"está muito feliz porque passará o carnaval de 2020 em Búzios. Ele e seu amigo Leo, resolveram curtir o feriado de carnaval nas belas praias de búzios. Tomando água de coco, sorvetinho e comendo aquele camarão maravilhoso."
      "\nMas algo INACREDITÁVEL aconteceu:")

algo_inacreditavel = int(input( "\n\nDiga o que de inacreditável aconteceu: "
                            "\n1 - quebrou o pé correndo 1 dia antes da viagem."
                            "\n2 - Deixou a panela no fogo e sua casa pegou fogo." 
                            "\n3 - Teve uma crise de gastrointerite.\n"))

if algo_inacreditavel == 1:
    resposta = "quebrou o pé correndo 1 dia antes da viagem."
elif algo_inacreditavel == 2:
    resposta = "Deixou a panela no fogo e sua casa pegou fogo."
else:
    resposta = "Teve uma crise de gastrointerite."

print("\nPois bem, é isso mesmo que aconteceu.",nome,resposta)
print("\nDevido a esse problema,",nome,"teve que ficar em casa e não pode viajar com Léo.")






