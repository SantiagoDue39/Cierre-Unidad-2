estudiantes = []

def mostrar_menu():
    print("\n===== SISTEMA DE ESTUDIANTES =====")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Consultar promedio de un estudiante")
    print("4. Mostrar estadisticas generales")
    print("5. Salir del programa")
    print()

def calcular_promedio(calificaciones):
    suma = 0

    for calificacion in calificaciones:
        suma += calificacion

    promedio = suma / 3
    return promedio

def registrar_estudiante():   # Use AI para algunas partes 
    identificacion = input("Numero de identificacion: ")
    nombre = input("Nombre del estudiante: ")

    calificaciones = []

    for i in range(3):
        while True:
            calificacion = int(input(f"Ingresa la calificacion {i + 1}: "))
            if calificacion >= 0 and calificacion <= 100:
                calificaciones.append(calificacion)
                break
            else:
                print("La calificacion debe estar entre 0 y 100.")

    calificaciones = tuple(calificaciones)

    promedio = calcular_promedio(calificaciones)
    aprobado = promedio >= 70

    if aprobado >= 70:
        situacion = "Aprobado"
    else:
        situacion = "Reprobado"

    estudiante = {"id": identificacion, "nombre": nombre, "calificaciones": calificaciones, "promedio": promedio, "aprobado": aprobado, "situacion": situacion}
    estudiantes.append(estudiante)

    print("Promedio:", round(promedio, 2))
    print("Situacion:", situacion)

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print("\nIdentificacion:", estudiante["id"])
        print("Nombre:", estudiante["nombre"])
        print("Calificaciones:", estudiante["calificaciones"])
        print("Promedio:", round(estudiante["promedio"], 2))
        print("Situacion:", estudiante["situacion"])

def consultar_estudiante():
    identificacion = input("Ingresa la identificacion: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            print("\nEstudiante encontrado.")
            print("Nombre:", estudiante["nombre"])
            print("Promedio:", round(estudiante["promedio"], 2))
            print("Situacion:", estudiante["situacion"])

            encontrado = True
            break
    if not encontrado:
        print("No se encontro ningun estudiante con esa identificacion.")

def mostrar_estadisticas():   # Lo siento profe use AI en esta parte :(
    if len(estudiantes) == 0:
        print("Todavia no hay estudiantes registrados.")
        return

    total = len(estudiantes)
    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_alto = estudiantes[0]["promedio"]

    for estudiante in estudiantes:
        suma_promedios += estudiante["promedio"]

        if estudiante["aprobado"]:
            aprobados += 1
        else:
            reprobados += 1

        if estudiante["promedio"] > promedio_alto:
            promedio_alto = estudiante["promedio"]

    promedio_general = suma_promedios / total

    print("Estudiantes registrados:", total)
    print("Promedio general:", round(promedio_general, 2))
    print("Estudiantes aprobados:", aprobados)
    print("Estudiantes reprobados:", reprobados)
    print("Promedio mas alto:", round(promedio_alto, 2))

while True:
    mostrar_menu()
    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
            registrar_estudiante()
    elif opcion == 2:
            mostrar_estudiantes()
    elif opcion == 3:
            consultar_estudiante()
    elif opcion == 4:
            mostrar_estadisticas()
    elif opcion == 5:
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Opcion no valida, intenta de nuevo")
