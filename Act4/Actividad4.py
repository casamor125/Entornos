#Ejercicio 1

print("Introduzca dos numeros y le dire que numeros ha introducido")
A = int(input("Introduzca un numer A"))
B = int(input ("Introduzca un numero B"))
print("El numero A es:", A ,"El numero B es:",B)

#Ejercicio 2

print("Introduzca dos numeros y le dire el resultado de su suma, resta, multiplicacion y division")
A = int(input("Introduzca un numer A"))
B = int(input ("Introduzca un numero B"))
print("El numero A es:", A ,"El numero B es:",B) 
print ("suma = ",A+B," resta = ", A-B," multiplicacion = ",A*B," division (A/B) = ", A/B )

#Ejercicio 3

print("Introduzca dos numeros y le dire qual es mayor")
A = int(input("Introduzca un numer A"))
B = int(input ("Introduzca un numero B"))

if A > B:
        print("A es mayor que B")
elif A < B:
        print("B es mayor que A")
else:
        print("A y B son iguales")

#Ejercicio 4


print("Introduzca tres numeros y le dire qual es mayor")
A = int(input("Introduzca un numer A"))
B = int(input ("Introduzca un numero B"))
C = int(input ("Introduzca un numero B"))

if A == B == C:
        print("A,B,C son iguales")
else:
        if A>B and A>C:
                print ("A es el mayor")
        elif B>A and B>C:
                print ("B es el mayor")
        else:
                print("C es el mayor")
        

#Ejercicio 5

print("Introduzca tres numeros y si el primero es negativo imprimire el producto si no la suma")
A = int(input("Introduzca un numer A"))
B = int(input ("Introduzca un numero B"))
C = int(input ("Introduzca un numero B"))


if A <0:
        print("El producte dels tres es: ",A*B*C)
else:
        print("La suma dels tres es: ",A+B+C)        
