meme_dict = {
    "LOL" : "una respuesta a algo gracioso",
    "CRINGE" : "algo raro o embarazoso",
    "CREEPY" : "aterrador, siniestro",
}

word = input("Que palabra no entiendes? (Escribe con mayusculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No conozco esa palabra")
