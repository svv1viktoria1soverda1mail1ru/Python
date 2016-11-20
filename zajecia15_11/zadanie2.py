# coding=utf-8

#Napisać skrypt, który będzie działał jak gra w koło fortuny. Na początku gry podaje się
#liczbę uczestników oraz losowo wybierana jest kategoria i hasło z pliku txt. Następnie każdy
#z uczestników losuje liczbę od 1 do ilości uczestników. W ten sposób ustala się kolejność
#gry przy pierwszym kręceniu kołem. Na kole znajdują się cyfry od -10 do 10. Liczby te
#symbolizują pkt. Użytkownik kręci kołem czyli losuje liczbę. Liczba 0 symbolizuje
#bankruta i kolejny uczestnik losuje. Następnie podaje literkę. Jeśli literka znajduje się w
#haśle i pkt są ujemne to OTRZYMUJE 1 PUNKT. W przypadku pkt dodatnich są dodawane do
#sumy pkt. Uczestnik po wylosowaniu literki ma prawo do odgadnięcia hasła. Jeśli zgadnie
#jego pkt są mnożone przez ilość literek, które nie zostały odkryte (JESLI PKT UJEMNE TO
#MNOZONE PRZEZ WARTOSC BEZWZGLEDNA). Po odgadnięciu hasła pkt
#wszystkich uczestników zapisywane są do pliku punkty.txt. '''
from random import randrange
import linecache, random, math
class Gra():
    liczba_uczestnikow=0
    kolejka = {}
    punkty=[]
    haslo=""
    def ustawDane(self):
        print "Gra w kolo fortuny"
        self.liczba_uczestnikow = int(raw_input("Podaj liczbe uczestnikow "))
        f1 = open("kategoria.txt", "r+b")
        count = len(open('kategoria.txt', 'rU').readlines())
        random_kat = randrange(1, count+1)
        kat=linecache.getline('kategoria.txt', random_kat)
        print "\nTwoja kategoria\n",kat
        f1.closed
        if (random_kat==1):
            f1 = open("informatyka.txt", "r+b")
            count = len(open('informatyka.txt', 'r+b').readlines())
            random_kat = randrange(1,count+1)
            self.haslo=linecache.getline('informatyka.txt',random_kat)
            print "Twoje haslo"#,self.haslo# print self.haslo[0],self.haslo[1]
            for i in range(len(self.haslo)-1):
                print "*",
            f1.close()
        elif (random_kat==2) :
            f1 = open("matematyka.txt", "r+b")
            count = len(open('matematyka.txt', 'r+b').readlines())
            random_kat = randrange(1, count+1)
            self.haslo=linecache.getline('matematyka.txt',random_kat)
            print "Twoje haslo"#,self.haslo
            for i in range(len(self.haslo) - 1):
                print "*",
            f1.close()
    def losujKolejke(self):
        lista_uczestnikow=[]
        print "\n"
        for i in range(self.liczba_uczestnikow):
            lista_uczestnikow.append(i+1)
            self.punkty.append(0)
        for i in lista_uczestnikow:
            random_kolejka = random.choice(lista_uczestnikow)
            while (random_kolejka in self.kolejka.values()):
                random_kolejka = random.choice(lista_uczestnikow)
            self.kolejka[i]=random_kolejka
        print "Kazdy z uczestnikow losuje liczbe od 1 do ilosc_uczestnikow, az wszystcy beda mieli rozne liczby "
        print "np. zapis 1:3 oznacza ze pierwszy uczestnik bedzie trzeci w kolejce \nKolejka - ",self.kolejka
        print "Wylosowana kolejnosc dla uczestnikow:"
        f2 = open("punkty.txt", "wb")
        f2.write("nr uczestnika :")
        for i in range(1,self.liczba_uczestnikow+1):
            uczestnik=self.kolejka.values().index(i)+1
            print uczestnik,
            f2.write("%3i" % (uczestnik), )
        f2.write("\n")
        f2.close()
try:
    dalej=True
    gra=Gra()
    gra.ustawDane()
    gra.losujKolejke()
    litery=[]
    print "\n---------------------Gra---------------------"
    while (dalej):
        print "---------------------------------------------"
        for i in range(1, gra.liczba_uczestnikow + 1):
            uczestnik = gra.kolejka.values().index(i) + 1
            print "uczestnik nr. ", uczestnik
            losuj_punkty = randrange(-10, 11)
            print "\t\t\twylosowano ",losuj_punkty, " punktow "
            if (losuj_punkty==0):
                print "\t\t\tBankrut"
                gra.punkty[i - 1] = 0
            else :
                literka=raw_input("\t\t\tpodaj literke ")
                if (literka in gra.haslo):
                    litery.append(literka)
                    k=0
                    for j in range(len(gra.haslo) - 1):
                        if (gra.haslo[j] in litery):
                            print gra.haslo[j],
                        else:
                            print "*",
                            k=k+1
                    if (losuj_punkty>0):
                        punkty=gra.punkty[i-1]+losuj_punkty
                        gra.punkty[i - 1] = punkty
                    elif (losuj_punkty<0):
                        punkty=gra.punkty[i-1]+1
                        gra.punkty[i - 1] = punkty
                    if (k==0):
                        print "\n-----------------Koniec gry!------------------"
                        print " wyniki mozna zobaczyc w pliku punkty.txt"
                        dalej = False
                        break;
                    print "\n"
                    napis=raw_input("\t\t\t mozesz zgadnac haslo ")
                    if (len(napis)+1==len(gra.haslo)):
                        for l in range(len(napis)):
                            if (napis[l]==gra.haslo[l]):
                                print "",
                        punkty = gra.punkty[i - 1] + math.fabs(losuj_punkty)*k
                        gra.punkty[i - 1] = punkty
                        print " haslo jest zgadniete "
                        print "\n-----------------Koniec gry!------------------"
                        print " wyniki mozna zobaczyc w pliku punkty.txt"
                        dalej=False;
                        break;

    f2 = open("punkty.txt", "a")
    f2.write("zdobyte punkty:")
    for i in range(len(gra.punkty)):
        f2.write("%3i" % (gra.punkty[i]), )
    f2.close()
except IOError, (errno, strerror):
    print "Błąd I/O (%s): %s" % (errno, strerror)
except ValueError:
    print "Nie mogę przekształcić danej w liczbę całkowitą."
except:
    print "Nieobsługiwany błąd:", sys.exc_info()[0]
    raise









