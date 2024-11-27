import json
import os
from exercises.models import Exercise

#Ruta del archivo JSON
DATA_FILE = "data/data.json"

def load_data():
    """
    Carga los datos del archivo JSON.
    :return: Diccionario con los datos cargados.
    """
    if not os.path.exists(DATA_FILE):
        return {}  # Si el archivo no existe, devolvemos un diccionario vacío.
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """
    Guarda los datos en el archivo JSON.
    :param data: Diccionario con los datos a guardar.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_exercise(name, category, weight, sets, reps):
    """
    Añade un nuevo ejercicio al archivo JSON.
    """
    # Cargar datos existentes
    data = load_data()

    # Crear un nuevo ejercicio
    exercise = Exercise(name, category, weight, sets, reps)

    # Añadirlo a la lista de ejercicios
    if "exercises" not in data:
        data["exercises"] = []
    data["exercises"].append(exercise.to_dict())

    # Guardar datos en el archivo JSON
    save_data(data)
    print(f"Ejercicio '{name}' añadido correctamente.")
