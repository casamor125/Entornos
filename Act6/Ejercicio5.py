print("escriba una sequencia de numeros acabada en 0 ")
print("y le diremos su maximo su minimo y calcularemos su media aritmetica")
n = int(input("introduzca el primer numero "))
sum = 0
cont = 0
min = n
max = n
while n > 0:
    cont = cont +1
    sum = sum +n
    if max <n:
        max = n
    if min >n:
        min = n
    n = int(input("introduzca el siguiente numero "))
if n <0:
    print("Error numero negativo introducido")
else:
    print("el maximo introducido es = ",max," y el minimo = ",min,)
    print("la media aritmètica es = ",sum/cont)
