# Operadoras basicas.

def suma():
    while True:
        try:
            cantidad = int(input("Cuantos numeros deseas sumar: "))
            if 10 >= cantidad >= 2:
                print(f"Seleccionado correctamente, numeros a sumar: {cantidad}")
                break
            elif cantidad > 10:
                print("No se permite sumar más de 10 numeros.")
            else:
                print("Opcion incorrecta, debe ser un numero de 2-10.")
        except ValueError:
            print("Opcion incorrecta, debe ser un numero de 2-10.")

    if cantidad == 2:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b

    if cantidad == 3:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c

    if cantidad == 4:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d
    if cantidad == 5:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e

    if cantidad == 6:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e + f
    if cantidad == 7:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e + f + g
    if cantidad == 8:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e + f + g + h
    if cantidad == 9:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e + f + g + h + i
    if cantidad == 10:
        while True:
            try:
                a = float(input("Primer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                j = float(input("Decimo numero a sumar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a + b + c + d + e + f + g + h + i + j


def resta():
    while True:
        try:
            cantidad = int(input("Cuantos numeros deseas restar: "))
            if 10 >= cantidad >= 2:
                print(f"Seleccionado correctamente, numeros a restar: {cantidad}")
                break
            elif cantidad > 10:
                print("No se permite restar más de 10 numeros.")
            else:
                print("Opcion incorrecta, debe ser un numero de 2-10.")
        except ValueError:
            print("Opcion incorrecta, debe ser un numero de 2-10.")

    if cantidad == 2:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b

    if cantidad == 3:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c

    if cantidad == 4:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d
    if cantidad == 5:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e

    if cantidad == 6:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e - f
    if cantidad == 7:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e - f - g
    if cantidad == 8:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e - f - g - h
    if cantidad == 9:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e - f - g - h - i
    if cantidad == 10:
        while True:
            try:
                a = float(input("Primer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                j = float(input("Decimo numero a restar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a - b - c - d - e - f - g - h - i - j


def multiplicacion():
    while True:
        try:
            cantidad = int(input("Cuantos numeros deseas multiplicar: "))
            if 10 >= cantidad >= 2:
                print(f"Seleccionado correctamente, numeros a multiplicar: {cantidad}")
                break
            elif cantidad > 10:
                print("No se permite multiplicar más de 10 numeros.")
            else:
                print("Opcion incorrecta, debe ser un numero de 2-10.")
        except ValueError:
            print("Opcion incorrecta, debe ser un numero de 2-10.")

    if cantidad == 2:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b

    if cantidad == 3:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c

    if cantidad == 4:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d
    if cantidad == 5:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e

    if cantidad == 6:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e * f
    if cantidad == 7:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e * f * g
    if cantidad == 8:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e * f * g * h
    if cantidad == 9:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e * f * g * h * i
    if cantidad == 10:
        while True:
            try:
                a = float(input("Primer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")

        while True:
            try:
                b = float(input("Segundo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                c = float(input("Tercer numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                d = float(input("Cuarto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                e = float(input("Quinto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                f = float(input("Sexto numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                g = float(input("Septimo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                h = float(input("Octavo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                i = float(input("Noveno numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        while True:
            try:
                j = float(input("Decimo numero a multiplicar: "))
                break
            except ValueError:
                print("Eso no es un numero, intenta de nuevo.")
        return a * b * c * d * e * f * g * h * i * j


def division():
    while True:
        try:
            a = float(input("Ingresa el numerador: "))
            break
        except ValueError:
            print("Eso no es un numero, intenta de nuevo.")
    while True:
        try:
            b = float(input("Ingresa el denominador: "))
            if b != 0:
                break
            else:
                print("Error, el denominador debe ser diferente de cero.")
        except ValueError:
            print("Eso no es un numero, intenta de nuevo.")
    return a / b
