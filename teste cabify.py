# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:03:41 2016

@author: Michel
"""
from datetime import datetime
horario_atual = datetime.now()

dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6
distancia=9.9
tempo=21

dia_teste=5
hora_teste=13
if dia_teste>4: # se for fim de semana
    if distancia<10:
        preco_cabify=0.5+2.9*distancia
    elif distancia<25:
        preco_cabify=0.5*1.85*distancia
else:
    a="semana"
print(preco_cabify)
