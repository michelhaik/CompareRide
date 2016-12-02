from tkinter import *
class Interface:
    def __init__(self):
         
        self.janela = Tk()
        self.janela["bg"] = "black"
        self.janela.title("CompareRide")
        self.janela.geometry("400x1200+300+300")

def bt_click():
    print("bt_click")
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        
        num1 = int(ed1.get())
        num2 = int(ed2.get())    
        lb1["text"]  = num1 + num2
    else:
        lb1["text"] = "valores informados invalidos"

def entrada(self):
        
    self.ed1 = Entry(self.janela)
    self.ed1.place(x= 100, y = 100)
    self.ed2= Entry(self.janela)
    self.ed2.place(x=100,y=130)

    self.bt = Button(self.janela, width = 20, text = "Comparar", command=bt_click)
    self.bt.place(x= 100, y = 150)

    self.lb1 = Label(self.janela, text = "Label1")
    self.lb1.place(x=100, y = 200)



janela.mainloop()


