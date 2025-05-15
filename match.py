#  USO Y EXPLICACION DE MATCH
# def suma2(n1,n2):
#   print("el resultado de la suma es", n1+n2)
  
# def suma():
#   n1=int(input("ingrese un numero: "))
#   n2=int(input("ingrese otro numero: "))
#   print("el resultado de la suma es", n1+n2)
# def resta():
#   n1=int(input("ingrese un numero: "))
#   n2=int(input("ingrese otro numero: "))
#   print("el resultado de la resta es", n1-n2)
# def multi():
#   n1=int(input("ingrese un numero: "))
#   n2=int(input("ingrese otro numero: "))
#   print("el resultado de la multiplicacion es", n1*n2)
# def divi():
#   n1=int(input("ingrese un numero: "))
#   n2=int(input("ingrese otro numero: "))
#   print("el resultado de la division es", n1/n2)

# def calcu():
#  while True:
#   op=int(input('''ingrese una opcion
#             1.- Suma
#             2.- Resta
#             3.- Multiplicacion
#             4.- Division
#             5.- Salir
#             '''))


#   match op:
#     case 1:
#       print("suma")
#       suma()
#     case 2:
#       print("Resta")
#       resta()
#     case 3:
#      print("Multiplicacion")
#      multi()
#     case 4:
#      print("Division")
#      divi()
#     case 5:
#      print("Salir")
#      break
#     case _:
#      print("Opcion invalida")
#      break
   
# calcu()


cantalum=int(input("Cantidad de alumnos: "))

promgen=0
contpromgen=0

for i in range(cantalum):
  cantnotas=int(input(f"ingrese la cantidad de notas del alumno {i+1}: "))
  notas=0
  for e in range(cantnotas):
   notas=float(input(f"ingrese la nota {e+1}: "))


promgen=cantnotas
prom=(notas/cantnotas)
print(f"el promedio de las notas es: {prom}")

if prom>=40:
    print("Aprobo")
else:
    print("Usted no aprobo, que penita")
    