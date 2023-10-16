#Ejercicio 1
print("introduzca la base y la altura de un triangulo y le calcularemos el area")
base = int(input("Introduzca la base del triangulo "))
altura = int(input("Introduzca el altura del triangulo "))

print("El area del triangulo es: ",(base*altura)/2)

#Ejercicio 2

print("introduzca dos numeros y hare la division del mayor entre el menor")

A = int(input("Introduzca un numero A "))
B= int(input("Introduzca un numero B "))

if A>B:
    print("A es el mayor y el resultado es: ", A/B)
else:
    print ("B es el mayor y el resultado es: ", B/A)    

#Ejercicio3

#Ejercicio4

n = int (3)
contraseña = str ('eureka')
intento = str(input("Introduzca la contraseña: "))

while(n>=2 and intento != "eureka"):
    n = n-1
    intento = input("Contraseña incorrecta, le quedan {n} intentos: ")
    
  
if intento=="eureka":
    print("Contraseña correcta")
else:
    print("Lo sentimos no te quedan intentos")
