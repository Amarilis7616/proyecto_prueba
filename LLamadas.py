"""Autor: Amarilis Cueva
Fecha:13-05-2020
Tema: Condicionales
"""
print("--Programa de Llamdas--")
while True:
    telefono = int(input("Ingrese el número de teléfono:"))
    if len(str(telefono))==9:
        telefono=str(telefono)
        dig=telefono[6]+telefono[7]+telefono[8]
        digp=telefono[0]+telefono[1]+telefono[2]
        break

while True:
    horat = int(input("Hora de la llamada entrante:"))
    if horat>=00 and horat<=23:
        break
while True:
    minutos=int(input("Minutos de la llamada entrante:"))
    if minutos>=00 and minutos<=59:
        break
if horat==0:
    cminut=minutos
else:
    cminut=((horat*60)+minutos)

if cminut>=0 and cminut<=500:
    print("Contestar")
elif cminut>500 and cminut<=780:
    if dig=='909':
        print("Contestar")
    else:
        print("No Contestar")
elif cminut>780 and cminut<=1190:
    if digp=='877':
        print("No Contestar")
    else:
        print ("Contestar")
elif  cminut>1190 and cminut<1440:
    print("No Contestar")



















