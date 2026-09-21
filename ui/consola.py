class ConsolaUI:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def registrar_usuario(self):
        print("Registrar usuario")

    def agregar_serie(self):
        print("Agregar serie")

    def busqueda_BST(self):
        titulo = input("Ingrese el titulo a buscar: ")
        resultado = self.arbol.buscar(titulo.lower(), clave=lambda s: s.titulo.lower())
        if resultado:
            print(resultado)
        else:
            print("No se encontró")
        print("Fin de resultados")

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
            print("4. Buscar serie por titulo")
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
                # self.busqueda_BST()
                self.catalogo.busqueda_BST()
            elif opcion == "5":
                self.dejar_resena()
            elif opcion == "6":
                self.catalogo.filtrar_serie_genero()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
