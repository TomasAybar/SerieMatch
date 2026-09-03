# SerieMatch — Propuesta (TP0)
Sistema de recomendación de series que permite buscar, filtrar y descubrir títulos a partir del estado de ánimo y preferencias del usuario.


## 1. Dominio elegido y justificación
**Dominio:** Series de televisión y plataformas de streaming.
**Por qué:** Utilizamos un juego de palabras, "Serie" como referencia a la temática y "Match" como término universal para encontrar la combinación perfecta. Elegimos este dominio principalmente porque es un tema que nos gusta mucho y ataca un problema cotidiano que nos pasa a todos los integrantes del grupo. Además, al ser un universo tan amplio y lleno de variables (géneros, duraciones, puntuaciones, plataformas, etc.), resulta ideal para explorar y aplicar todos los temas y estructuras de datos que veremos a lo largo de la cursada.


## 2. Problema que resuelve
El scroll infinito y la frustración de perder tiempo buscando sin saber qué ver, erradicando para siempre la típica pregunta de "¿Qué miramos hoy?".


## 3. Usuario objetivo
Fanáticos de las series que pasan más tiempo buscando qué ver que consumiendo el contenido, y necesitan recomendaciones directas para dejar de hacer scroll eternamente.


## 4. Funcionalidades iniciales
| ID | Funcionalidad |
|---|---|
| F1 | Realizar un mini test interactivo para preparar el algoritmo |
| F2 | Indicar en qué plataforma de streaming se puede ver la serie |
| F3 | Guardar recomendaciones en una lista de favoritos |
| F4 | Proveer el enlace al tráiler oficial |
| F5 | Listar el ranking de las series mejor valoradas |


## 5. Ejemplo de uso (input/output)
```text
==================================================
        🎥   BIENVENIDO A SERIEMATCH   🎥 
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
> Opción: 1

==================================================
            🎯 ¡IT'S A MATCH! / ¡LEVEL UP! 🎯
==================================================
Elegiste: Ted Lasso
🍿 Disponible en: Apple TV+
🔗 Link directo: https://tv.apple.com/us/show/ted-lasso/

[!] Serie guardada automáticamente en tu lista de Favoritos (Opción 4).

Presioná ENTER para volver al menú principal...
```


## 6. Requerimientos (borrador)
> Los requerimientos formales (RF / RNF) se completan con más detalle en este
> mismo archivo a lo largo del TP.

|   ID  |                                  Requerimiento                                                    |       Tipo        |
|---|---|-------------------|
|  RF01 | El sistema debe presentar un cuestionario interactivo de 3 preguntas al iniciar                   |     Funcional     |
|  RF02 | El sistema debe recomendar series basándose en las respuestas del cuestionario y el dataset       |     Funcional     |
|  RF03 | El sistema debe permitir al usuario guardar una serie específica en una lista de favoritos        |     Funcional     |
|  RF04 | El sistema debe detallar en qué plataforma de streaming se encuentra disponible la serie          |     Funcional     |
|  RF04 | El sistema debe generar y mostrar un ranking con las series mejor puntuadas del dataset           |     Funcional     |
| RNF01 | El sistema debe estar desarrollado íntegramente en Python                                         |   No funcional    |
| RNF02 | La lista de favoritos debe persistir localmente en un archivo (para no perderse al salir)         |   No funcional    |
| RNF03 | El filtrado de recomendaciones debe procesar el dataset y responder en menos de 2 segundos        |   No funcional    |


## 7. Fuera de alcance (por ahora)
- No hay autenticación de usuarios ni registro con contraseñas.
- No se implementa interfaz gráfica, solo por terminal.
- No se reproduce video nativamente dentro de la consola; los tráilers se ofrecerán mediante enlaces web.