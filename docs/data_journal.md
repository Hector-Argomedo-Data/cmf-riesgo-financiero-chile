Markdown
# 📓 Data Journal (P.D.A.R.) - Proyecto CMF Risk

## [Fase 1: Preparación y Limpieza en Google Sheets / Excel]

### 1. Tratamiento de Inconsistencias y Simbología CMF
- **[P] Problema:** Las planillas originales de la CMF traían símbolos '---' para celdas vacías, comas decimales y encabezados combinados en 3 filas, lo que impedía la lectura automática de BigQuery.
- **[D] Decisión:** Limpiar manualmente el piloto y estandarizar la convención de datos a nivel de archivo fuente.
- **[A] Acción:** Reemplazo masivo de '---' por '0.00', aplanamiento de encabezados a single-row en `snake_case` y eliminación de comas de miles.
- **[R] Resultado:** 4 hojas por mes aisladas con datos 100% numéricos listos para asignación de tipo `FLOAT64`.

---

## [Fase 2: Automatización y Conversión con Python]

### 2. Conversión Masiva de Excel a CSV
- **[P] Problema:** Convertir a mano 48 archivos Excel a formato CSV UTF-8 consumiría demasiado tiempo y tenía riesgo de error humano.
- **[D] Decisión:** Crear un script automatizado en Python (Google Colab) con la librería `pandas`.
- **[A] Acción:** Ejecución del script de barrido de directorios y exportación limpia:
  ```python
  df.to_csv(ruta_salida, index=False, encoding='utf-8')
- **[R] Resultado: Reducción del tiempo de preparación de datos de horas manuales a solo 8 segundos. Generación de 48 archivos .csv con 100% de compatibilidad para BigQuery (UTF-8, snake_case, sin nulos/acentos y números enteros limpios).
