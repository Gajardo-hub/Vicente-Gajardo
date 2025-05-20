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


# cant=int(input("ingrese la cantidad de numeros "))
# suma=0
# for i in range(cant):
#    n1=int(input("ingrese la nota "))
#    suma+=n1
# print("La suma de todos los numeros es ",suma)


# frase=input("ingrese una frase ")
# cantcar=0
# v=0
# cons=0
# e=0
# for i in frase:
#     print(i)
#     cantcar+=1

#     if i in "aeiouAEIOU":
#       v+=1
#     elif i==" ":
#        e+=1
#     else:
#        cons+=1
    

# print(f"el total de caracteres es {cantcar}")
# print(f"el total de vocales es {v}")
# print(f"el total de cons es {cons}")


# from random import randint
# a=randint(1,100) 
# print(f"el numero generado es {a}" )


# PERROS DE CASA 

# import random 

# while True:
#  try:
#   per=int(input("Cuantos perros van a cazar?: "))
#   break
#  except ValueError:
#    print("Error, ingrese un numero entero")

# resumen=[]

# print(f"Saldras {per} perros.")
# print("Cada perro debe traer minimo 3 conejos.")

# for i in range (per):
#     cone=random.randint(0,5)
    
#     print(f"El perro {i+1} trajo {cone} conejos")
#     if cone>=3:
#      print("buen perrito, tiene filete.")
#      resumen.append(f"El perro {i+1} cumplio.")
#     else:
#      print("mal perrito, no filete >:(.")
#      resumen.append(f"El perro {i+1} NO cumplio.")

# print("\nResumen:")
# for r in resumen:
#   print(r)

