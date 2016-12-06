from tkinter import *

from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6

#### criacao do menu de entrada    
janela1 = Tk()
janela1["bg"] = "black"
janela1.title("CompareRide")
janela1.geometry("400x400+300+300")
ed1 = Entry(janela1)
ed1.place(x= 100, y = 100)
ed2= Entry(janela1)
ed2.place(x=100,y=130)
lb0 = Label(janela1, width = 30, text= "BEM VINDO AO CompareRide",fg ="black", bg = "red", font=("Helvetica", 18))
lb0.place(x= 0, y= 0)
lb1 = Label(janela1, width = 10, text = "Tempo(min)",fg="black",bg="gold")
lb1.place(x = 0, y =100)
lb2 = Label(janela1, width = 10, text = "Distancia(km)",fg="black",bg="gold")
lb2.place(x = 0, y =130)
lb3 = Label(janela1, width = 20,text = "Comparar",fg="black",bg="gold")
lb3.place(x = 100, y =180)

## funcao que recolhe os inputs na janel
def bt_click():
    global tempo
    global distancia
    
    if float(ed1.get().isnumeric()) and float(ed2.get().isnumeric()):
        tempo = float(ed1.get())
        distancia = float(ed2.get())
        print(tempo,distancia)

    else:
        lb3["text"] = "Comandos invalidos"

    
    
                            
bt = Button(janela1, width = 20, text = "Comparar",command = bt_click)
bt.place(x= 100, y = 150)

janela1.mainloop()





### criacao dos outputs de valores 
janela=Tk()
janela["bg"] = "black"
janela.title("CompareRide")
janela.geometry("400x400+300+300")


##### definicao dos precos de cada app
## preco do Uber
preco_uber=int(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)
## preco EasyTaxi
preco_easy=int( 2+ 0.26*tempo + distancia*1.40)
## Preco WillGo
preco_WillGo=int(0.32*tempo +1.61*distancia)
## preco Televo   
preco_Televo=int(1.90+ 0.23*tempo + 1.35*distancia)

## preco taxi comum
#bandeira 2- domingo o dia todo e segunda-sabado das 20 as 6
if dia_semana==6 or (hora_oficial>=0 and hora_oficial<6) or (hora_oficial>=20):
    preco_taxi=int(4.5+ 0.55*tempo + 3.58*distancia) #bandeira 2
   
else:
    preco_taxi=int(4.5 + 0.55*tempo + 2.75*distancia) #bandeira 1
## preco taxi 30% desconto
preco_30=int(4.5 + 0.55*tempo + 2.75*distancia)*0.7


lbpreco = Label(janela, width = 30, text= "PREÇOS POR APP",fg ="black", bg = "red", font=("Helvetica", 18))
lbpreco.place(x= 0, y= 0)
### definicao dos labels p UBER
lbuber= Label(janela, width = 25, text = "Uber",fg="black",bg="gold")
lbuber.place(x= 0, y = 100)
lbuber1= Label(janela, width = 25,text = ("R$",preco_uber),fg="black",bg="gold")
lbuber1.place(x = 150, y=100)

#### definicao dos labels p EasyGo
lbeasy = Label(janela, width = 25, text = "EasyGo",fg="black",bg="gold")
lbeasy.place(x = 0, y = 140)
lbeasy1 = Label(janela, width = 25,text =("R$", preco_easy),fg="black",bg="gold")
lbeasy1.place(x=150, y = 140)

### definicao dos labels p WillGO
lbwillgo = Label(janela, width = 25, text = "WillGo",fg="black",bg="gold")
lbwillgo.place(x=0, y = 180)
lbwillgo1 = Label(janela, width = 25,text =("R$" ,preco_WillGo),fg="black",bg="gold")
lbwillgo1.place(x=150, y = 180)

### definicao dos labels p Taxi comum
lbtx = Label(janela, width = 25, text = "Taxi",fg="black",bg="gold")
lbtx.place(x =0 , y=220)
lbtx1 = Label(janela, width = 25,text =("R$", preco_taxi),fg="black",bg="gold")
lbtx1.place(x=150, y = 220)

### definicao de labels para Taxi com 30% desconto
lb30 = Label(janela, width = 25, text = "Taxi 30%",fg="black",bg="gold")
lb30.place(x =0, y=260)
lb301 = Label(janela, width = 25,text =("R$", preco_30),fg="black",bg="gold")
lb301.place(x=150, y = 260)

### definicao de labels para Televo
lbtel = Label(janela, width = 25, text = "Televo",fg="black",bg="gold")
lbtel.place(x =0, y=300)
lbtel = Label(janela, width = 25,text =("R$", preco_Televo),fg="black",bg="gold")
lbtel.place(x=150, y = 300)

janela.mainloop()

