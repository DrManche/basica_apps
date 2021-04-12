# Calculadora

def calculadora():
    from principal import principal
    from Funcions_list.operaciones import suma, resta, multiplicacion, division
    from Funcions_list.funcions import cls
    import time
    print("\nBienvenido(a) a mi calculadora basica.")
    print("\nQue deseas hacer:\n1) Sumar\n2) Restar\n3) Multiplicar\n4) Dividir\n5) Salir\n")

    while True:
        try:
            option = int(input("Elige una opcion: "))
            if 1 <= option <= 5:
                break
            else:
                print("Esa opcion no existe, intentalo de nuevo")
        except ValueError:
            print("Esa opcion no existe, intentalo de nuevo.")

    if option == 1:
        print(f"La suma es: {suma()}")
        while True:
            try:
                respuesta = input("Deseas realizar otra operacion? Si/No: ").lower()
                if respuesta == "si" or respuesta == "no":
                    break
                else:
                    print("Esa no es una opcion valida.")
            except ValueError:
                print("Esta no es una opcion, prueba de nuevo.")
        if respuesta == "si":
            cls()
            print(calculadora())
        elif respuesta == "no":
            print("\nGracias por usar el programa, vuelva pronto.")
            time.sleep(3)
            cls()
            principal()

    elif option == 2:
        print(f"La resta es: {resta()}")
        while True:
            try:
                respuesta = input("Deseas realizar otra operacion? Si/No: ").lower()
                if respuesta == "si" or respuesta == "no":
                    break
                else:
                    print("Esa no es una opcion valida.")
            except ValueError:
                print("Esta no es una opcion, prueba de nuevo.")
        if respuesta == "si":
            cls()
            print(calculadora())
        elif respuesta == "no":
            print("\nGracias por usar el programa, vuelva pronto.")
            time.sleep(3)
            cls()
            principal()

    elif option == 3:
        print(f"La multiplicacion entre ambos numeros es: {multiplicacion()}")
        while True:
            try:
                respuesta = input("Deseas realizar otra operacion? Si/No: ").lower()
                if respuesta == "si" or respuesta == "no":
                    break
                else:
                    print("Esa no es una opcion valida.")
            except ValueError:
                print("Esta no es una opcion, prueba de nuevo.")
        if respuesta == "si":
            cls()
            print(calculadora())
        elif respuesta == "no":
            print("\nGracias por usar el programa, vuelva pronto.")
            time.sleep(3)
            cls()
            principal()

    elif option == 4:
        print(f"La division entre los dos numeros es: {division()}")
        while True:
            try:
                respuesta = input("Deseas realizar otra operacion? Si/No: ").lower()
                if respuesta == "si" or respuesta == "no":
                    break
                else:
                    print("Esa no es una opcion valida.")
            except ValueError:
                print("Esta no es una opcion, prueba de nuevo.")
        if respuesta == "si":
            cls()
            print(calculadora())
        elif respuesta == "no":
            print("\nGracias por usar el programa, vuelva pronto.")
            time.sleep(3)
            cls()
            principal()

    elif option == 5:
        print("\nGracias por usar el programa, vuelva pronto.")
        time.sleep(3)
        cls()
        principal()
