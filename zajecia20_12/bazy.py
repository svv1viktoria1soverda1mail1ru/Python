# -*- coding: utf-8 -*-
'''bazy danych'''
#konwersja na string
lista=[1,'2',3,'cztery',5]
t=str(lista)
print t
#proces odwrotny
l = list(t)
print l
#serializacja obiektu (pilkowanie)
# - przeksztalcenie danych go opisyjacych w ciag bajtow
#(funkcja dumps) z ktorego mozna pozniek odtworzyc taki sam obiekt
#(funkcja loads)
import pickle
zapis = pickle.dumps(lista)
print zapis
l = pickle.loads(zapis)
print l
#przyklad ze slownikiem
slownik={"a":"b",1:2}
zapis=pickle.dumps((lista,slownik))
del lista
del slownik
(lista,slownik)=pickle.loads(zapis)
print lista
print slownik
#przyklad z wlasna funkcja
class wymiary3:
    x=0
    y=0
    z=0
w3=wymiary3()
w3.x=1
w3.y=2
w3.z=3
zapis=pickle.dumps(w3)
del w3
w3=pickle.loads(zapis)
print w3.x
#zapis do pliku
f1=file("trzy_rzeczy.txt","w+")
pickle.dump((lista,slownik,w3),f1)
lista=[]
slownik={}
w3=wymiary3()
print lista
print slownik
print w3.x
f1.seek(0)
(lista,slownik,w3)=pickle.load(f1)
print lista
print slownik
print w3.x

#uzycie slownika - napisy jako klucze
import dumbdbm
db=dumbdbm.open("prosta_baza")
db['napis']="hej ho!"
print db['napis']
db.close()
#dowolne dane - metody jak do slownika
import shelve
db=shelve.open('baza')
db['lista']=lista
print db['lista']
db['lista']=slownik
print db['lista']
db.close()