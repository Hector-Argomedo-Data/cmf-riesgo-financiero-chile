Markdown
# 📓 Data Journal - Proyecto CMF Risk

## [Fase 1: Preparación y estructuración / Google Sheet]

### 1. Tratamiento de Inconsistencias y Simbología CMF
- **[P] Problema:** Las planillas originales de la CMF traían símbolos '---' para celdas vacías, comas decimales y encabezados combinados en 3 filas, lo que impedía la lectura automática de BigQuery.
- **[D] Decisión:** Limpiar manualmente el piloto y estandarizar la estructura a nivel de archivo fuente agregando columna fuente.
- **[A] Acción:** Reemplazo masivo de '---' por '0.00'.
- **[R] Resultado:** 4 hojas por mes aisladas con datos 100% numéricos listos para asignación de tipo `FLOAT64`.

---

[Fase 2: Pipeline de Automatización y Normalización con Python]

1. Pipeline de Ingesta, Normalización de Esquema y Precisión Numérica (Python & Pandas)

- [P] Problema: Convertir a mano los 48 reportes extraídos a CSV consumiría  tiempo ademas se eliminan decimales inecesarios para dejar numeros redondos para facilitar trabajos futuros.
- [D] Decisión: Diseñar un script automatizado en Python (Google Colab) utilizando `pandas`, `glob` (para barrido recursivo de carpetas) y `unicodedata` para realizar la conversión y ajuste numérico en una sola ejecución masiva.
- [A] Acción: Implementación de un pipeline integral que lee la estructura de directorios, redondea flotantes a enteros (`INT64`) y exporta a formato `.csv` limpio:

  ```python
      df.to_csv(ruta_salida, index=False, encoding='utf-8')
