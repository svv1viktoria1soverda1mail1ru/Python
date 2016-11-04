import random
random.seed()
print "Gra: Program wylosowal liczbe od 1 do 20, zgadnij ja"
czyniezgadl = True
liczba  = random.randint(1,20)
while czyniezgadl:
    sam = input()
    sam = int(sam)
    if sam<liczba:
        print('Liczba jest wieksza')
    if sam>liczba:
        print('Moja liczba jest mniejsza')
    if sam == liczba:
        print('Brawo, zgadles moja liczbe!')
        break