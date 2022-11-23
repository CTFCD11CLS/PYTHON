def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print("1.TABLA DE MULTIPLICACION ")
    print("2.NUMEROS IMPARES")
    print("3.MULTIPLOS")
    print("4.Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("BIENVENIDO A LA TABLA DE MULTIPLICACION")
        tabla = int(input("Ingrese la tabla a multiplicar"))
        inicio=int(input("Ingrese el inicio de la tabla"))
        final=int(input("Ingrese el final de la tabla"))

        for i in range(inicio, final + 1):
         if tabla < 0:
            conver=(tabla*-1)
            print(conver, "x", i, "=", conver * i);
         else:
          print(tabla, "x", i, "=", tabla * i);

    elif opcion == 2:
        print("BIENVENIDO A LOS NUMEROS IMPARES DE 1")
        final=int(input("Ingrese el valor final"))

        for i in range(1,final+1):
            if(i % 2==1):
                print(i)

    elif opcion == 3:
        print("BIENVENIDO A LOS MULTIPLOS")

        multiplo=int(input("Ingrese in valor del multiplo"))


        for i in range(1,100+1):
            if(i % multiplo==0):
                print(i);
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")