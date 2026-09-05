# SerieMatch

> El fin del scroll infinito. Encontrá tu próxima serie favorita sin perder el tiempo.

## Sobre el proyecto

SerieMatch es una aplicación de consola diseñada para los fanáticos que pasan más tiempo buscando qué ver que disfrutando de una buena historia. Eliminamos la eterna pregunta de *"¿Qué miramos hoy?"* mediante un sistema de recomendaciones rápidas para que encuentres tu *match* ideal al instante.

## Funcionalidades Principales

*   **Mini test inteligente:** Un cuestionario rápido al ingresar para adaptar el algoritmo a tu estado de ánimo actual.
*   **¿Dónde verla?:** Integración de disponibilidad para indicarte exactamente en qué plataforma de streaming se encuentra la serie.
*   **Lista de Favoritos:** Guardá tus *matches* para no olvidarte qué mirar el fin de semana.
*   **Tráiler Oficial:** Acceso directo a los avances para ayudarte a tomar la decisión final.
*   **Ranking:** Top de las series mejor valoradas por la crítica.



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
    - Mateo Luquetti
    - Tomas Aybar

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `modelos/` | Clases del dominio (`Serie`, `Usuario`) |
| `estructuras/` | Estr. de datos implementadas (BST, AVL, Heap, Grafo) |
| `algoritmos/` | Búsquedas, BFS/DFS, caminos mínimos |
| `datos/` | Datasets de prueba (JSON) |
| `servicios/` | Lógica de negocio (recomendador) |
| `ui/` | Interfaz de terminal |
| `tests/` | Pruebas |
| `docs/` | Documentación del proyecto |

## Documentación
- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Conexión entre estructuras](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)

## Estado del proyecto
⏳ TP0