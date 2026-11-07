estudiantes = []

def ingresar_estudiantes():

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    id = int(input("Ingrese el ID: "))
    nota = float(input("Ingrese la nota: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "id": id,
        "nota": nota
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente")

def mostrar_estudiantes():

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")

    else:
        for estudiante in estudiantes:
            print("\n-------------------")
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("ID:", estudiante["id"])
            print("Nota:", estudiante["nota"])

def estadisticas_estudiantes():

    if len(estudiantes) == 0:
        print("No hay estudiantes para mostrar estadisticas")

    else:
        suma = 0
        aprobados = 0
        reprobados = 0

        mejor_estudiante = estudiantes[0]

        for estudiante in estudiantes:

            suma = suma + estudiante["nota"]

            if estudiante["nota"] >= 3:
                aprobados = aprobados + 1
            else:
                reprobados = reprobados + 1

            if estudiante["nota"] > mejor_estudiante["nota"]:
                mejor_estudiante = estudiante

        promedio = suma / len(estudiantes)

        print("\n===== ESTADISTICAS =====")
        print("Total de estudiantes:", len(estudiantes))
        print("Promedio general:", round(promedio, 2))
        print("Estudiantes aprobados:", aprobados)
        print("Estudiantes reprobados:", reprobados)

        print("\n===== MEJOR ESTUDIANTE =====")
        print("Nombre:", mejor_estudiante["nombre"])
        print("Nota:", mejor_estudiante["nota"])

while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1. Ingresar estudiantes")
    print("2. Mostrar estudiantes")
    print("3. Estadisticas estudiantes")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        ingresar_estudiantes()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        estadisticas_estudiantes()

    elif opcion == "4":
        print("Gracias por utilizar el programa")
        break

    else:
        print("Opcion no valida, intente nuevamente")
