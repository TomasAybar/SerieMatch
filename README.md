# SerieMatch

> El fin del scroll infinito. Encontrá tu próxima serie favorita sin perder el tiempo.

## Sobre el proyecto

SerieMatch es una aplicación de consola diseñada para los fanáticos que pasan más tiempo buscando qué ver que disfrutando de una buena historia. Eliminamos la eterna pregunta de *"¿Qué miramos hoy?"* mediante un sistema de recomendaciones rápidas para que encuentres tu *match* ideal al instante.

## Funcionalidades Principales

Funcionalidades planteadas en la propuesta inicial y su estado en la versión final:

*   **Mini test inteligente:** Un cuestionario rápido al ingresar para adaptar el algoritmo a tu estado de ánimo actual. ❌ *No implementada.*
*   **¿Dónde verla?:** Integración de disponibilidad para indicarte exactamente en qué plataforma de streaming se encuentra la serie. 🟡 *Implementada en parte: cada serie muestra su plataforma, sin el link.*
*   **Lista de Favoritos:** Guardá tus *matches* para no olvidarte qué mirar el fin de semana. ✅ *Implementada: los favoritos se guardan en un archivo de texto.*
*   **Tráiler Oficial:** Acceso directo a los avances para ayudarte a tomar la decisión final. ❌ *No implementada.*
*   **Ranking:** Top de las series mejor valoradas por la crítica. ✅ *Implementada con un heap.*

Además, la versión final incluye búsqueda por título (árbol AVL), filtro por género, exploración por categorías (árbol general) y recomendación de series relacionadas por género (grafo). El detalle está en la [documentación final](docs/11-documentacion-final.md).


## Instalación y ejecución

#### Windows

```bash
# 1. Clonar el repositorio
git clone https://github.com/TomasAybar/SerieMatch.git

# 2. Entrar al directorio del proyecto
cd SerieMatch

# 3. Crear el entorno virtual
python -m venv venv

# 4. Activar el entorno virtual
.\venv\Scripts\activate

# 5. Instalar las dependencias
pip install -r requirements.txt

# 6. Ejecutar
python main.py
```
#### Linux / macOS

```bash
# 1. Clonar el repositorio
git clone https://github.com/TomasAybar/SerieMatch.git

# 2. Entrar al directorio del proyecto
cd SerieMatch

# 3. Crear el entorno virtual
python3 -m venv venv

# 4. Activar el entorno virtual
source venv/bin/activate

# 5. Instalar las dependencias
pip install -r requirements.txt

# 6. Ejecutar
python main.py
```


## Integrantes

- Violeta Curto
- ~~Mateo Luquetti~~ *(DNF)*
- Tomás Aybar

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `modelos/` | Clases del dominio (`Serie`, `Usuario`, `Catalogo`, `GestorFavoritos`) |
| `estructuras/` | Estructuras de datos implementadas (BST, AVL, árbol general, heap, grafo) |
| `algoritmos/` | Scripts de prueba de las estructuras y experimentos de medición de tiempos |
| `datos/` | Catálogo de series (JSON), generador de datasets de prueba y favoritos guardados |
| `ui/` | Interfaz de terminal |
| `utils/` | Funciones auxiliares (normalización de los datos del JSON) |
| `docs/` | Documentación del proyecto |

## Documentación
- **[Documentación final](docs/11-documentacion-final.md)**: propuesta vs. resultado, estructuras por TP, diagrama de clases y trabajo futuro.
- [Propuesta](docs/00-propuesta.md)
- [Requerimientos](docs/01-requerimientos.md)
- [Diagrama de clases (boceto TP0)](docs/03-diagrama-clases.md)
- [Conexión entre estructuras](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)
- [TP3: BST y comparación de búsquedas](docs/07-analisis-tp3.md)
- [TP4 y TP5: AVL y árbol general](docs/08-analisis-tp4-tp5.md)
- [TP6: heap y ranking](docs/09-tp6-heap.md)
- [TP7: grafo y series relacionadas](docs/10-tp7-grafos.md)

## Estado del proyecto
✅ **Versión final entregada** (TP0 a TP7 y lista de favoritos).

**En mejora continua:** el proyecto sigue abierto a nuevas funcionalidades y mejoras. Las próximas están listadas en la [documentación final](docs/11-documentacion-final.md#7-limitaciones-conocidas-y-trabajo-futuro), como el mini test, el tráiler y las opciones del menú que todavía no tienen lógica (registrar usuario, agregar serie y dejar reseña).