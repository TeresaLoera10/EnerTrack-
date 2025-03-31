import requests
import random

def generar_datos():
    # Generar una medición simulada
    return {"medicion": random.uniform(100, 500)}

def enviar_medicion():
    url = 'http://127.0.0.1:5000/mi-endpoint'
    data = generar_datos()  # Llamada a la función generadora de datos
    response = requests.post(url, json=data)
    print(response.status_code, response.text)

# Iniciar simulador
if __name__ == "__main__":
    print("📡 Simulador de datos iniciado...")
    enviar_medicion()




"""
import json
from pymongo import MongoClient

# Configurar conexión con MongoDB Atlas
client = MongoClient("mongodb+srv://tloera976:LOERALOERA13@cluster0.pkmny.mongodb.net/")
db = client["ConsumoEnergeticoDB"]
collection = db["consumo_energetico"]       

# Cargar archivo JSON
with open("C:\Users\Teresa Loera\Documents\Garza_Proyecto\CONSUMO_E.json ", encoding="utf-8") as file:
    data = json.load(file)  # Cargar JSON

# Insertar los datos en MongoDB
if isinstance(data, list):  # Verifica si el JSON es una lista de documentos
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Datos insertados correctamente.")

"""





