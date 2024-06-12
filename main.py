meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "aterrador, siniestro",
            "BRO": "para referirse a un amigo o alguien de confianza",
            "SHIPPEAR": "Emparejar a dos personas por razones subjetivas",
            "HATER":  "Personas que odian algo y que hacen todo lo posible por echarlo abajo.",
            "SPOILER": "Es aquel que no pierde la oportunidad para anticipar de forma intencional datos o noticias importantes",
            "EZ": "Expresa que un juego o algo es facil",
            }
            
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme_dict.keys():
    print(meme_dict[palabra])
else:
    print("Lo siento esta palabra no se encuentra en el diccionario")
