
from Tkinter import *
class LabelDemo(Frame):
    def __init__(self):
        """Tworzy 3 etykiety i 2 przyciski oraz pakje je"""
        # tworzy obiekt ramka w ktorym umieszczam widgety
        #ramka  jest upakowana w oknie glownym i ma tytul Przyklad
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Przyklad")
        self.master.minsize(200,200)
        self.labelText = ""
        #tworzymy 2 przyciski o nazwach QUIT i HEJ
        self.button=Button(self,text="QUIT",fg="red",command=self.quit1,width=16,height=1)
        self.hi_there=Button(self,text="Wyswietl wynik dla ciagu fibbonaciego",command=self.say_hi,width=50,height=1)
        self.Label1 = Label(self,text=self.labelText)


        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack()


    #metoda wywolywana przez wcisniecie pzycisku QUIT
    def quit1(self):
        print "Koniec"
        quit()
    #metoda wywolywana przez wcisniecie przycisku Hej
    def say_hi(self):
        self.Label1.config(text=self.fib(10))
    def fib(self,nr):
        k = [0, 1]
        for l in range(2, nr):
            il = k[l - 2] + k[l - 1]
            k.append(il)
        return k

#print fib(10)
#(A)Program glowny-utworzenie okna LabelDemo i obsluga wszystkich zdarzen
def main():
    LabelDemo().mainloop()
#jesli azwa uruchamianego programu to __main__ wywolaj procedure main()
if __name__=="__main__":
    main()