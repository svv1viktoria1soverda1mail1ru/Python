# -*- coding: utf-8 -*-
#wytworniki
l=range(1,21,2)
print l

#postac prosta

#podwojenie wartosci
print [2*x for x in l]
#para (x, kwadrat x)
print [(x,x*x) for x in range(1,5)]
#tabela kodowa ASCII
print [(x, ord(x)) for x in "ABCDF"]
#lista zawierajaca 10 pustych list
print [ [] for x in range(10)]


#postac prosta warunkowa

#pary kazdy element z kazdym
print [(x,y) for x in range(1,5)
       for y in range(4,0,-1)]
#roznica miedzy wartoscia z pierwszej i drugiej listy
print [x-y for x in range(1,5)
       for y in range(4,0,-1)]
#sklejenie napisu z wartosci pochodzocych z trzech list
print [`x`+y+`z` for x in [1,2]
       for y in ['A','B']
       for z in [0,3] ]


#postac rozszerzona z jednym warunkiem

#para kazdy element z kazdym tylko jezeli pierwszy element jest mniejszy od drugiego
print [(x,y) for x in range(1,5)
       for y in range(6,3,-1)
       if x<y]
#para kazdy element z kazdym tylko jezeli suma elementow jest mniejsza od 7
print [(x,y) for x in range(1,5)
       for y in range(6,3,-1)
       if x+y<7]
#para kazdy element z kazdym pod warunkiem ze pierwszy element jest parzysty lub drugi jest nieparzysty
print [(x,y) for x in range(1,5)
       for y in range(6,3,-1)
       if not (x%2) or y%2]


#postac rozszerzona z wieloma warunkami

#para kazdy element z kazdym pod warunkiem ze pierwszy element jest parzysty a drugi jest nieparzysty
print [(x,y) for x in range(1,5) if not (x%2)
       for y in range(6,2,-1) if y%2]


#funkcje ulatwiajace przetwarzanie sekwencji
#f-cja map - wywoluje okreslona funkcje dla kazdego elementu sekwencji z osobna
dziel = lambda x,y,z: (x+y)/z
print dziel(1,2,3)
xyz={1,2,3}
#print apply(dziel,xyz)
print map(lambda x: x*x*x, range(10))
print map(dziel,range(10),range(10),[2]*10)
#f-cja zip - sluzy do konsolidacji danych
#wartosc pojedynczego elementu listy wwarunkowej zalezy od wartosci pojedynczych elementow list zrodlowych
print zip("abcdef", [1,2,3,4,5,6])
print zip(range(1,10),range(9,0,-1))
print zip("zip",range(0,9),zip(range(0,9)))

#funkcja filter - sluzy do filtrowania danych
#filtrowanie samoglosek
samogloska = lambda x:x.lower() in 'aeiou'
print samogloska('A')
print filter(samogloska,"ala ma kota")
#filtrowanie innych znakow
print filter(lambda  x:not samogloska(x),"Ala ma kota")

#f-kcja reduce - agregowanie danych (operacja obliczania pojedynczego wyrazenia zaleznego od wszystkich elementoe listy zrodlowej)
#suma elementow
print reduce(lambda x,y: x+y,[1,2,3])
#sume kwadratow elementow
print reduce(lambda x,y:x+y,map(lambda  x:x*x,range(1,3)))