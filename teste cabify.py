from datetime import datetime
horario_atual = datetime.now()
distancia=float(input("distancia"))
tempo=10
dia_completo = datetime.now()
hora_oficial=dia_completo.hour
dia_semana=dia_completo.weekday() # Pelo Python, Segunda é 0, Terça é 1, quarta é 3..... até domingo=6

print(dia_semana)      
print(hora_oficial)   
if dia_semana>=0 and dia_semana<5: #true
    if hora_oficial>=7 and hora_oficial<10  or hora_oficial>=17 and hora_oficial<21:
        
        if distancia<=10:
            preco_cabify=distancia*2.9 +3
        elif distancia>10 and distancia<25:
            preco_cabify=(distancia-10)*1.85 + 32
        elif distancia>25:
            preco_cabify=(distancia-25)*3 +59.75
    else:
        if distancia<=10:
            preco_cabify=distancia*2.9 +.5
        elif distancia>10 and distancia<25:
            preco_cabify=(distancia-10)*1.85 +29.5
        elif distancia>25:
            preco_cabify=(distancia-25)*3 +57.25
    
        
else:
    if distancia<=10:
            preco_cabify=distancia*2.9 +.5
    elif distancia>10 and distancia<25:
            preco_cabify=(distancia-10)*1.85 +29.5
    elif distancia>25:
            preco_cabify=(distancia-25)*3 +57.25
    

if preco_cabify<7:
    preco_cabify=7
print(preco)