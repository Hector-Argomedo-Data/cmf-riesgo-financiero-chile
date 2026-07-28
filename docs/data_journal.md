Markdown
# 📓 Data Journal - Proyecto CMF Risk

## [Fase 1: Preparación y Limpieza en Google Sheets / Excel]

### 1. Tratamiento de Inconsistencias y Simbología CMF
- **[P] Problema:** Las planillas originales de la CMF traían símbolos '---' para celdas vacías, comas decimales y encabezados combinados en 3 filas, lo que impedía la lectura automática de BigQuery.
- **[D] Decisión:** Limpiar manualmente el piloto y estandarizar la convención de datos a nivel de archivo fuente.
- **[A] Acción:** Reemplazo masivo de '---' por '0.00', aplanamiento de encabezados a single-row en `snake_case` y eliminación de comas de miles.
- **[R] Resultado:** 4 hojas por mes aisladas con datos 100% numéricos listos para asignación de tipo `FLOAT64`.

---

[Fase 2: Pipeline de Automatización y Normalización con Python]

1. Pipeline de Ingesta, Normalización de Esquema y Precisión Numérica (Python & Pandas)

- [P] Problema: Convertir a mano los 48 reportes extraídos a CSV consumiría horas. Además, la presencia de caracteres especiales/acentos en los encabezados rompería el esquema en BigQuery, y la imprecisión de los tipos flotantes genera decimales excesivos en cifras financieras.
- [D] Decisión: Diseñar un script automatizado en Python (Google Colab) utilizando `pandas`, `glob` (para barrido recursivo de carpetas) y `unicodedata` para realizar la conversión, normalización de esquema y ajuste numérico en una sola ejecución masiva.
- [A] Acción: Implementación de un pipeline integral que lee la estructura de directorios, limpia nombres de columna a formato estricto `snake_case`, redondea flotantes a enteros (`INT64`) y exporta a formato `.csv` limpio:

  ```python
      df.to_csv(ruta_salida, index=False, encoding='utf-8')
