meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BRO": "Un amigo",
            "BUGUEADA": "Que está trabado",
            "CREEPY": "Algo que da miedo"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Busca esa palabra en Google. Y si no la encuentras no es mi problema")
