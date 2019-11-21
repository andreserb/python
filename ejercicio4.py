#pide dos numeros por pantalla y muestra el cociente y 
#el restante

a=int(input("Ingrese dividendo: "))
b=int(input("Ingrese divisor: "))
c=a/b
d=a%b

print("{} entre {} da un cociente {} y un resto {}".format(a,b,c,d))