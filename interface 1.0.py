from tkinter import *
janela1 = Tk()
janela1["bg"] = "black"
janela1.title("CompareRide")
janela1.geometry("400x1200+300+300")

def bt_click():
    print("bt_click")
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        
        num1 = int(ed1.get())
        num2 = int(ed2.get())    
        lb3["text"]  = num1 + num2
        
    elif lb3["text"] == "valores informados invalidos":
        pass


    
ed1 = Entry(janela1)
ed1.place(x= 100, y = 100)
lb1 = Label(janela1, width = 10, text = "Tempo",fg="black",bg="gold")
lb1.place(x = 0, y =100)
ed2= Entry(janela1)
ed2.place(x=100,y=130)
lb2 = Label(janela1, width = 10, text = "Distancia",fg="black",bg="gold")
lb2.place(x = 0, y =130)
lb3 = Label(janela1, width = 10,text = "Comparar",fg="black",bg="gold")
lb3.place(x = 100, y =180)
    
bt = Button(janela1, width = 20, text = "Comparar", command=bt_click)
bt.place(x= 100, y = 150)

janela1.mainloop()

  
janela=Tk()
janela["bg"] = "black"
janela.title("CompareRide")
janela.geometry("400x1200+300+300")
janela.mainloop()

if bt_click == True:
    janela1.destroy()
    janela.mainloop

