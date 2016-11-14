# -*- coding: utf-8 -*-
#!/usr/bin/python
'''Napisać skrypt który wykona następujące czynności:
a) utworzy listę o rozmiarach podanych przez użytkownika
b) uzupełni listę losowymi wartościami z zakresu podanego przez użytkownika
c) wyświetli listę
d) wyszuka wielokrotności liczby 2 , 3, 5 i zapisze każdą do nowej listy
e) wyszuka duplikaty z każdej listy i utworzy z nich nową listę
f) zastąpi duplikaty znakiem ‘X’
g) usunie duplikaty z listy a)
h) obliczy wartość średnią i podniesie każdą wartość do potęgi 3
i) zastąpi wielokrotności liczby 2 litera A, 3 litera E, 5 litera L
j) wyszuka liczby pierwsze i zastąpi je literą Z
k) wyszuka litery w liście i utworzy z nich losowe napisy
'''
import random
from random import randrange
import string, sys
class Wytworniki():
    def __init__(self):
        self.lista=[]
    def uzupelnijListe(self,l,a,b):
        i = 0
        while (i < l):
            self.lista.append(random.randint(a, b))
            i = i + 1
    def wyswietlListe(self):
        print "* Wyswietlic liste"
        print "Lista ",self.lista,"\n\n"
    def wyszWielLiczb_2_3_5(self,a,b):
        print "* Wyszukac wielokrotnosci liczby 2, 3, 5 i zapisac kazda do nowej listy"
        global listawielokr2,listawielokr3,listawielokr5
        lista2 = [x for x in range(a, b+1) if not (x % 2)]
        lista3 = [x for x in range(a, b+1) if not (x % 3)]
        lista5 = [x for x in range(a, b+1) if not (x % 5)]
        listawielokr2 = []
        listawielokr3 = []
        listawielokr5 = []
        for i in self.lista:
            for j in lista2:
                if i == j:
                    listawielokr2.append(i)
        for i in self.lista:
            for j in lista3:
                if i == j:
                    listawielokr3.append(i)
        for i in self.lista:
            for j in lista5:
                if i == j:
                    listawielokr5.append(i)
        print "wielokrotnosci 2 z przedzialu ",listawielokr2
        print "wielokrotnosci 3 z przedzialu ",listawielokr3
        print "wielokrotnosci 5 z przedzialu ",listawielokr5,"\n\n"
        print "* Wyszukac duplikaty z kazdej listy"
        print "lista wielokrotnosci 2 bez dublikatow ",list(set(listawielokr2))
        print "lista wielokrotnosci 3 bez dublikatow ",list(set(listawielokr3))
        print "lista wielokrotnosci 5 bez dublikatow ",list(set(listawielokr5)),"\n\n"

    def zastDublikatyX(self):
        print "* Zastapic duplikaty znakiem ‘X’"
        lista2x=[]
        for i in range(len(listawielokr2)):
            el=listawielokr2[i]
            if (lista2x.count(el)==0):
                lista2x.append(el)
            else:
                lista2x.append("X")
        print "wielokrotnosci 2 z przedzialu ",lista2x
        lista3x = []
        for i in range(len(listawielokr3)):
            el = listawielokr3[i]
            if (lista3x.count(el) == 0):
                lista3x.append(el)
            else:
                lista3x.append("X")
        print "wielokrotnosci 3 z przedzialu ",lista3x
        lista5x = []
        for i in range(len(listawielokr5)):
            el = listawielokr5[i]
            if (lista5x.count(el) == 0):
                lista5x.append(el)
            else:
                lista5x.append("X")
        print "wielokrotnosci 5 z przedzialu ",lista5x,"\n\n"
    def usunDublikaty(self):
        global listabezdublikatow
        listabezdublikatow=[]
        for i in range(len(self.lista)):
            el =self.lista[i]
            if (listabezdublikatow.count(el) == 0):
                listabezdublikatow.append(el)
        print "* Usunac duplikaty z listy"
        print "Lista bez dublikatow ", listabezdublikatow,"\n\n"
    def wartSrednia(self):
        print "* Obliczyc wartosc srednia i podniesc kazda wartosc do potegi 3"
        wynik=0
        for i in range(len(listabezdublikatow)):
            wynik = wynik + listabezdublikatow[i]
        if (len(listabezdublikatow)):
            wynik=float(wynik)/len(listabezdublikatow)
            print "Wartosc srednia wynosi ",wynik
        print "Lista z elementami podniesionymi do potegi 3 ",[x*x*x for x in listabezdublikatow],"\n\n"
    def zastapienie(self):                                                              #i
        wynik=[]
        print "* Zastapic wielokrotności liczby 2 litera A, 3 litera E, 5 litera L"
        print "lista przed zastapieniem ",self.lista
        for i in range(len(self.lista)):
            if (self.lista[i]%2==0):
                wynik.append('A')
            elif (self.lista[i]%3==0):
                wynik.append('E')
            elif (self.lista[i]%5==0):
                wynik.append('L')
            else :
                wynik.append(self.lista[i])
        self.lista= wynik
        print "Wynik ",wynik,"\n\n"
    def sito(self,n):
        L = [0] + n * [1]
        p = 2
        q = p * p
        while q <= n:
            if L[p] == 1:
                i = q
                while i <= n:
                    L[i] = 0
                    i = i + p
            p = p + 1
            q = p * p
        M = []
        for i in range(1, n + 1):
            if L[i] == 1:
                M.append(i)
        return M
    def liczbyPierwsze(self):
        wynik = []
        print "* Zastapic liczby pierwsze litera Z"
        print "lista przed zastapieniem ",self.lista
        print "lista liczb pierwszych ",self.sito(b)
        for i in range(len(self.lista)):
            if (self.lista[i] in self.sito(b)):
                wynik.append('Z')
            else:
                wynik.append(self.lista[i])
        self.lista = wynik
        print "Wynik ",wynik,"\n\n"
    def losoweNapisy(self):
        wynik=[]
        print "* Wyszukac litery w liscie i utworzyc z nich losowe napisy"
        list_of_random_items=[]
        for i in range(len(self.lista)):
            if ((self.lista[i]>='A') and (self.lista[i]<='Z')):
                wynik.append(self.lista[i])

        random_len = randrange(0, len(wynik))
        for wyraz in range(random_len):
            list_of_random_items.append(''.join(random.choice(wynik) for _ in range(randrange(0, 10))))
        #list_of_random_items = random.sample(wynik,random_len)
        print " Lista z samych liter",wynik
        print " Losowa lista losowych napisow dlugosci od 1 do 10 z elementow z powyzszej listy"
        print list_of_random_items,"\n\n"
try:
    w=Wytworniki()
    l = input("Podaj dlugosc listy ")
    print 'Podaj zakres, czyli dwie liczby (liczba 1 musi byc mniejsza od liczby 2)'
    a = input("Twoja liczba 1: ")
    b = input("Twoja liczba 2: ")
    w.uzupelnijListe(l,a,b)
    w.wyswietlListe()
    w.wyszWielLiczb_2_3_5(a,b)
    w.zastDublikatyX()
    w.usunDublikaty()
    w.wartSrednia()
    w.zastapienie()
    w.liczbyPierwsze()
    w.losoweNapisy()
except IOError, (errno, strerror):
    print "Błąd I/O (%s): %s" % (errno, strerror)
except ValueError:
    print "Nie mogę przekształcić danej w liczbę całkowitą."
except:
    print "Nieobsługiwany błąd:", sys.exc_info()[0]
    raise
