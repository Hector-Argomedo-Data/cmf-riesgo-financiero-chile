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


# 2. Función para normalizar encabezados a snake_case sin acentos ni 'ñ'
def limpiar_texto(texto):
  if not isinstance(texto, str):
    return texto
  nfkd = unicodedata.normalize("NFKD", texto)
  sin_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
  limpio = sin_acento.replace("ñ", "n").replace("Ñ", "N").lower()
  limpio = re.sub(r"[^a-z0-9_]", "_", limpio)  # Solo letras, números y '_'
  limpio = re.sub(r"_+", "_", limpio)  # Evitar guiones bajos dobles
  return limpio.strip("_")


print(f"🚀 Procesado de {len(archivos)} archivos...\n")

for ruta_archivo in archivos:
  # Mantener la estructura de subcarpetas al guardar
  ruta_relativa = os.path.relpath(ruta_archivo, carpeta_origen)
  ruta_salida = os.path.join(carpeta_destino, ruta_relativa)

  # Crear la subcarpeta de destino si no existe
  os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

  # Cargar el CSV
  df = pd.read_csv(ruta_archivo)

  # A) Limpiar nombres de columnas (snake_case sin acentos)
  df.columns = [limpiar_texto(col) for col in df.columns]

  # B) Limpiar datos: Redondear columnas numéricas (floats) a enteros
  for col in df.select_dtypes(include=["float64", "float32"]).columns:
    df[col] = df[col].round(0)  # Redondea a 0 decimales

  # C) Guardar el nuevo CSV limpio en Drive
  df.to_csv(ruta_salida, index=False, encoding="utf-8")

  print(f"✅ Procesado: {ruta_relativa}")

print(
    "\n🎉 Proceso finalizado
)
