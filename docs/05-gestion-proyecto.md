# Gestión del Proyecto

## Metodología
Trabajamos de forma ágil e incremental: cada TP de la materia fue una iteración en la que se agregaba una estructura de datos, se integraba a la aplicación y se documentaba.

> **Cambio respecto al plan inicial:** al comienzo del proyecto (TP0) planificamos organizar las tareas en un tablero de Trello. En la práctica no lo usamos: la organización se hizo por Discord y el seguimiento del trabajo quedó registrado en Git y GitHub.

## Roles
- Todos los integrantes participan en el desarrollo y la documentación.
- Proponemos, editamos y corroboramos cada parte realizada por cada integrante.

## Herramientas
- **Discord**: comunicación del grupo, reparto de tareas y reuniones.
- **Git y GitHub**: control de versiones del código y la documentación, y seguimiento de lo que hizo cada integrante.

## Organización de tareas
- Las tareas se repartían y se acordaban por Discord, al inicio de cada TP.
- Cada cambio se registraba con un commit que indica el TP al que corresponde (por ejemplo, `TP6 agrego implementacion de ranking utilizando heap`).
- Las funcionalidades más grandes se desarrollaron en una rama propia y se incorporaron a `main` mediante un *pull request*, por ejemplo:
  - `heap` → ranking con heap (TP6, pull request #1).
  - `feat/favoritos` → lista de favoritos persistente (pull request #2).

## Seguimiento
Nos reunimos periódicamente por Discord para revisar el avance y ajustar las tareas. El historial de commits y los pull requests de GitHub funcionan como registro de qué se hizo, quién lo hizo y cuándo.
