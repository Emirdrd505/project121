meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "FAKE": "şaşırtmak",
            "EZ": "kolay",
            "ROLEPLAY": "rol yapmak"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("kelime listede yok")
