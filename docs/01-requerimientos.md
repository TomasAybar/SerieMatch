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