#Ingresar dos numeros y muestre resultado por pantalla
#Si el divisor es 0 que muestre un error

a=float(input("Ingrese dividendo: "))
b=float(input("Ingrese divisor: "))

if b == 0:
    print("Error: No se puede realizar")
else:
    print(a/b)
