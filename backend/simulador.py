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
