print("Introduzca un numero y le mostrare su factorial")
num = int(input("Introduzca el numero: "))
resultado = num

while(num>1):
    num=num-1
    resultado = resultado*num

print("el resultado del factorial es: ", resultado)

    