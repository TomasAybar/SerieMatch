class ConsolaUI:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def registrar_usuario(self):
        print("Registrar usuario")

    def agregar_serie(self):
        print("Agregar serie")

    def dejar_resena(self):
        print("Dejar reseña")

    def iniciar_aplicacion(self):
        while True:
            print("""==============================================================
        🎥   BIENVENIDO A SERIEMATCH (CLI Edition)  🎥 
==============================================================""")
            print("1. Registrar usuario")
            print("2. Agregar serie")
            print("3. Ver series")
            print("4. Buscar serie")
            print("5. Dejar reseña")
            print("6. Filtrar por género")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.agregar_serie()
            elif opcion == "3":
                self.catalogo.listar_series()
            elif opcion == "4":
                self.catalogo.buscar_por_titulo_BST()
            elif opcion == "5":
                self.dejar_resena()
            elif opcion == "6":
                self.catalogo.filtrar_serie_x_genero()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
