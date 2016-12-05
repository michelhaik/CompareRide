# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:50:43 2016

@author: Michel
"""
dinamica=1
from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6
distancia=5.6
tempo=21

    #Uber
preco_uber=(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)
        
   #Cabify
        # Os horários de pico são das 7 às 10 e das 17 as 21, de segunda a sexta-feira
"""
if dia_semana>=0 and dia_semana<5:
    if hora_oficial>=7 and hora_oficial<10  or hora_oficial>=17 and hora_oficial<21:
        
        if distancia<=10:
            preco_cabify=distancia*2.9 +3
        elif distancia>10 and distancia<25:
            preco_cabify=distancia*1.85 +3
        elif distancia>25:
            preco_cabify=distancia*3 +3
else:
    if distancia<=10:
        preco_cabify=distancia*2.9 +.5
    elif distancia>10 and distancia<25:
        preco_cabify=distancia*1.85 +0.5
    elif distancia>25:
        preco_cabify=distancia*3 +0.5
        
   """     
            
            
            
    #easy
preco_easy= 2+ 0.26*tempo + distancia*1.40
    
    #willgo
preco_WillGo=0.32*tempo +1.61*distancia
        
    #televo
preco_Televo=1.90+ 0.23*tempo + 1.35*distancia
    
   #taxi comum 
        #bandeira 2- domingo o dia todo e segunda-sabado das 20 as 6
if dia_semana==6 or (hora_oficial>=0 and hora_oficial<6) or (hora_oficial>=20):
    preco_taxi=4.5+ 0.55*tempo + 3.58*distancia #bandeira 2
   
else:
    preco_taxi=4.5 + 0.55*tempo + 2.75*distancia #bandeira 1
    #taxi com 30%
preco_30=(4.5 + 0.55*tempo + 2.75*distancia)*0.7
#print(preco_cabify)

print(preco_30, "taxi 30")
print(preco_easy, "easy")
print(preco_WillGo, "will")
#print(preco_cabify)
print(preco_uber, "uber")
print(preco_Televo, "televo")