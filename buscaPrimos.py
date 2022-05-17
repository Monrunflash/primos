#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# Abre el fichero
import os

ruta = "fichero.txt"
#comprobamos que la ruta exista
if os.path.isfile(ruta):
    fichero = open(ruta,"r+")
    tieneContenido = fichero.read()
    primos = tieneContenido.split(",")
else:
    fichero = open(ruta,"w+")
    fichero.write("2")
    primos = [2]
lista = list()
# Selecciona el último número de la lista para empezar a probar
print(primos)
count = int(primos[len(primos)-1])
limite = int(input("¿Cuántos nuevos números quieres añadir? "))
# Recorre todos los numeros hasta el limite de números seleccionados
for n in range(count+1,count+limite):
    primo = True
    for elem in range(2,n):
        if n%elem == 0:
            primo = False
            break
    if primo:
        lista.append(n)
        print(n)
# Convierte a string la nueva lista para almacenarla en el fichero
listaAStr = str(lista).replace("[","").replace("]","").replace(" ","")
fichero.write(","+listaAStr)
fichero.close()
print("Ha agregado %s nuevos números primos" % len(lista))
