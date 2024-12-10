import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Directorio raíz del proyecto

def load_data(data_type):
    filename = os.path.join(BASE_DIR, "colaborative_task_system\\" "data",data_type )
    print(filename)
    """Carga los datos de usuarios desde el archivo JSON."""
    try:
        with open(filename, "r") as jusers:
            return json.load(jusers)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al cargar el archivo JSON.")
        return []

def save_update(data, prefix):
    filename = os.path.join(BASE_DIR, "colaborative_task_system\\" "data", prefix)
    try:
        with open(filename, "w") as data_file:
            json.dump(data, data_file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error al sobrescribir los datos")
