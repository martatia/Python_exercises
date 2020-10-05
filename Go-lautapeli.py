# Tehtävä:
# Go-pelissä lisätään vuorotellen mustia ja valkoisia kiviä pelilaudalle. 
# Pelin voittaa se pelaaja, jolla on enemmän kiviä laudalla pelin lopuksi.
# Kirjoita funktio kumpi_voitti(pelilauta: list), joka saa parametrikseen kaksiulotteisen taulukon, joka kuvaa pelilautaa. 
# Taulukko koostuu kokonaisluvuista seuraavasti:
    #0: tyhjä ruutu
    #1: pelaajan 1 nappula
    #2: pelaajan 2 nappula
# Esimerkissä pelilaudan koko voi olla mikä tahansa.
# Funktio palauttaa arvon 1, jos pelaaja 1 on voittanut pelin, ja arvon 2, jos pelaaja 2 on voittanut pelin. 
# Jos molemmilla pelaajilla on yhtä paljon nappuloita laudalla, funktio palauttaa arvon 0.

def kumpi_voitti(pelilauta: list):
    ykkoset=0
    nollat=0
    kakoset=0
    for x in pelilauta:
        for a in x:
            if a==0:
                nollat+=1
            elif a==1:
                ykkoset+=1
            elif a==2:
                kakoset+=1
    if ykkoset==kakoset:
        return 0
    elif ykkoset>kakoset:
        return 1
    elif kakoset>ykkoset:
        return 2

if __name__=="__main__":
    lauta= [
        [1, 0, 0, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 1, 0, 0],
        [0, 2, 0, 2, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 2, 2, 0],
        [2, 0, 2, 0, 2, 0, 1, 0, 0],
        [0, 0, 2, 1, 0, 2, 2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 2],
        [2, 0, 0, 0, 0, 0, 0, 0, 1]
        ]
    print(kumpi_voitti(lauta))