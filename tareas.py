# from random import randint
# a=randint(1,100) 
# print(f"el numero generado es {a}" )

# EJERCICIO 1

# num=int(input("ingrese un numero: "))
# if num%2==0:
#    print("par")
# else:
#    print("impar")

# print("mostrar numeros pares")
# for i in range(1,num+1):
#    if i%2==0:
#      print(i)
    
# print("mostrar numeros impares")
# for i in range(1,num+1):
#    if i%2!=0:
#      print(i)



# EJERCICIO 2

# cont=0
# total=0
# opc=0
# while opc !=2:
#     print("1.-Agregar nuevo numero ")
#     print("2.-Salir")
#     opc = int(input("->:"))
#     if(opc==1):
#         num=int(input("ingrese un numero: "))
#         cont+=1
#         total+=num
# print(f"la cantidad de numeros ingresados son {cont}")
# print(f"la suma de cada numero es {total}")



# EJERCICIO 3


# from random import randint
# a=0
# b=0
# r=a*b
# while r<50:
#     a=int(input("ingrese el valor de a: "))
#     b=randint(2,8)
#     r=a*b
#     print(f"el numero aleatorio es {b}")
#     print(f"la multiplicacion entre {b} x {a} = {r}")
#     if r<50:
#      print("intente nuevamente")
# print("LOGRO LA META")



from random import randint
num=int(input("ingrese un numero "))
num2=int(input("ingrese un numero mayor al primero "))


if num>=num2:
    print("Error, el numero es menor al numero 2")
else:
    print(f"su numero es {num} y {num2}")
numr=randint(num,num2)

print("▄ "*numr)
