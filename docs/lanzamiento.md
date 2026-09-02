## Nombre del proyecto.
    SerieMatch

## Dominio elegido y por qué.

Utilizamos un juego de palabras, "Serie" como referencia clara a la tematica elegida y "Match" como termino universalmente asociado a encontrar la combinacion perfecta. Es corto y facil de pronunciar con un tono fresco y cercano para el publico.


## Problema que resuelve.
Eliminamos el scroll infinito y el tiempo que perdes cuando no sabes que ver, te recomendamos series que te van a encantar en base a tus series favoritas, la tipica pregunta de "Que miramos hoy" es cosa del pasado


## Usuario objetivo (una persona concreta, no "el usuario en general").
Fanaticos de ver series que pasa más tiempo buscando qué ver que viendo series y quiere recomendaciones según sus gustos para dejar de hacer scroll eternamente y encontrar de una vez su próxima serie favorita.

## Cinco funcionalidades iniciales.
- **Mini test:** cuestionario corto al ingresar para preparar el algoritmo de recomendaciones
- **Donde verla:** al ver los detalles de una serie, te dice en que plataformas esta disponible para verla!
- **Lista de favoritos:** lista las series que te recomendamos en favoritos para no olvidarte de verlas
- **Trailer oficial:** te proporcionamos el trailer al alcance de tu mano para terminar de decidir
- **Ranking:** Te listamos las series mejores valoradas 



## Un ejemplo de interacción.

    ==================================================
      🎥   BIENVENIDO A SERIEMATCH (CLI Edition)  🎥 
    ==================================================

    1 - Iniciar mini test
    2 - Ver series mejores puntuadas
    3 - Buscar series
    4 - Ver lista de favoritos
    0 - Salir

    > Seleccioná una opción: 1


    --------------------------------------------------
            📋 MINI TEST DE RECOMENDACIÓN
    --------------------------------------------------
    Respondé 3 preguntas para encontrar tu serie ideal:

    [1/3] ¿Cómo venís hoy?
    1. Cansado, quiero algo liviano
    2. Con ganas de engancharme / Trama compleja
    3. Sorprendeme
    > Opción: 1

    [2/3] ¿De cuánto tiempo disponés por capítulo?
    1. Corto (< 30 min)
    2. Estándar (45 - 60 min)
    > Opción: 1

    [3/3] ¿Algún género en particular?
    1. Comedia
    2. Animación
    3. Cualquiera
    > Opción: 1



    --------------------------------------------------
                📺 RECOMENDACIÓN #1
    --------------------------------------------------
    Título:       Ted Lasso
    Género:       Comedia / Deporte
    Duración:     30 min por episodio
    Puntuación:   ⭐ 8.8 / 10
    Plataforma:   Apple TV+
    Sinopsis:     Un eufórico entrenador de fútbol americano es contratado 
                para dirigir un equipo de fútbol profesional en Inglaterra.
    --------------------------------------------------
    [1] Hacer Match (Elegir) | [2] Siguiente serie | [0] Volver al menú
    > Opción: 2


    --------------------------------------------------
                📺 RECOMENDACIÓN #2
    --------------------------------------------------
    Título:       Abbott Elementary
    Género:       Comedia / Falso Documental
    Duración:     22 min por episodio
    Puntuación:   ⭐ 8.2 / 10
    Plataforma:   Disney+
    Sinopsis:     Un grupo de profesores dedicados intenta navegar el sistema 
                de enseñanza pública en una escuela con pocos recursos.
    --------------------------------------------------
    [1] Hacer Match (Elegir) | [2] Siguiente serie | [0] Volver al menú
    > Opción: 1



    ==================================================
            🎯 ¡IT'S A MATCH! / ¡LEVEL UP! 🎯
    ==================================================
    Elegiste: Abbott Elementary
    🍿 Disponible en: Disney+
    🔗 Link directo: https://www.disneyplus.com/browse/abbott-elementary

    [!] Serie guardada automáticamente en tu lista de Favoritos (Opción 4).

    Presioná ENTER para volver al menú principal...




## Requerimientos Funcionales (RF)

- RF01: El sistema debe presentar un cuestionario interactivo de 3 preguntas al iniciar.

- RF02: El sistema debe recomendar series basándose en las respuestas del cuestionario y el dataset cargado

- RF03: El sistema debe permitir al usuario guardar una serie específica en una lista de favoritos.

- RF04: El sistema debe detallar en cual o cuales plataformas de streaming se encuentra disponible la serie consultada.

- RF05: El sistema debe generar y mostrar un ranking con las series mejor puntuadas del dataset.

---

## Requerimientos no funcionales (RNF)

- RNF01: La lista de favoritos debe persistir localmente en un archivo, de modo que no se borre al cerrar la aplicación.

- RNF02: El filtrado de recomendaciones debe procesar el dataset y devolver una respuesta en menos de 2 segundos

---

## Alcance y fuera de alcance

- Fuera de alcance: No se implementará manejo de múltiples usuarios simultáneos. No se reproducirá el video del trailer directamente.