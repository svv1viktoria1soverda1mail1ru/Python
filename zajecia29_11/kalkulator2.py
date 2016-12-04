#!/usr/bin/python
from Tkinter import *
import sys
class Kalkulator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title("Kalkulator")
        self.num1=StringVar()
        self.frame = Frame(self)
        self.frame.pack()

        self.E=Entry(self.frame,textvariable = self.num1, bd=5)
        self.E.pack()

        self.frame1 = Frame(self)
        self.frame1.pack()
        self.button1 = Button(self.frame1, text="1",width=5,height=1,command=self.evaluate1)
        self.button1.pack( side = LEFT)
        self.button2 = Button(self.frame1, text="2",width=5,height=1,command=self.evaluate2)
        self.button2.pack( side = LEFT )
        self.button3 = Button(self.frame1, text="3",width=5,height=1,command=self.evaluate3)
        self.button3.pack( side = LEFT )


        self.frame2 = Frame(self)
        self.frame2.pack()
        self.button4 = Button(self.frame2, text="4",width=5,height=1,command=self.evaluate4)
        self.button4.pack( side = LEFT)
        self.button5 = Button(self.frame2, text="5",width=5,height=1,command=self.evaluate5)
        self.button5.pack( side = LEFT)
        self.button6 = Button(self.frame2, text="6",width=5,height=1,command=self.evaluate6)
        self.button6.pack( side = LEFT)

        self.frame3 = Frame(self)
        self.frame3.pack()
        self.button7 = Button(self.frame3, text="7",width=5,height=1,command=self.evaluate7)
        self.button7.pack( side = LEFT)
        self.button8 = Button(self.frame3, text="8",width=5,height=1,command=self.evaluate8)
        self.button8.pack( side = LEFT)
        self.button9 = Button(self.frame3, text="9",width=5,height=1,command=self.evaluate9)
        self.button9.pack( side = LEFT)

        self.frame4 = Frame(self)
        self.frame4.pack()
        self.button10 = Button(self.frame4, text="0",width=5,height=1,command=self.evaluate0)
        self.button10.pack( side = LEFT)
        self.button11 = Button(self.frame4, text=".",width=5,height=1,command=self.evaluatekropka)
        self.button11.pack( side = LEFT)
        self.button12 = Button(self.frame4, text="=",width=5,height=1,command=self.evaluaterown)
        self.button12.pack( side = LEFT)

        self.frame5 = Frame(self)
        self.frame5.pack()
        self.button13 = Button(self.frame5, text="-",width=4,height=1,command=self.evaluatemin)
        self.button13.pack( side = LEFT)
        self.button14 = Button(self.frame5, text="+",width=4,height=1,command=self.evaluatepl)
        self.button14.pack( side = LEFT)
        self.button15 = Button(self.frame5, text="*",width=4,height=1,command=self.evaluatemn)
        self.button15.pack( side = LEFT)
        self.button16 = Button(self.frame5, text="/",width=4,height=1,command=self.evaluatedz)
        self.button16.pack( side = LEFT)

        self.frame6 = Frame(self)
        self.frame6.pack()
        self.button17 = Button(self.frame6, text="Clr",width=20,height=1,command=self.clear)
        self.button17.pack()
    def clear(self):
        self.E.delete(0,END)
        return
    def evaluate1(self):
        self.E.insert(END,"1")
    def evaluate2(self):
        self.E.insert(END,"2")
    def evaluate3(self):
        self.E.insert(END,"3")
    def evaluate4(self):
        self.E.insert(END,"4")
    def evaluate5(self):
        self.E.insert(END,"5")
    def evaluate6(self):
        self.E.insert(END,"6")
    def evaluate7(self):
        self.E.insert(END,"7")
    def evaluate8(self):
        self.E.insert(END,"8")
    def evaluate9(self):
        self.E.insert(END,"9")
    def evaluate0(self):
        self.E.insert(END,"0")
    def evaluatekropka(self):
        self.E.insert(END,".")
    def evaluaterown(self):
        self.napis=self.E.get()
        self.clear()
        #self.operator=self.napis.find("-" or "+" or "*" or "/")
        for nr,wartosc in enumerate(list(self.napis)):
            if wartosc in ['-','+','*','/']:
                #print nr,wartosc
                self.liczba1=self.napis[0:nr]
                self.liczba2=self.napis[nr+1:]
                self.E.insert(END,str(eval(self.liczba1+wartosc+self.liczba2)))
    def evaluatemin(self):
        self.E.insert(END,"-")
    def evaluatepl(self):
        self.E.insert(END,"+")
    def evaluatemn(self):
        self.E.insert(END,"*")
    def evaluatedz(self):
        self.E.insert(END,"/")
def main():
    Kalkulator().mainloop()
if __name__=="__main__":
    main()

