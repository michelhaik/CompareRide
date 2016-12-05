# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:29:53 2016

@author: Michel
"""
from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6



def calculadora(distancia, tempo, app):
    if app == "Uber":
        preco=(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)*dinamica
        
    elif app == "Cabify":
        # Os horários de pico são das 7 às 10 e das 17 as 21, de segunda a sexta-feira
        if dia_semana>=0 and dia_semana<5:
            if hora_oficial>=7 and hora_oficial<10  or hora_oficial>=17 and hora_oficial<21:
        
                if distancia<=10:
                    preco=distancia*2.9 +3
                elif distancia>10 and distancia<25:
                    preco=distancia*1.85 +3
                elif distancia>25:
                    preco=distancia*3 +3
        else:
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
        #bandeira 2- domingo o dia todo e segunda-sabado das 20 as 6
        if dia_semana==6 or (hora_oficial>=0 and hora_oficial<6) or (hora_oficial>=20):
            preco=4.5+ 0.55*tempo + 3.58*distancia #bandeira 2
   
        else:
            preco=4.5 + 0.55*tempo + 2.75*distancia #bandeira 1
            
            
            
    elif app=="Táxi com 30% de desconto":
        preco_30=(4.5 + 0.55*tempo + 2.75*distancia)*0.7

        

print(preco)

distancia=5.6
tempo=21
app="Táxi comum"
calculadora(distancia, tempo, app)

