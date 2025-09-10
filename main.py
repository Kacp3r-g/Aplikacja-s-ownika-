meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego"
}

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict:   # check if the word exists in the dictionary
    print(meme_dict[word])  # print its definition
else:
    print("Niestety, tego słowa nie ma w słowniku :(")
