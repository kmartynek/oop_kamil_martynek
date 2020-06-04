class Empty: #klasa bazowa
	pass

class Tamagotchi(Empty):  #klasa pochodna
prog_nudy = 5 #pole
prog_glodu = 10 #pole

def __init__(self, imie): #konstruktor
self.imie = imie #atrybut
self.slowa = ["Mmmmrrp", "Hrrp"] #atrybut
self.poziom_nudy = 0 #atrybut

burek = Tamagotchi("Burek") #instancja