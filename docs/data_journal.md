# 📓 Data Journal - Proyecto CMF Risk

## [Fase 1: Preparación y Estructuración en Google Sheets]

### 1. Tratamiento de Inconsistencias, Encabezados y Simbología CMF
- **[P] Problema:** Las planillas originales de la CMF traían símbolos `'---'` para celdas vacías, comas de miles y encabezados combinados en 3 filas con acentos y caracteres especiales, lo que impedía la lectura automática de BigQuery.
- **[D] Decisión:** Diseñar una plantilla base (*molde*) en Google Sheets, aplanar encabezados a una sola fila en formato `snake_case` (sin acentos ni `ñ`), reemplazar nulos y agregar la columna `fecha`.
- **[A] Acción:** Reemplazo masivo de `'---'` por `0`, aplanamiento estructural de encabezados e inyección del metadato temporal en los 48 reportes.
- **[R] Resultado:** 48 archivos aislados y estructurados con encabezados en `snake_case` nativos para SQL y datos preparados para tipado `FLOAT64`/`INT64`.

---

## [Fase 2: Pipeline de Automatización y Tratamiento de Precisión Numérica con Python]

### 1. Ingesta Masiva, Conversión a CSV y Redondeo de Precisión (Python & Pandas)
- **[P] Problema:** La conversión manual de 48 archivos a `.csv` generaba alto consumo de tiempo. Adicionalmente, las transformaciones de hoja de cálculo introdujeron decimales flotantes extensos no corregibles masivamente con formato visual.
- **[D] Decisión:** Construir un script automatizado en Python (Google Colab) utilizando `pandas` y `glob` (para barrido recursivo de carpetas) que convierta los archivos a `.csv` e imponga un redondeo entero a los valores numéricos.
- **[A] Acción:** Ejecución del pipeline de lectura recursiva de directorios, aplicación de `round(0)` en columnas flotantes y exportación en codificación `UTF-8`:

  ```python
      df.to_csv(ruta_salida, index=False, encoding='utf-8')
