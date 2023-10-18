
dia = int(input("Introduzca un dia "))
mes = int(input("Introduzca un mes "))

if mes<=0 or mes>12:
    print("la data es incorrecta")
elif dia >31 or dia <=0:
    print("la data es incorrecta")
elif dia >30 and (mes == 2 or mes == 4 or mes == 6 or mes == 11 or mes == 9):
          print("La data es incorrecta")
elif dia > 28 and mes == 2:
          print("La data es incorrecta")
else:
     print("la data ", dia ,"/",mes," es correcta")