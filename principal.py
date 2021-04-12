# Aplicacion multi apps

def principal():
    from Funcions_list.funcions import cls
    from Calculadora.calcul import calculadora
    import time

    print("\nBienvenido(a) al selector de aplicaciones.")
    print("\nQue deseas usar:\n1) Calculadora basica\n2) \n3) \n4) \n5) \n6) \n7) \n8) \n9) \n10) \n11) Salir")

    while True:
        try:
            option = int(input("\nElige un programa: "))
            if 11 >= option >= 1:
                break
            else:
                print("Eso no es una opcion, intenta de nuevo.")
        except ValueError:
            print("Eso no es una opcion.")

    if option == 1:
        cls()
        calculadora()
    elif option == 2:
        cls()
    elif option == 3:
        cls()
    elif option == 4:
        cls()
    elif option == 5:
        cls()
    elif option == 6:
        cls()
    elif option == 7:
        cls()
    elif option == 8:
        cls()
    elif option == 9:
        cls()
    elif option == 10:
        cls()
    elif option == 11:
        print("\nGracias por usar el programa, vuelva pronto.")
        time.sleep(3)
        cls()
        exit()
