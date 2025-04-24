# Explicacion y uso de while 

# import time
# num=10

# while num<5:
#     print("Hola")
#     num+=1


# while num>0:
#     print(num)
#     time.sleep(1) 
#     num-=1


clave=3344
intentos=3
password=int(input("ingrese su clave: " ))

while clave!=password or intentos==0:
    intentos-=1
    print(f"ERROR, le quedan {intentos} intentos")
    password=int(input("ingrese su clave:" ))

    if intentos<=1:
        break

if intentos!=0 and clave==password:
   print("usted ingreso al sistema")
else:
    print("bloqueo")