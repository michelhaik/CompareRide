from tkinter import *

janela = Tk()
def bt_click():
    print("bt_click")
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        
        num1 = int(ed1.get())
        num2 = int(ed2.get())    
        lb1["text"]  = num1 + num2
    else:
        lb1["text"] = "valores informados invalidos"


ed1 = Entry(janela)
ed1.place(x= 100, y = 100)
ed2= Entry(janela)
ed2.place(x=100,y=130)

bt = Button(janela, width = 20, text = "Comparar", command=bt_click)
bt.place(x= 100, y = 150)

lb1 = Label(janela, text = "Label1")
lb1.place(x=100, y = 200)


janela.geometry("400x1200+300+300")
janela.mainloop()


