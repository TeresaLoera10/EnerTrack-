from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

app = Flask(__name__)

# Ruta para cargar el modelo (puedes hacerlo solo una vez al iniciar)
model = None

def load_model():
    global model
    with open('model/model.pkl', 'rb') as file:
        model = pickle.load(file)

# Ruta para realizar una predicción
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de la solicitud
        data = request.get_json()
        # Aquí podrías procesar el JSON y convertirlo en un DataFrame o similar
        input_data = pd.DataFrame(data)
        
        # Usar el modelo para predecir el consumo energético
        if model:
            prediction = model.predict(input_data)
            return jsonify({'predicted_consumo': prediction.tolist()})
        else:
            return jsonify({'error': 'Modelo no cargado'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta de ejemplo para probar
@app.route('/')
def home():
    return "API de Predicción de Consumo Energético"

if __name__ == '__main__':
    load_model()  # Cargar el modelo al inicio
    app.run(debug=True)
