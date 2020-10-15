# Tehtävässä Kilpailija-luokkaa muokataan kahdella tavalla. 
# Ensinnäkin, kirjoita luokalle seliterivi "Kilpailija: sisältää pisteet ja värin". 
# Toisekseen, lisää luokkaan alustusfunktio __init__, 
# jossa uusi olio pyytää itselleen värin käyttäjän syötteenä "Anna minulle väri: ".

# Pääohjelmassa tulee luoda kaksi oliota ja antaa näille alustuksessa värit "sininen" ja "punainen",
# tämän jälkeen kutsuen molempien tilanne-jäsenfunktiota. 
# Lopuksi ohjelma vielä tulostaa ensimmäisen olion selostetekstin komennolla print([nimi].__doc__).

class Kilpailija():
	"""Kilpailija: sisältää pisteet ja värin"""
	pass

	__pisteet=0
	__vari=""
	def __init__(self, vari):
		self.__vari=vari
	def tilanne(self):
		print("Olen", self.__vari,"ja minulla on",self.__pisteet,"pistettä!")

vari=input("Anna minulle väri: ")
eka=Kilpailija(vari)
vari=input("Anna minulle väri: ")
toka=Kilpailija(vari)

eka.tilanne()
toka.tilanne()

print(eka.__doc__)