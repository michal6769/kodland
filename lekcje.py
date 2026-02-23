
slownik = {
    "CRINGE": "Coś wyjątkowego dziwnego lub wstydliwego",
    "LOL": "odpowiedź na coś zabawnego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły",
    "APPLE": "jabłko",
    "CAR": "samochód",
    "CAT": "kot",   
}

word = input("Wpisz słwo, którego nie rozumiesz(używaj wielkich liter!): ") 

if word in slownik.keys():
    print(slownik[word])
else:
    print("Nie rozumiem tego słowa")
