from math import sqrt
#Wiktoria Sowerda
def tablica(pocz, koniec):#utworz tablice poczatkowa
    tablica = []
    while pocz != koniec + 1:
        tablica.append(pocz)
        pocz += 1
    return tablica

def sitoEratostenesa(gornyZakres):
    sq = int(sqrt(gornyZakres))
    wart_pocz = 2
    tab = tablica(2, gornyZakres)
    while True:
        if wart_pocz > sq:
            return tab

        for i in tab:
            if (not (i % wart_pocz) and not (wart_pocz == i)) and wart_pocz != 1:
                tab.remove(i)
        i = tab.index(wart_pocz) + 1
        wart_pocz = tab[i]
# pobierz gorny zakres
n = int(raw_input("Wpisz gorny zakres: "))
liczby = sitoEratostenesa(n)
for i in liczby:
         print i