#zbiory zmienne
A=set([1,2,3])
print A
#dod i usuwanie elemmentow zbioru
A.discard(3)#usuwanie elementu 3
print A

A.add(8)#dodanie el 8
print A

#zbiory niezmienne
B=frozenset([3,5,6])
print B

#klucze w slownikach
slownik={B,9}
print slownik

#elementy innych zbiorow
C=set([5,4,9])
C.add(B)
print C

#zbior pusty
D=set()
print D
#operacje na zbiorach
#liczba elementow
print len(A),len(B),len(C),len(D)
#sprawdzenie czy dany obiekt jest elementem zbioru
print 5 in A, 5 in B, 5 in C, 5 in D

#sprawdzenie czy dany obiekt nie  jest elementem zbioru
print 8 not in A, 8 not in B, 8 not in C, 8 not in D
print '\n'
#spr czy dany zbior jest podzbiorem
print set([1,2]) <=A
print set([3,4]) <=B
print set([5]) <=B
print set([1,3,5]) <=A
print A.issubset(B)
print '\n'
#spr czy dany zbior jest nadzbiorem innego zbioru
print A>=set([1,2])
print B>=set([3,4])

print A.issuperset(B)
print '\n'
#laczenie zbiorow
E=A |B
print E
print '\n'
#czesc wspolna dwoch zbiorow
F=A & B
print F
print '\n'

#roznica zbiorow
print A-B
print B-A
print '\n'
#roznica symetryczna
G=A^B
print G


'''Klasy'''

class Napis:
    "Klasa wyswietla napis"
    txt = 'Pierwsza klasa'
    def wyswietl(self):
        return "Witaj!"

#konkretyzacja klasy (wywolanie obiektu klasy)
napis = Napis()
#odwolanie do metody
print napis.wyswietl()
#odwolanie do atrybutu klasy
print napis.txt
#konkrety klasy
class Zespolona:
    def __init__(self,rzeczywista,urojona):
        self.r = rzeczywista
        self.i = urojona

x = Zespolona(5.0,-3.2)
print x.r,x.i

'''
metody operujace na napisach
'''

napis = 'Witaj w swiecie PYTHONA!'

print napis.capitalize()
print napis.center(64)
print napis.center(64,'*')
print napis.count('e')
print napis.find('Taj')
print napis.find('taj')
print napis.isdigit()
print '12'.isdigit()
print '12.4'.isdigit()
print ' '.join(['Python','jest','super'])
print napis.join(['***']*5)
print napis.lower()
print napis.replace('PYTHONA','programowania')
print napis.rfind('PYTHONA')
print 'Python jest super'.rfind('e')
print napis.rjust(32)
print napis.rjust(64)
print napis.rjust(64,'.')
print napis.split()
print '123-234-567'.split('-')
print ((napis+'\n')*10).splitlines()
print napis.swapcase()
print napis.title()
print napis.upper()

'''Metody operujace nalistach'''


l = range(1,21)
print l
l.append(22)
print l
l.extend([20,24])
print l
print l.count(20)
print l.index(20)
l.insert(12,44)
print l
l.pop(12)
print l
l.remove(20)
print l
l.reverse()
print l
l.sort()
print l

'''moduly - generator liczb pseudolosowych'''


import random
#from random import *   #nazwy funkcji dostepne bez uzycia nazwy modulu
#from random import randint  #funkcja dostepna bez uzycia nazwy modulu

random.seed()
print random.randint(1,15)#losuje liczbe calkowita od 1 do 15
print random.randint(1,15)

l = range(1,10)
print random.choice(l)#wybiera losowy element z sekwencji
random.shuffle(l)#wykonuje losowa permutacje sekwencji
print l

print random.random()# losowa liczba rzeczywista z zakresu od o.o do 1.0
print random.uniform(10,30)# losowa lczba rzeczywista  z przedzialu [10,30)
print random.normalvariate(5,48)#zmienna losowa o rozkladzie normalnym z srednia 5 i odchyleniem 48

'''rekordy'''


class Adres:
    pass
adr1 = Adres()#utworzenie rekordu
adr1.ulica = 'Stonogi'
adr1.nr=23
adr1.kod = '12-123'
adr1.miasto = 'Dno'
print adr1.ulica
print adr1.__dict__


