#sacar promedio 3 numeros
print("ingrese 3 numeros para sacar un promedio")
n1=int(input("ingrese un numero "))
n2=int(input("ingrese un numero "))
n3=int(input("ingrese un numero "))
prom=(n1+n2+n3)/3
print("El promedio es", prom)

if prom>=40:
    print("El alumno aprobó")
else:
    print("El alumno reprobó")
