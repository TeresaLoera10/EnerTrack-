import json
from pymongo import MongoClient

# Configurar conexión con MongoDB Atlas
client = MongoClient("mongodb+srv://tloera976:LOERALOERA13@cluster0.pkmny.mongodb.net/?retryWrites=true&w=majority")
db = client["ConsumoEneregtico_DB"]
collection = db["consumo_energetico"]

# Cargar archivo JSON
with open("C:/Users/Teresa Loera/Documents/Garza_Proyecto/CONSUMO_E.json", encoding="utf-8") as file:
    data = json.load(file)  # Cargar JSON

# Insertar los datos en MongoDB
if isinstance(data, list):  # Verifica si el JSON es una lista de documentos
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Datos insertados correctamente.")