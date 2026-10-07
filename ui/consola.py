class ConsolaUI:
    def __init__(self, catalogo, avl, arbol_categorias):
        self.catalogo = catalogo
        self.avl = avl
        self.arbol_categorias = arbol_categorias

    def registrar_usuario(self):
        print("Registrar usuario")

    def agregar_serie(self):
        print("Agregar serie")

    def busqueda_AVL(self):
        titulo = input("Ingrese el titulo a buscar: ")
        resultado = self.avl.buscar(titulo.lower(), clave=lambda s: s.titulo.lower())
        if resultado:
            print(resultado)
        else:
            print("No se encontró")
        print("Fin de resultados")

    def explorar_categorias(self):
        arbol = self.arbol_categorias

        print("\n=== Explorar categorías ===")
        print(f"Total de géneros: {len(arbol.raiz.hijos)}")
        print()

        generos = [nodo.dato for nodo in arbol.raiz.hijos]
        for i, genero in enumerate(generos, 1):
            print(f"  {i}. {genero}")

        print("\nIngrese el número del género (o 0 para volver): ", end="")
        opcion = input()

        if opcion == "0":
            return

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(generos):
            print("Opción inválida")
            return

        genero_elegido = generos[int(opcion) - 1]
        nodo_genero = arbol.buscar(genero_elegido)

        print(f"\n--- Series de {genero_elegido} ---")
        for nodo_serie in nodo_genero.hijos:
            print(f"  · {nodo_serie.dato}")

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
            print("7. Explorar categorías")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.agregar_serie()
            elif opcion == "3":
                self.catalogo.listar_series()
            elif opcion == "4":
                self.busqueda_AVL()
            elif opcion == "5":
                self.dejar_resena()
            elif opcion == "6":
                self.catalogo.filtrar_serie_genero()
            elif opcion == "7":
                self.explorar_categorias()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
