
print("")
print("2020..."
      "\nO ano que marcou a história da Humanidade. A sociedade está em perigo e com risco de ser extinta. Mas você poderá  resolver esse problema.Estará em suas mãos escolhas que podem mudar o rumo da humanidade."
      "Respire fundo, concentre -se ,pois embarcaremos em uma história incrível onde você é o herói.")
print("")

nome = input("Qual é o seu nome? ")
print("")

print(nome,"está muito feliz porque passará o carnaval de 2020 em Búzios.Com sua família, resolveu curtir o feriado de carnaval nas belas praias de búzios. Tomando água de coco, sorvetinho e comendo aquele maravilhoso camarãozinho."
      "\nMas algo TERRÍVEL aconteceu:")

algo_inacreditavel = int(input( "\n\nDiga o que de terrível aconteceu: "
                            "\n1 - Quebrou o pé correndo 1 dia antes da viagem." 
                            "\n2 - teve crise de sinusite.\n"))

if algo_inacreditavel == 1:
    resposta = "quebrou o pé correndo 1 dia antes da viagem."
else:
    resposta = "teve crise de sinusite."

print(f"\nPois bem, é isso mesmo que aconteceu. {nome}, {resposta}"
      f"Devido a esse problema,teve que ficar em casa e não pode viajar com sua família.\n"
      f"Para não ficar no ócio,{nome} bolou uma ideia do que fazer em casa durante o feriado.")
print(f"\nQual ideia {nome} bolou?")

ideia = int(input(
                  "\n1 - Maratonar as 2 temporadas de The Umbrella Academy e The Boys."
                  "\n2 - Jogar Demon's Soul até zerar\n"
                  ))
if ideia == 1:
    resposta = "maratonar as 2 temporadas de The Umbrella Academy e The Boys"
else:
    resposta = "jogar Demon's Soul até zerar"
print (f"\n {nome},bolou que iria",resposta,"durante todo o feriado de carnaval."
      "Queria amenizar a dor de ficar em casa em pleno feriado."
       )

print (
     "\nSua mãe ficou bem triste, então resolveu ficar em casa para ajudar no que precisar."
     f"{nome} não concordou com a ideia e pediu para que sua mãe fosse viajar, pois não poderia perder a oportunidade de conhecer as lindas praias de Búzios."
     f"\nEntão, chegou o dia 21 de fevereiro e sua família foi viajar.Momento difícil para {nome}, mas ficou confortado porque sua familia conheceria um lugar fenomenal." )










