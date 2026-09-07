class ConsolaUI:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def registrar_usuario(self):
        print("Registrar usuario")

    def agregar_serie(self):
        print("Agregar serie")

    def ver_series(self):
        print("\n=== CATÁLOGO DE SERIES ===")

        if not self.catalogo.series:
            print("No hay series cargadas en el sistema.")
            return

        for serie in self.catalogo.series:
            print(
                f"[{serie.id}] {serie.titulo} - {serie.plataforma} - {serie.puntuacion}"
            )

    def buscar_serie(self):
        titulo = input("Ingrese el titulo a buscar: ")      
        for serie in self.catalogo.series:
            if titulo.lower() in serie.titulo.lower():
                print(serie)
        print("Fin de resultados")

    def filtrar_x_genero(self):
        genero = input("Ingrese el género a filtrar: ")
        for serie in self.catalogo.series:
            for g in serie.generos:
                if genero.lower() in g.lower():
                   print(serie)
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
                self.ver_series()
            elif opcion == "4":
                self.buscar_serie()
            elif opcion == "5":
                self.dejar_resena()
            elif opcion == "6":
                self.filtrar_x_genero()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
