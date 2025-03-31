""" 
import pandas as pd
from pymongo import MongoClient

# 📌 Cargar el archivo CSV
df = pd.read_csv("CONSUMO_E.csv")

# 📌 Convertir la columna de fecha a tipo datetime
df["FechaHora"] = pd.to_datetime(df["FechaHora"])

# 📌 Conectar con MongoDB Atlas
MONGO_URI = "mongodb+srv://tloera976:LOERALOERA13@cluster0.pkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  

# 📌 Seleccionar la base de datos y la colección
db = client["ConsumoEnergetico"]
collection = db["Lecturas"]

# 📌 Convertir el DataFrame en una lista de diccionarios e insertarlo en MongoDB
data = df.to_dict(orient="records")
collection.insert_many(data)

print("✅ Datos insertados correctamente en MongoDB")


"""


import pandas as pd

# Cargar el dataset
ruta_dataset = "CONSUMO_E.csv"  # Asegúrate de que la ruta sea correcta
df = pd.read_csv(ruta_dataset)

# Mostrar las primeras filas
print(df.head())

# Información general del dataset
print(df.info())

# Estadísticas básicas
print(df.describe())






""" 
import pandas as pd
import json

# Cargar el archivo CSV
df = pd.read_csv("CONSUMO_E.csv")

# Convertir a formato JSON
json_data = df.to_dict(orient="records")

# Guardar en un archivo JSON
with open("CONSUMO_E.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4)

print("✅ Archivo JSON generado con éxito.")

""" 

















