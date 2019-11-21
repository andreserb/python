
#Escribir un programa que pregunte el nombre del usuario 
#en la consola y despues de que el usuario lo introduzca 
#muestre por pantalla <NOMBRE> tiene <n> letras, 
#donde <NOMBRE> es el nombre de usuario en mayusculas y 
#<n> es el numero de letras que tienen el nombre.

name=input("Como te llamas ")
print("{} tiene {} ".format(name.upper(), len(name)))