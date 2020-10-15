#tehdään peli Jalka-Torakka-Ydinpommi. Ohjelma pyytää käyttää valitseman jalan, torakan tai ydinpommin,
# ja tämän jälkeen arpoo tietokoneelle oman vastauksen. Jalka voittaa torakan, ydinpommi voittaa jalan
# ja torakka voittaa ydinpommin. Jos pelaaja ja tietokone valitsee saman, on kyseessä tasapeli
# (vaikka oikeastaan molempien valitessa ydinaseen kaikien pitäisi hävitä :) ). Tee ohjelmaan lisäksi laskurit,
# jotka kertovat kuinka monta kierrosta peliä on pelattu, kuinka monesti pelaaja voitti ja montako tasapeliä pelattiin.

# Jos pelaaja voittaa, tulostetaan "Voitit!", jos häviää niin "Hävisit!".
# Tasapelillä tulostetaan "Tasapeli!" ja pelin loppuessa, kun pelaaja valitsee "Lopeta",
# tulostetaan "Pelasit [kierrosmäärä] kierrosta, joista voitit [voitot] ja pelasit tasan [tasapelit] peliä.".

import random

def valinta():
    luku = random.randint(0, 2)

    if luku == 1:
        return "Jalka"
    elif luku == 2:
        return "Ydinase"
    else:
        return "Torakka"

def main():
    kierroksia = 0
    voitot = 0
    tasapelit = 0
    while True:
        syote = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
        tietokone = valinta()
        if syote == "Lopeta":
            break
        elif syote == "Jalka":
            print("Sinä valitsit:", syote)
            tietokone = valinta()
            print("tietokone valitsi:", tietokone)
            if syote == tietokone:
                print("Tasapeli!")
                tasapelit += 1
            elif tietokone == "Torakka":
                print("Voitit!")
                voitot += 1
            else:
                print("Hävisit!")

        elif syote == "Ydinase":
            print("Sinä valitsit:", syote)
            print("tietokone valitsi:", tietokone)
            if syote == tietokone:
                print("Tasapeli!")
                tasapelit += 1
            elif tietokone == "Jalka":
                print("Voitit!")
                voitot += 1
            else:
                print("Hävisit!")

        elif syote == "Torakka":
            print("Sinä valitsit:", syote)
            print("tietokone valitsi:", tietokone)
            if syote == tietokone:
                print("Tasapeli!")
                tasapelit += 1
            elif tietokone == "Ydinase":
                print("Voitit!")
                voitot += 1
            else:
                print("Hävisit!")

        kierroksia += 1

    print("Pelasit", kierroksia, "kierrosta, joista voitit", voitot, "ja pelasit tasan", tasapelit, "peliä.")

if __name__ == "__main__":
    main()