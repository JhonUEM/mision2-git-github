# Evidencias — Misión 2
**Equipo:** Jhon Mario Sepulveda Torres (trabajo individual)
**URL del repositorio:** https://github.com/JhonUEM/mision2-git-github

## Aportaciones individuales
| Persona | Rama | Commits relevantes | PR |
|---|---|---|---|
| JhonUEM | `feature/metricas` | `5c49bd3` Añade función calcular_accuracy · `92e4352` Muestra la accuracy en el predictor · `443c94a` Valida listas vacías (revisión) | [#1](https://github.com/JhonUEM/mision2-git-github/pull/1) |
| JhonUEM | `feature/tests` | `1ba97d6` Tests de accuracy total y parcial · `0811679` Test de listas vacías · `7100c82` Test de longitudes distintas (revisión) | [#2](https://github.com/JhonUEM/mision2-git-github/pull/2) |
| JhonUEM | `feature/documentacion` y `feature/titulo-readme` | `460143a` y `613f18c`: cambios del título usados para el conflicto controlado | Merge local |

## Revisiones de código
Trabajo individual: según la guía, la revisión se adapta y se realiza como **autorrevisión**, con comentarios en las líneas del código dentro de cada PR.
- **PR 1:** [#1](https://github.com/JhonUEM/mision2-git-github/pull/1) — Comentario: `calcular_accuracy` producía un `ZeroDivisionError` poco claro con listas vacías. Cambio aplicado en `443c94a`: se valida antes y se lanza `ValueError("Las listas no pueden estar vacías")`. Comprobado con `python -c` y los tests.
- **PR 2:** [#2](https://github.com/JhonUEM/mision2-git-github/pull/2) — Comentario: faltaba un test para listas de distinta longitud. Cambio aplicado en `7100c82`: nuevo `test_rechaza_longitudes_distintas`. Resultado: 6 tests OK.

## Conflicto de fusión
- **Archivo y línea afectados:** `README.md`, línea 1 (título).
- **Qué propuso cada rama:**
  - `feature/documentacion`: `# Proyecto IA — Clasificador de flores Iris`
  - `feature/titulo-readme`: `# Clasificador de flores con scikit-learn`
- **Cómo lo resolvimos:** se fusionó primero `feature/documentacion` (fast-forward). Al fusionar `feature/titulo-readme`, Git informó `CONFLICT (content): Merge conflict in README.md` y `git status` mostró `both modified: README.md`. Se editó el archivo con nano, se eliminaron las marcas `<<<<<<<`, `=======` y `>>>>>>>`, y se combinaron ambas propuestas: `# Proyecto IA — Clasificador de flores Iris con scikit-learn`. Se comprobó con `grep` que no quedaban marcas, se ejecutó `git add README.md` y se completó el merge con el commit `a5ef340`. Los 6 tests siguieron en OK.
- **Evidencia del historial (`git log --oneline --graph --all`):** ver el final de este documento.

## Verificación final
- **Comando para ejecutar el proyecto y resultado:** `python -m src.predictor` → `Predicción: 0 | Clase real: 0` y `Accuracy en test: 0.89`.
- **Comando para ejecutar tests y resultado:** `python -m unittest discover -s tests -v` → `Ran 6 tests ... OK`.
- **Reproducibilidad:** el repositorio se clonó en una carpeta nueva (`git clone`), se creó el entorno virtual, se instalaron las dependencias y el proyecto y los tests funcionaron igual.
- **Incidencia resuelta durante el trabajo:** al descomprimir el kit, las carpetas tenían permisos de solo lectura (`dr-xr-xr-x`), lo que impedía crear `.venv` y `.git`. Se corrigió con `chmod -R u+w`, dando solo el permiso de escritura necesario al propietario.
- **¿Qué mejoraríamos en el siguiente proyecto?:** crear las ramas de trabajo desde el principio con una convención de nombres acordada, añadir un flujo de GitHub Actions que ejecute los tests automáticamente en cada Pull Request, y contar con revisión por parte de otra persona para que la revisión de código sea independiente.

## Grafo de ramas
```
*   a5ef340 Resuelve conflicto en el título del README combinando ambas propuestas
|\  
| * 613f18c Cambia el título del README a Clasificador de flores con scikit-learn
* | 460143a Cambia el título del README a Clasificador de flores Iris
|/  
*   b200971 Merge pull request #2 from JhonUEM/feature/tests
|\  
| * 7100c82 Añade test de longitudes distintas en calcular_accuracy (revisión PR #2)
| * 0811679 Añade test para listas vacías en calcular_accuracy
| * 1ba97d6 Añade tests de calcular_accuracy con aciertos totales y parciales
|/  
*   fa845b9 Merge pull request #1 from JhonUEM/feature/metricas
|\  
| * 443c94a Valida listas vacías en calcular_accuracy (revisión PR #1)
| * 92e4352 Muestra la accuracy del modelo al ejecutar el predictor
| * 5c49bd3 Añade función calcular_accuracy en metricas.py
|/  
* 7a85a62 Añade requisitos y resultado esperado al README
* fff5a14 Versión inicial del clasificador de flores
```
