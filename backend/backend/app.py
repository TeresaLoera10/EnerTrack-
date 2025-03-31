from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# 🔹 Conectar a MongoDB Atlas (Usa tu URI de conexión)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://tloera976:LOERALOERA13@cluster0.pkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_URI)
db = client["consumo_energia"]  # Nombre de la base de datos
collection = db["mediciones"]  # Nombre de la colección

@app.route('/mi-endpoint', methods=['POST'])
def mi_funcion():
    # lógica de la ruta
    return 'Datos recibidos'


def recibir_medicion():
    """Recibe datos de consumo energético y los almacena en MongoDB."""
    data = request.json
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    
    collection.insert_one(data)  # Guardar en MongoDB
    return jsonify({"mensaje": "Datos recibidos y almacenados"}), 201

@app.route("/", methods=["GET"])
def home():
    return "API de Monitoreo Energético funcionando 🚀", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
