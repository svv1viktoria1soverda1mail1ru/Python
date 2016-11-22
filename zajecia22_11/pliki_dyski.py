# -*- coding: utf -*-
'''
operacje  na plikach i katalogach
'''
from os import *
# sprawdzenie w jakim aktualnie katalogu jestesmy
print getcwd()

#zmiana biezocego katalogu na inny
#chdir('Test')
print getcwd()

#zawartosc katalogu
print listdir('..')

#zaw kat - sciezka absolutna
print listdir(r'/home/wiki/PyCharmProjekts/Skrypty')

#filtrowanie plikow i kat wg okreslonego wzorca
import fnmatch
print fnmatch.fnmatch('Python','P*n')
print fnmatch.fnmatch('Python','P*e')

#lista plikow z rozszerzeniem py
print [x for x in listdir(r'/home/wiki/PyCharmProjekts/Skrypty')
       if fnmatch.fnmatch(x,'*.py')]

#lista plikow koncz sie liczba 6 lub 1
print [x for x in listdir(r'/home/wiki/PyCharmProjekts/Skrypty')
       if fnmatch.fnmatch(x,'*[61].*')]

import glob
for x in glob.glob(r'/home/wiki/PyCharmProjekts/Skrypty/*[61].*'):
    print x

#rozdzielenie sciezki absolutnej na kat w ktorym znajduje sie plik oraz nazwe pliku
print path.split('/home/wiki/PyCharmProjekts/Skrypty/script25.py')

for x in glob.glob(r'../*[61].*'):
    print path.split(x)[1]

#laczenie ciagu katalogow w sciezke
print path.join('/','home','wiki','PyCharmProjekts','Skrypty','script25.py')
print path.join(r'home/wiki','PyCharmProjekts','Skrypty/script25.py')

#spr czy podana sciezka jest absolutna
print  path.isabs(r'../script25.py')
print  path.isabs(r'/home/wiki/PyCharmProjekts/Skrypty/script25.py')

#spr czy dany obiekt dyskowy istnieje
print path.exists('/home/wiki/PyCharmProjekts/Skrypty/script25.py')
print path.exists('/home/wiki/PyCharmProjekts/Skrypt1')

#zmiana nazwy kat lub pliku
#rename('../Test','../nTest')
print path.exists('nTest')
print listdir('.')

#spr czy dany obiekt dyskowy jest plikiem
print path.isfile('nTest')
print path.isfile('script25.py')

#spr czy dany obiekt dyskowy jest kat
print path.isdir('nTest')
print path.isdir('script25.py')

#spr czy dany obiekt dyskowy jest dskiem
print path.ismount('nTest')
print path.ismount('/home')

#spr dlugosci pliku (bajty)
print path.getsize('nTest')
print path.getsize('script25.py')

for x in listdir('.'):
    print x,path.getsize(x)

#czas stworzenia oliku
from time import ctime
print ctime(path.getctime('script25.py'))

#czas ost modyfikacji
print ctime(path.getmtime('script25.py'))

#rekursywne przechodzenie katalogow
for sciezka, podkatalogi, pliki in walk(r'./'):
    print 'W kat %s znajduje sie %i bajtow w %i plikach' \
        % (sciezka, sum(path.getsize(path.join(sciezka,nazwa))
                        for nazwa in pliki), len(pliki))

