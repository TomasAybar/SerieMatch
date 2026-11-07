class ConsolaUI:
    def __init__(self, catalogo, avl, arbol_categorias, heap_ranking, grafo):
        self.catalogo = catalogo
        self.avl = avl
        self.arbol_categorias = arbol_categorias
        self.heap_ranking = heap_ranking
        self.grafo = grafo

    def ver_ranking(self):
        entrada = input("¿Cuántas series quiere ver en el ranking? [5]: ").strip()
        if entrada == "":
            n = 5
        elif entrada.isdigit() and int(entrada) > 0:
            n = int(entrada)
        else:
            print("Cantidad inválida")
            return

        # Top-N: se extrae el máximo n veces y luego se reinsertan para no perderlos
        ranking = []
        for _ in range(min(n, len(self.heap_ranking.heap))):
            ranking.append(self.heap_ranking.extract_max())
        for serie in ranking:
            self.heap_ranking.insert(serie)

        print(f"\n=== TOP {len(ranking)} SERIES POR PUNTUACIÓN ===")
        medallas = {1: "🥇", 2: "🥈", 3: "🥉"}
        for posicion, serie in enumerate(ranking, 1):
            marca = medallas.get(posicion, f"{posicion}.")
            print(f"{marca} {serie.titulo:<35} {serie.puntuacion:.1f}")

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

    def buscar_series_relacionadas(self):
        titulo = input("Ingrese el titulo de una serie: ")
        relacionadas = self.grafo.obtener_vecinos(titulo)

        if relacionadas:
            print("\n=== SERIES RELACIONADAS POR GÉNERO ===")

            relacionadas_ordenadas = sorted(
                relacionadas,
                key=lambda serie: (
                    -len(self.grafo.obtener_generos_compartidos(titulo, serie)),
                    serie.lower()
                )
            )

            for serie in relacionadas_ordenadas:
                generos = self.grafo.obtener_generos_compartidos(titulo, serie)
                generos_formateados = ", ".join(generos)
                print(f"- {serie} | Géneros compartidos: {generos_formateados}")
        else:
            print("No se encontraron series relacionadas.")

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
            print("4. Buscar serie por titulo")
            print("5. Dejar reseña")
            print("6. Filtrar por género")
            print("7. Explorar categorías")
            print("8. Ranking de series")
            print("9. Buscar series relacionadas por género")
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
            elif opcion == "8":
                self.ver_ranking()
            elif opcion == "9":
                self.buscar_series_relacionadas()
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")
