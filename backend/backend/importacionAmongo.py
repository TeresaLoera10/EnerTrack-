from pymongo import MongoClient
import json

# Conectar con MongoDB Atlas
client = MongoClient("mongodb+srv://tloera976:LOERALOERA13@cluster0.pkmny.mongodb.net/")
db = client["ConsumoEnergeticoDB"]
collection = db["consumo_energetico"]

# Cargar el archivo JSON
with open("CONSUMO_E.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Insertar los datos en MongoDB
collection.insert_many(data)

print("✅ Datos importados con éxito en MongoDB Atlas.")

mongoimport("mongodb+srv://tloera976:LOERALOERA13@cluster.mongodb.net/mi_base_de_datos"collection consumo_energetico CONSUMO_E.json)