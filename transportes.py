# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:29:53 2016

@author: Michel
"""
from datetime import datetime

def Hora

def calculadora(distancia, tempo, app):
    if app == "Uber":
        preco_=(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)*dinamica
        
    elif app == "Cabify":
 #       preco=distancia*2.9 +3 #pico
        
        if distancia<=10:
            preco=distancia*2.9 +.5
        elif distancia>10 and distancia<25:
            preco=distancia*1.85 +0.5
        elif distancia>25:
            preco=distancia*3 +0.5
    elif app == "Easy":
        preco= 2+ 0.26*tempo + distancia*1.40
    
    elif app == "WillGo":
        preco=0.32*tempo +1.61*distancia
        
    elif app == "Televo":
        preco=1.90+ 0.23*tempo + 1.35*distancia
    
    elif app =="Táxi comum":
        preco=4.5 + 0.55*tempo + 2.75*distancia #Bandeira 1
        #preco=4.5+ 0.55*tempo + 3.58*distancia #Bandeira 2
    elif app=="Táxi com 30% de desconto":
        preco_30=(4.5 + 0.55*tempo + 2.75*distancia)*0.7

        

    print(preco_30)
    

distancia=5.6
tempo=21
app="Táxi com 30% de desconto"
calculadora(distancia, tempo, app)
now = datetime.now()
print(now)