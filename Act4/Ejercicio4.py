#Ejercicio 4


print("Introduzca tres numeros y le dire qual es mayor")
A = int(input("Introduzca un numero A "))
B = int(input ("Introduzca un numero B "))
C = int(input ("Introduzca un numero B "))

if A == B == C:
        print("A,B,C son iguales")
else:
        if A>=B and A>C:
                print ("A es el mayor")
        elif B>A and B>C:
                print ("B es el mayor")
        else:
                print("C es el mayor")