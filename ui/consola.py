class ConsolaUI:
    def __init__(self):
        pass

    def registrar_usuario(self):
        print("Registrar usuario")

    def agregar_serie(self):
        print("Agregar serie")

    def ver_series(self):
        print("Ver series")

    def buscar_serie(self):
        print("Buscar serie")

    def dejar_resena(self):
        print("Dejar reseña")

    def iniciar_aplicacion(self):
        print("Ejecuto iniciar app..")
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
                self.registrar_usuario()
            elif opcion == "2":
                self.agregar_serie()
            elif opcion == "3":
                self.ver_series()
            elif opcion == "4":
                self.buscar_serie()
            elif opcion == "5":
                self.dejar_resena()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
