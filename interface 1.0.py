from tkinter import *

#### criacao do menu de entrada       
janela1 = Tk()
janela1["bg"] = "black"
janela1.title("CompareRide")
janela1.geometry("400x400+300+300")

def bt_click():
    print("bt_click")
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        
        tempo = int(ed1.get())
        distancia = int(ed2.get())    
        lb3["text"]  = tempo + distancia
    else:
        lb3["text"] = "valores informados invalidos"



lb0 = Label(janela1, width = 30, text= "BEM VINDO AO CompareRide",fg ="black", bg = "red")
lb0.place(x= 0, y= 0)
ed1 = Entry(janela1)
ed1.place(x= 100, y = 100)
lb1 = Label(janela1, width = 10, text = "Tempo",fg="black",bg="gold")
lb1.place(x = 0, y =100)
ed2= Entry(janela1)
ed2.place(x=100,y=130)
lb2 = Label(janela1, width = 10, text = "Distancia",fg="black",bg="gold")
lb2.place(x = 0, y =130)
lb3 = Label(janela1, width = 20,text = "Comparar",fg="black",bg="gold")
lb3.place(x = 100, y =180)
bt = Button(janela1, width = 20, text = "Comparar", command=bt_click)
bt.place(x= 100, y = 150)

janela1.mainloop()
#janela1.destroy()
 
#### criacao dos outputs de valores
 
janela=Tk()
janela["bg"] = "black"
janela.title("CompareRide")
janela.geometry("400x400+300+300")


### definicao dos labels p UBER
lbuber= Label(janela, width = 25, text = "Uber",fg="black",bg="gold")
lbuber.place(x= 0, y = 100)
lbuber1= Label(janela, width = 25,fg="black",bg="gold")
lbuber1.place(x = 150, y=100)
### definicao dos labels p Cabify
lbcab = Label(janela, width = 25, text = "Cabify",fg="black",bg="gold")
lbcab.place(x = 0 , y = 140)
lbcab1 = Label(janela, width = 25,fg="black",bg="gold")
lbcab1.place(x = 150, y=140)
### definicao dos labels p EasyGo
lbeasy = Label(janela, width = 25, text = "EasyGo",fg="black",bg="gold")
lbeasy.place(x = 0, y = 180)
lbeasy1 = Label(janela, width = 25,fg="black",bg="gold")
lbeasy1.place(x=150, y = 180)
### definicao dos labels p WillGO
lbwillgo = Label(janela, width = 25, text = "WillGo",fg="black",bg="gold")
lbwillgo.place(x=0, y = 220)
lbwillgo1 = Label(janela, width = 25,fg="black",bg="gold")
lbwillgo1.place(x=150, y = 220)
### definicao dos labels p Taxi comum
lbtx = Label(janela, width = 25, text = "Taxi comum",fg="black",bg="gold")
lbtx.place(x =0 , y=260)
lbtx1 = Label(janela, width = 25,fg="black",bg="gold")
lbtx1.place(x=150, y = 260)
### definicao de labels para Taxi com 30% desconto
lb30 = Label(janela, width = 25, text = "Taxi 30% desconto",fg="black",bg="gold")
lb30.place(x =-200, y=300)
lb301 = Label(janela, width = 25,fg="black",bg="gold")
lb301.place(x=150, y = 300)

janela.mainloop()