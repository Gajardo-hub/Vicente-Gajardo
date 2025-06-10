# uso y explicacion de LISTAS

#     -6 -5 -4 -3  -2 -1
# lista=[5, 7, 2, 9, 10, 2]
# #      0  1  2  3  4   5
 
# print(lista[-6]) # acceso al valor por indice nevativo
# print(lista[0]) # acceso al valor por indice positivo

# # mostrar toda la lista
# print(lista)

# for num in lista:
#     print(num)

# hacer una lista de 5 notas luego sacar su promedio. Las notas deben ser valores int ej: 55,32.

# notas=[34,45,65,70]
# print(notas)
# c=0
# suma=0
# for nota in notas:
#    suma+=nota
#    c+=1
# prom=suma/c
# print("El promedio es ", round(prom))

# for nota in notas:
#    if notas>=40:
#       print("Paso")
#    else:
#       print("NO PASO")
      


# nombres=["rei", "cony", "Kun"]
# apellidos=["Hood", "Kai", "Chan"]

# print(len(nombres))

# for i in range(len(nombres)):
#     print(f"Su nombre es {nombres[i]} {apellidos[i]}")

# frutas=["melo", "sandia", "kiwi"]
# for fruta in frutas:
#     print (f"La {fruta} tiene {len(fruta)} caracteres")

# autos=["audi", "toyota", "BMW", "KIA", "Mercedes"]

# for auto in autos:
#     print(auto)
#     if "a" in auto.lower():
#         print("La marca contiene una A")
#     else:
#         print("No contiene A")

  

# nombres=[]
# apellidos=[]

# while True:
#     print('''
#           1.- Insertar nombre y apellido
#           2.- Buscar nombre
#           3.- Buscar apellido
#           4.- Mostrar nombres y apellidos
#           5. Salir''')
#     op=int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre: ")
#             nombres.append(nom)
#             print(nombres)
#             ape=input("Ingrese un apellido: ")
#             apellidos.append(ape)
#             print(apellidos)
#         case 2:
#             buscar=input("Busque un nombre: ")
#             if buscar in nombres:
#                 print(f"El nombre {buscar} SI encuentra en la lista")
#             else:
#                 print(f"El nombre {buscar} NO se encuentra en la lista")
#         case 3:
#             buscar=input("Busque un apellido: ")
#             if buscar in apellidos:
#                 print(f"El apellido {buscar} SI encuentra en la lista")
#             else:
#                 print(f"El apellido {buscar} NO se encuentra en la lista")
#         case 4:
#             cont=0
#             for i in nombres:
#                 print(cont+1,".-", nombres[cont], apellidos[cont])
#                 cont+=1
#         case 5:
#             print("Saliendo...")
#             break
#         case _:
#             print("Selecciona una opcion valida")
        
        
        