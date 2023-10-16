#Ejercicio4

n = int (3)
contraseña = str ('eureka')
intento = str(input("Introduzca la contraseña: "))

while(n>=2 and intento != "eureka"):
    n = n-1
    intento = input(f"Contraseña incorrecta, le quedan {n} intentos: ")
    
  
if intento=="eureka":
    print("Contraseña correcta")
else:
    print("Lo sentimos no te quedan intentos")
