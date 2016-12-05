# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:22:57 2016

@author: Michel
"""
distancia=5.6
tempo=21
from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6

preco_uber=(2+ tempo*0.26 + distancia*1.40 + distancia*0.1)*dinamica

preco_easy= 2+ 0.26*tempo + distancia*1.40


preco_WillGo=0.32*tempo +1.61*distancia

   
preco_Televo=1.90+ 0.23*tempo + 1.35*distancia


#bandeira 2- domingo o dia todo e segunda-sabado das 20 as 6
if dia_semana==6 or (hora_oficial>=0 and hora_oficial<6) or (hora_oficial>=20):
    preco_taxi=4.5+ 0.55*tempo + 3.58*distancia #bandeira 2
   
else:
    preco_taxi=4.5 + 0.55*tempo + 2.75*distancia #bandeira 1



preco_30=(4.5 + 0.55*tempo + 2.75*distancia)*0.7





print(preco_taxi)
print(preco_uber)
print(preco_easy)
print(preco_WillGo)
print(preco_Televo)
print(preco_30)

