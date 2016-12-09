# -*- coding: utf-8 -*-
#!/usr/bin/python
from Tkinter import *
import sys
class Konwersja(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Konwersja liczb")
        self.master.geometry("300x300")
        self.num1=StringVar()
        self.frame = Frame(self)
        self.frame.pack()
        self.lab1=Label(self.frame,text="Wpisz liczbe :")
        self.lab1.pack(side=LEFT)
        self.E=Entry(self.frame,textvariable = self.num1, bd=5)
        self.E.pack(side=LEFT)
        self.frame11 = Frame(self)
        self.frame11.pack()
        self.lab1=Label(self.frame11,text="     Z systemu  ------   NA system")
        self.lab1.pack()
        self.frame1 = Frame(self)
        self.frame1.pack()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = StringVar()
        for text, row, col,value in [('dwojkowy', 0, 0,1),
                                       ('dziesietny', 1, 0,2),('osemkowy',2,0,3),('szesnastkowy',3,0,4)]:

            Radiobutton(self.frame1, text=text,value=value, variable=self.var1).grid(row=row,column=col)

        for text, row, col, value in [ ('dwojkowy', 0, 1, 11),
                                          ('dziesietny', 1, 1, 22), ('osemkowy', 2, 1, 33),('szesnastkowy',3,1,44)]:

            Radiobutton(self.frame1, text=text, value=value, variable=self.var2).grid(row=row, column=col)
        self.frame2 = Frame(self)
        self.frame2.pack()

        self.button = Button(self.frame2, text="Konwertuj", width=10, height=1, command=self.konwertuj)
        self.button.pack(side=LEFT)

        self.text = Entry(self.frame2, name="tekst 3")
        self.text.insert(INSERT, "           ")
        self.text.config(state=DISABLED)
        self.text.pack(side=LEFT, padx=5)
        self.frame3 = Frame(self)
        self.frame3.pack()
        self.info=Label(self.frame3,textvariable=self.var3,fg="red",width=20,height=10)
        self.info.pack()
    def konwertuj(self):
        self.var3.set("")
        try:
            self.text.config(state=NORMAL)
            self.text.delete(0,END)

            if (self.var1.get()==1):
                self.liczba =int(self.E.get(),2)
            elif (self.var1.get()==2):
                self.liczba = int(self.E.get())
            elif (self.var1.get()==3):
                self.liczba = int(self.E.get(),8)
            elif (self.var1.get()==4):
                self.liczba = int(self.E.get(),16)

            if (self.var2.get()==11):
                wynik = ""
                while self.liczba > 0:
                    wynik = str(self.liczba % 2) + wynik
                    self.liczba = self.liczba / 2
                self.text.insert(INSERT, wynik)
            elif (self.var2.get()==22):
                self.text.insert(INSERT,str(self.liczba))
            elif (self.var2.get()==33):
                self.wynik=str(oct(self.liczba))[1:]
                self.text.insert(INSERT, self.wynik)
            elif (self.var2.get()==44):
                self.wynik=str(hex(self.liczba))[2:]
                self.text.insert(INSERT, self.wynik)
        except IOError, (errno, strerror):
            print "Błąd I/O (%s): %s" % (errno, strerror)
        except ValueError:
            self.var3.set("Nie mogę przekształcić \n danej w liczbę całkowitą.")
        except:
            print "Nieobsługiwany błąd:", sys.exc_info()[0]
            raise
        return
def main():
    Konwersja().mainloop()
if __name__=="__main__":
    main()