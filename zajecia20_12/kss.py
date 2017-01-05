#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Osoba():
    kolejny_id = 1
    def __init__(self):
        self.id = self.kolejny_id
        self.__class__.kolejny_id= self.kolejny_id + 1
    def dodaj(self):
        print   'Osoba nr.',self.id
        osoba.imie=raw_input("Podaj imie ")
        osoba.nazwisko=raw_input("Podaj nazwisko ")
        osoba.pesel =long(raw_input("Podaj pesel "))
        osoba.adres =  raw_input("Podaj adres ")
        osoba.telefon = long(raw_input("Podaj telefon "))
        print 'Dodano osobe ','\t',osoba.imie,'\t',osoba.nazwisko,'\t',osoba.pesel,'\t',osoba.adres,'\t',osoba.telefon
        lista_osob.append([osoba.id,osoba.imie,osoba.nazwisko,osoba.pesel,osoba.adres,osoba.telefon])
    def wyswietl(self):
        for i in range(0,len(lista_osob)):
            #print '\t\t'.join(map(str, lista_osob[i]))
            print "%2s" % lista_osob[i][0],'\t',"%15s" % lista_osob[i][1],'\t', "%15s" % lista_osob[i][2],'\t',"%12s" % lista_osob[i][3],'\t',"%20s" % lista_osob[i][4],'\t',"%12s" % lista_osob[i][5]
    def usun(self):
        id_do_usuniecia=int(raw_input("Wybierz i wpisz z powyzszej listy numer osoby do usuniecia "))
        del lista_osob[id_do_usuniecia]
        for i in range(id_do_usuniecia, len(lista_osob)):
            lista_osob[i][0]-=1
        self.id = self.kolejny_id
        self.__class__.kolejny_id = self.kolejny_id - 1
    def modyfikuj(self):
        id_do_modyfikacji = int(raw_input("Wybierz i wpisz z powyzszej listy numer osoby do modyfikacji danych "))
        print   ''
        print "Osoba nr.","%s" % lista_osob[id_do_modyfikacji][0], '\n1.IMIE:    ', "%s" % lista_osob[id_do_modyfikacji][1], '\n2.NAZWISKO:', "%s" % lista_osob[id_do_modyfikacji][2], '\n3.PESEL:   ', "%s" % \
            lista_osob[id_do_modyfikacji][3], '\n4.ADRES:   ', "%s" % lista_osob[id_do_modyfikacji][4], '\n5.TELEFON: ', "%s" % lista_osob[id_do_modyfikacji][5]

        a=raw_input(" Wpisz numer lub numery atrybutow, ktore chcesz zmienic (1-IMIE,2-NAZWISKO,3-PESEL,4-ADRES,5-TELEFON,6-WSZYSTKO) ")
        osoba.imie=lista_osob[id_do_modyfikacji][1]
        osoba.nazwisko=lista_osob[id_do_modyfikacji][2]
        osoba.pesel=lista_osob[id_do_modyfikacji][3]
        osoba.adres=lista_osob[id_do_modyfikacji][4]
        osoba.telefon=lista_osob[id_do_modyfikacji][5]
        for i in range(len(a)):
            if a[i] == '1':
                osoba.imie = raw_input("Podaj imie ")
            elif a[i] == '2':
                osoba.nazwisko = raw_input("Podaj nazwisko ")
            elif a[i] == '3':
                osoba.pesel =long(raw_input("Podaj pesel "))
            elif a[i] == '4':
                osoba.adres =  raw_input("Podaj adres ")
            elif a[i] == '5':
                osoba.telefon = long(raw_input("Podaj telefon "))
            elif a[i] == '6':
                osoba.imie = raw_input("Podaj imie ")
                osoba.nazwisko = raw_input("Podaj nazwisko ")
                osoba.pesel = long(raw_input("Podaj pesel "))
                osoba.adres = raw_input("Podaj adres ")
                osoba.telefon = long(raw_input("Podaj telefon "))


        print 'Dane:  ', '\t', '\t\t'.join(map(str, lista_osob[id_do_modyfikacji])), '\n','zmieniono na:', osoba.imie,'\t',osoba.nazwisko,'\t',osoba.pesel,'\t',osoba.adres,'\t',osoba.telefon
        del lista_osob[id_do_modyfikacji]
        lista_osob.insert(id_do_modyfikacji,[id_do_modyfikacji, osoba.imie, osoba.nazwisko,osoba.pesel,osoba.adres,osoba.telefon])
    def zapis(self):
        import shelve
        db = shelve.open('baza')
        db['0'] =  ['ID', 'IMIE', 'NAZWISKO','PESEL','ADRES','TELEFON']
        db['1'] =  [1,'Wiktoria','Sowerda',101010101, 'ul.Jasna 1',123456789]
        for i in db.keys():
            print db[i]
lista_osob = []
lista_naglowek = ['ID', 'IMIE', 'NAZWISKO','PESEL','ADRES','TELEFON']
lista_osob = [lista_naglowek]
osoba=Osoba()
lista_osob.append([1,'Wiktoria','Sowerda',101010101, 'ul.Jasna 1',123456789])
print "To jest twoja ksiazka adresowa.\nMasz wpisane moje dane w ksiazce pod numerem 1. "
while True:
    print "\n\nMenu: "
    print "1 - Dodaj nowa osobe"
    print "2 - Wyswietl zawartosc ksiazki adresowej"
    print "3 - Usun dane osoby"
    print "4 - Modyfikuj dane osoby"
    print "5 - Wyjscie\n"
    a = raw_input("wybierz numer: ")
    if a == '1':
        try:
            b = int(raw_input("Ile osob chcesz dodac? "))
            for i in range(0, b):
                osoba = Osoba()
                osoba.dodaj()
        except Exception:
            print "Wystapil blad, zle wprowadziles dane (pesel i telefon sa wartosciami liczbowymi)"
            break
    elif a =='2':
        try:
            osoba.wyswietl()
            osoba.zapis()
        except Exception:
            print "Wystapil blad, sprobuj ponownie"
            break
    elif a =='3':
        try:
            osoba.wyswietl()
            osoba.usun()
        except Exception:
            print "Wystapil blad, sprobuj ponownie"
            break
    elif a=='4':
        try:
            osoba.wyswietl()
            osoba.modyfikuj()
        except Exception:
            print "Wystapil blad, zle wprowadziles dane (pesel i telefon sa wartosciami liczbowymi)"
            break
    elif a =='5':
        break
    else:
        print("zly wybor, odpal jeszcze raz")