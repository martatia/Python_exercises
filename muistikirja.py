#Työssä rakennetaan muistikirja, joka käyttää merkintöjen hallintaan Pythonin lista-tietorakennetta
# sekä tallentaa muistikirjan bittimuotoisena tietokoneen levylle. Ohjelmassa on seuraavat ominaisuudet:
# A) Ohjelmaan voidaan lisätä merkintöjä, joissa on samanlainen aikaleima kuin aiemmin.
# B)Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
# C)Ohjelmalla voi poistaa yksittäisen merkinnän listalta, sekä
# D)Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa.

# Ohjelma käyttää tietokantanaan tiedostoa nimeltä "muistio.dat". 
# Käynnistyessään ohjelma koittaa ladata aiemmin luodun listan ko. tiedostosta, 
# tai mikäli tällaista ei ole olemassa tai sen lataaminen tuottaa virheen, 
# luo uuden ilmoittaen "Virhe tiedostossa, luodaan uusi muistio.dat."

import pickle
import time

kello = time.strftime("%X %x")


def luoda():
    try:
        tiedosto = open("muistio.dat", "r")
        tiedosto.close()
        nimi = tiedosto.name
        return nimi
    except Exception:
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
        uusi = open("muistio.dat", "w")
        uusi.close()


def main():
    file0 = luoda()
    file1 = luoda()
    lista = []

    while True:
        print(
            "(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta")
        valinta = int(input("\nMitä haluat tehdä?: "))

        if valinta == 5:
            tiedosto = open(file1, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
            print("Lopetetaan.")
            break

        elif valinta == 1:
            for i in lista:
                print(i)

        elif valinta == 2:
            texti = input("Kirjoita uusi merkintä: ")
            koko_tiedosto = texti + ":::" + kello
            lista.append(koko_tiedosto)

        elif valinta == 3:
            print("Listalla on", len(lista), "merkintää.")
            muutos = int(input("Mitä niistä muutetaan?: "))
            print(lista[muutos - 1])
            texti1 = input("Anna uusi teksti: ")
            koko_tiedosto1 = texti1 + ":::" + kello
            lista.insert(muutos - 1, koko_tiedosto1)
            lista.pop(muutos)

        elif valinta == 4:
            print("Listalla on", len(lista), "merkintää.")
            poisto = int(input("Mitä niistä poistetaan?: "))
            print("Poistettiin merkintä", lista[poisto - 1])
            lista.pop(poisto - 1)


if __name__ == "__main__":
    main()