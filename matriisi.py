# Kirjoita funktiot summa ja maksimi, jotka lukevat ja palauttavat nimensä mukaisesti matriisin 
# kaikkien alkioiden summan ja suurimman alkion.
# Kirjoita lisäksi funktio rivisummat, joka palauttaa listassa kaikkien matriisin rivien summat. 

def summa():
    lista=[]
    koko=[]
    with open("matriisi.txt") as file:
        for rivi in file:
            rivi = rivi.replace("\n", "")
            numero=rivi.split(",")
            for x in numero:
                x=int(x)
                lista.append(x)
            
    return sum(lista)
            

def maksimi():
    lista=[]
    koko=[]
    with open("matriisi.txt") as file:
        for rivi in file:
            rivi = rivi.replace("\n", "")
            numero=rivi.split(",")
            for x in numero:
                x=int(x)
                lista.append(x)

    return max(lista)

def rivisummat():
    lista=[]
    summat=[]
    with open("matriisi.txt") as file:
            for rivi in file:
                rivi = rivi.replace("\n", "")
                numero=rivi.split(",")
                lista.append(numero)
    for x in lista: 
        rivi = 0 
        for numero in x: 
            numero=int(numero)
            rivi += numero 
        summat.append(rivi) 
        
    return summat

if __name__=="__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())