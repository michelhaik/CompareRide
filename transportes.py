# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:29:53 2016

@author: Michel
"""
dinamica=1
from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6



def calculadora(distancia, tempo, app):
    if app == "Uber":
        preco=(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)*dinamica
 
            
            
            
            
    elif app == "Easy":
        preco_easy= 2+ 0.26*tempo + distancia*1.40
    
    elif app == "WillGo":
        preco_WillGo=0.32*tempo +1.61*distancia
        
    elif app == "Televo":
        preco_Televo=1.90+ 0.23*tempo + 1.35*distancia
    
    elif app =="Táxi comum":
        #bandeira 2- domingo o dia todo e segunda-sabado das 20 as 6
        if dia_semana==6 or (hora_oficial>=0 and hora_oficial<6) or (hora_oficial>=20):
            preco_taxi=4.5+ 0.55*tempo + 3.58*distancia #bandeira 2
   
        else:
            preco_taxi=4.5 + 0.55*tempo + 2.75*distancia #bandeira 1
            
            
            
    elif app=="Táxi com 30% de desconto":
        preco_30=(4.5 + 0.55*tempo + 2.75*distancia)*0.7

        

distancia=5.6
tempo=21
app="Táxi comum"#Táxi com 30% de desconto"
calculadora(distancia, tempo, app)
print(preco_taxi)

