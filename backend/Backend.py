from flask import Flask, jsonify, request
import pandas as pd
import json
import joblib
from flask_cors import CORS
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde el frontend

# Cargar dataset desde CSV o JSON
csv_file = "backend/CONSUMO_E.csv"
json_file = "CONSUMO_E.json"

def load_data():
    try:
        df = pd.read_csv(csv_file)
        df["Fecha"] = pd.to_datetime(df["Fecha"])  # Ajustar para la columna "Fecha"
        return df
    except Exception as e:
        print("Error cargando CSV:", e)
    
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            df["Fecha"] = pd.to_datetime(df["Fecha"])  # Ajustar para la columna "Fecha"
            return df
    except Exception as e:
        print("Error cargando JSON:", e)
    
    return pd.DataFrame()

df = load_data()

# Entrenar modelo de predicción
def train_model():
    if df.empty:
        return None
    
    df["timestamp"] = df["Fecha"].astype(int) / 10**9  # Convertir fecha a timestamp
    X = df[["timestamp"]]
    y = df["Consumo_kWh"]  # Ajustar a la columna "Consumo_kWh"
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "modelo_consumo.pkl")
    return model

# Cargar o entrenar modelo
try:
    model = joblib.load("modelo_consumo.pkl")
except:
    model = train_model()

@app.route("/api/consumption", methods=["GET"])
def get_consumption():
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/predict", methods=["POST"])
def predict_consumption():
    if model is None:
        return jsonify({"error": "Modelo no disponible"}), 500
    
    request_data = request.get_json()
    fecha_pred = pd.to_datetime(request_data.get("fecha"))
    timestamp_pred = int(fecha_pred.timestamp())
    
    prediction = model.predict([[timestamp_pred]])[0]
    return jsonify({"fecha": request_data.get("fecha"), "prediccion": prediction})

if __name__ == "__main__":
    app.run(debug=True)
