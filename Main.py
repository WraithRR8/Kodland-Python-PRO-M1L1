meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "GANKAR": "Oferecer ajuda para outra lane passando fome",
            "FREEZAR": "Segurar os minions próximo a minha torre",
            "GIVAR": "Deixar um objetivo de lado",
            "AFK": "Abandonar o time, por que precisou sair",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Não há essa palavra no dicionário!")
