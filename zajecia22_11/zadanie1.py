# -*- coding: utf -*-
'''
operacje  na plikach i katalogach
'''
# wyswietlic wszystkie pliki i katalogi dla katalogu (podac sciezke), wysw rozm poszczegolnych plikow i kat w bajtach, kilobajtach i megabajtach
#podac ilosc plikow, ilosc kat, podplikow i podkatalogow 

from os import *
import glob
ilosc_kat=0
ilosc_podkat=0
ilosc_plikow=0
ilosc_podplikow=0
print 'W katalogu PycharmProjects '
for x in glob.glob(r'C:\Users\student\PycharmProjects\*'):
    if (path.isdir(x)):
        ilosc_kat=ilosc_kat+1
        print '\t',path.split(x)[1],'\t', path.getsize(x),'B,',path.getsize(x)/1024,'kB,',path.getsize(x)/(1024*1024),'MB'

    elif (path.isfile(x)):
        ilosc_plikow = ilosc_plikow + 1
        print '\t',path.split(x)[1],'\t', path.getsize(x),'B,',path.getsize(x)/1024,'kB,',path.getsize(x)/(1024*1024),'MB'
print 'Razem katalogow :',ilosc_kat,', plikow: ',ilosc_plikow
print 'Podkatalogi i podpliki:'
for y in glob.glob(r'C:\Users\student\PycharmProjects\*\*'):
    if (path.isdir(y)):
        ilosc_podkat = ilosc_podkat + 1
        print '\t\t', path.split(y)[1],'\t', path.getsize(y),'B,',path.getsize(y)/1024,'kB,',path.getsize(y)/(1024*1024),'MB'
    elif (path.isfile(y)):
        ilosc_podplikow = ilosc_podplikow + 1
        print '\t\t', path.split(y)[1],'\t', path.getsize(y),'B,',path.getsize(y)/1024,'kB,',path.getsize(y)/(1024*1024),'MB'
print 'Razem katalogow: ', ilosc_podkat, ', plikow: ', ilosc_podplikow