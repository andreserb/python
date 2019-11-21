# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla un triángulo rectángulo como el de más abajo.
lista=[]
a=int(input("Ingrese la altura del triángulo (entero positivo): "))
for i in range(1,a+1,2):
    lista.append(i)
    print(' '.join(map(str, lista[::-1])))