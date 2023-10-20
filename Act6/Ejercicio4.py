print("escriba una sequencia de numeros positivos acabada en -1 y calcularemos su media aritmetica")
n = int(input("introduzca el primer numero "))
sum = 0
cont = 0
while n >=0:
    sum = sum +n
    cont = cont +1
    n = int(input("introduzca otro numero "))
if n==-1 or n>=0:  
    print("La mitjana aritmètica es: ", sum/cont)
else:
      print("Error numero negativo insertado")