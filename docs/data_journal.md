Markdown
# 📓 Data Journal - Proyecto CMF Risk

## [Fase 1: Preparación y Limpieza en Google Sheets / Excel]

### 1. Tratamiento de Inconsistencias y Simbología CMF
- **[P] Problema:** Las planillas originales de la CMF traían símbolos '---' para celdas vacías, comas decimales y encabezados combinados en 3 filas, lo que impedía la lectura automática de BigQuery.
- **[D] Decisión:** Limpiar manualmente el piloto y estandarizar la convención de datos a nivel de archivo fuente.
- **[A] Acción:** Reemplazo masivo de '---' por '0.00', aplanamiento de encabezados a single-row en `snake_case` y eliminación de comas de miles.
- **[R] Resultado:** 4 hojas por mes aisladas con datos 100% numéricos listos para asignación de tipo `FLOAT64`.

---

## [Fase 2: Automatización y Conversión con Python]

### 1. Conversión Masiva de Excel a CSV
- **[P] Problema:** Convertir a mano 48 archivos Excel a formato CSV UTF-8 consumiría demasiado tiempo y tenía riesgo de error humano.
- **[D] Decisión:** Crear un script automatizado en Python (Google Colab) con la librería `pandas`.
- **[A] Acción:** Ejecución del script de barrido de directorios y exportación limpia:
  ```python
  df.to_csv(ruta_salida, index=False, encoding='utf-8')
- **[R] Resultado: Reducción del tiempo de preparación de datos de horas manuales a solo 8 segundos. Generación de 48 archivos .csv con 100% de compatibilidad para BigQuery (UTF-8, snake_case, sin nulos/acentos y números enteros limpios).

### 2. Normalización Masiva de Archivos (Python & Pandas)
- **[P] Problema: Los 48 archivos Excel presentaban imprecisiones en tipos de datos flotantes (decimales excesivos producto del procesamiento), nombres de columnas inconsistentes con caracteres especiales/acentos que romperían la sintaxis SQL de BigQuery, y una estructura manual ineficiente.

- **[D] Decisión: Automatizar el data wrangling mediante un script de Python en Google Colab utilizando pandas, glob (búsqueda recursiva) y unicodedata para limpiar y estandarizar la totalidad de los archivos de forma masiva antes de la ingesta.

- **[A] Acción: Ejecución de pipeline con normalización de esquema snake_case, redondeo de floats a enteros y preservación de jerarquía de subcarpetas:
- **[R] Resultado: Reducción del tiempo de preparación de datos de horas manuales a solo 8 segundos. Generación de 48 archivos .csv con 100% de compatibilidad para BigQuery (UTF-8, snake_case, sin nulos/acentos y números enteros limpios).
  ```python
  df.columns = [limpiar_texto(col) for col in df.columns]
  for col in df.select_dtypes(include=["float64", "float32"]).columns:
    df[col] = df[col].round(0)
