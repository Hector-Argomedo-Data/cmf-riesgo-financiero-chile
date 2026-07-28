import glob
import os
import re
import unicodedata
import pandas as pd

Rutas en Google Drive
carpeta_origen = "/content/drive/MyDrive/Caso de estudio 1 Morosidad bancos/CSV"
carpeta_destino = (
    "/content/drive/MyDrive/Caso de estudio 1 Morosidad bancos/CSV_limpios"
)

os.makedirs(carpeta_destino, exist_ok=True)

# Buscar recursivamente en TODAS las subcarpetas de CSV
archivos = glob.glob(os.path.join(carpeta_origen, "**/*.csv"), recursive=True)


for ruta_archivo in archivos:
  # Mantener la estructura de subcarpetas al guardar
  ruta_relativa = os.path.relpath(ruta_archivo, carpeta_origen)
  ruta_salida = os.path.join(carpeta_destino, ruta_relativa)

  # Crear la subcarpeta de destino si no existe
  os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

  # Cargar el CSV
  df = pd.read_csv(ruta_archivo)

  # A) Limpiar datos: Redondear columnas numéricas (floats) a enteros
  for col in df.select_dtypes(include=["float64", "float32"]).columns:
    df[col] = df[col].round(0)  # Redondea a 0 decimales

  # B) Guardar el nuevo CSV limpio en Drive
  df.to_csv(ruta_salida, index=False, encoding="utf-8")

  print(f"✅ Procesado: {ruta_relativa}")

print(
    "\n🎉 Proceso finalizado
)
