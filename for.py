# #Conoceremos la estructura y uso de for 

# #for i in range (10):
# print("Repeticion numero",i+1)


# #ingrese un nombre y salude 3 veces 

# nombre=input("ingrese un nombre ")


# #for i in range(3):
# print("Hola", nombre)


# #pida al usuario 3 notas y saque el promedio

# suma=0
# for i in range(3):
#    n1=int(input("ingrese la nota "))
#    suma=suma+n1
# prom=suma/3
# print("El promedio es ",round (prom))


# cant=int(input("ingrese la cantidad de notas "))
# suma=0
# for i in range(cant):
#    n1=int(input("ingrese la nota "))
#    suma=suma+n1
# prom=suma/cant
# print("El promedio es ",round (prom))


cant=int(input("ingrese la cantidad de numeros "))
suma=0
for i in range(cant):
   n1=int(input("ingrese la nota "))
   suma+=n1
print("La suma de todos los numeros es ",suma)