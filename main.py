
def pedirOpcion():
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
    print("MENU");
    print("1.mayor y menor")
    print("2.valor mayor")
    print("3.multiplo de 7")
    print("4.par o impar")
    print("5.Telefonia")
    print("6.Salir")

    print("Elige una opcion")

    opcion = pedirOpcion()

    if opcion == 1:
        print("Bienvenido a mayor y menor")
        num1=int(input("Ingrese un numero"));
        num2=int(input("Ingrese otro numero"));

        if(num1>num2):
            mensaje="El ingreso uno es el mayor y el ingreso dos es el menor"
        elif(num1==num2):
            mensaje="LOS NUMEROS SON IGUALES"
        else:
            mensaje="El ingreso dos es el mayor y el ingreso uno es el menor"

        print(mensaje);
    elif opcion == 2:
        print("Bienvenido al valor mayor")
        num1 = int(input("Ingrese un numero"));
        num2 = int(input("Ingrese otro numero"));
        num3 = int(input("Ingrese otro numero"));

        if (num1 > num2 and num1>num3):
            mensaje = "El ingreso uno es el mayor"
        elif(num2 > num1 and num2>num3):
            mensaje = "El ingreso dos es el mayor"
        elif (num3 > num1 and num3 > num2):
            mensaje = "El ingreso tres es el mayor"
        elif (num1 == num2):
            mensaje = "Los numeros son iguales"
        else:
            mensaje = "El ingreso dos es el mayor y el ingreso uno es el menor"
        print(mensaje);

    elif opcion == 3:
        print("Bienvenido al multiplo de 7")

        num1 = int(input("Ingrese un numero"));
        num2 = int(input("Ingrese otro numero"));
        num3 = int(input("Ingrese otro numero"));

        suma= int(num1+num2+num3);
        if (suma % 7 == 0):
            resultado = "La suma es multiplo de 7"
        else:
            resultado = "La suma no es multiplo de 7"

        print("La suma es",suma)
        print(resultado)

    elif opcion == 4:
        print("Bienvenido al par o impar")
        num1 = int(input("Ingrese un numero"));
        num2 = int(input("Ingrese otro numero"));
        num3 = int(input("Ingrese otro numero"));
        promedio=float(num1+num2+num3)/3

        if(promedio % 2==0):
            print("El promedio es par")
        else:
            print("El promedio no es par")
        print(promedio)
    elif opcion == 5:
        print("Bienvenido a la Telefonia")
        nombre=str(input("Ingrese su nombre"));
        nacionales=int(input("Ingrese los minutos nacionales"))
        internacionales=int(input("Ingrese los minutos internacionales"))


        suma=int(nacionales+internacionales);
        total=0;
        todo=int(suma-25)
        if (suma<=25):
            print(nombre,"¡LOS PRIMEROS 25 MINUTOS SON GRATIS!");
        elif(nacionales<=25):
            acu=nacionales-25;
            internacionales+=acu;
            total=internacionales*2.5;
        else:
            nacionales-=25;
            total=(nacionales*0.5)+(internacionales*2.5);
        print("Total a pagar Q",total);



    elif opcion == 6:
        salir = True
    else:
        print("INTRODUCE UN NUMERO ENTRE 1 Y 6")

print("ADIOS HASTA PRONTO")