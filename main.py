def registrar_usuario():
    print("Registrar usuario")


def agregar_serie():
    print("Agregar serie")


def ver_series():
    print("Ver series")


def buscar_serie():
    print("Buscar serie")


def dejar_resena():
    print("Dejar reseña")


def menu():
    while True:
        print("""==============================================================
        🎥   BIENVENIDO A SERIEMATCH (CLI Edition)  🎥 
==============================================================""")
        print("1. Registrar usuario")
        print("2. Agregar serie")
        print("3. Ver series")
        print("4. Buscar serie")
        print("5. Dejar reseña")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            agregar_serie()
        elif opcion == "3":
            ver_series()
        elif opcion == "4":
            buscar_serie()
        elif opcion == "5":
            dejar_resena()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


menu()
