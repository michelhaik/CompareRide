# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:04:51 2016

@author: Michel
"""
"""
g1=True
a=ed1.get()
if "." in a:
    b=a.split(".")
    if len(b)>2:
        g1=False
    else:
        for i in range(len(b)):
            if not (b[i].isnumeric()):
                g1=False
    
else:
    if not a.isnumeric():
        g1=False
a3=float(a)

g2=True
a=ed2.get()
if "." in a:
    b=a.split(".")
    if len(b)>2:
        g2=False
    else:
        for i in range(len(b)):
            if not (b[i].isnumeric()):
                g=False
    
else:
    if not a.isnumeric():
        g=False
a3=float(a)
if g1:
    if g2:
        tempo = float(ed1.get())
        distancia = float(ed2.get())
        print(tempo,distancia)
else:
    lb3["text"] = "Comandos inválidos"
"""
a="2.0"
f=a.isalpha()
print(f)
a="1"
b="1"
if (a.isalpha()) or (b.isalpha()): # float(ed1.get().isnumeric()) and float(ed2.get().isnumeric()):
    print("nwe")
else:
    print("fsdfa")