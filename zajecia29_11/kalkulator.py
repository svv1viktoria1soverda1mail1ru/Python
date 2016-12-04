from Tkinter import *
class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Kalkulator")
        self.master.minsize(600,400)
        self.labelText = "wynik"
        #self.button=Button(self,text="QUIT",fg="red",command=self.quit1,width=16,height=1)
        #self.hi_there=Button(self,text="Wyswietl wynik dla ciagu fibbonaciego",command=self.say_hi,width=50,height=1)
        #self.Label1 = Label(self,text=self.labelText)
        self.leftframe=Frame(self,width=200,height=400)
        self.leftframe.pack(side=LEFT)
        self.frame = Frame(self, width=200, height=400)
        self.frame.pack(side=LEFT)
        self.button1 = Button(self.frame, text="+",command=self.oblicz_s, width=10, height=1)
        self.button1.pack()
        self.button2 = Button(self.frame, text="-",command=self.oblicz_r, width=10, height=1)
        self.button2.pack()
        self.button3 = Button(self.frame, text="*",command=self.oblicz_mn, width=10, height=1)
        self.button3.pack()
        self.button4 = Button(self.frame, text="/",command=self.oblicz_dz, width=10, height=1)
        self.button4.pack()
        self.E1 = Entry(self.leftframe, bd=5)
        self.E1.pack(side=LEFT)
        self.rframe = Frame(self, width=200, height=600)
        self.rframe.pack(side=LEFT)
        self.E2 = Entry(self.rframe, bd=5)
        self.E2.pack(side=LEFT)
        self.wframe = Frame(self, width=200, height=400)
        self.wframe.pack(side=LEFT)
        self.Label1 = Label(self.wframe, text=self.labelText)
        self.Label1.pack(side=LEFT)

    def oblicz_s(self):
        self.Label1.config(text=float(self.E1.get())+ float(self.E2.get()))

    def oblicz_r(self):
        self.Label1.config(text=float(self.E1.get()) - float(self.E2.get()))


    def oblicz_mn(self):
        self.Label1.config(text=float(self.E1.get()) * float(self.E2.get()))

    def oblicz_dz(self):
        self.Label1.config(text=float(self.E1.get()) / float(self.E2.get()))

    def say_hi(self):
        pass



def main():
    LabelDemo().mainloop()
if __name__=="__main__":
    main()