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


def list_exercises():
    """
    Muestra todos los ejercicios almacenados en el archivo JSON.
    """
    data = load_data()
    if "exercises" not in data or not data["exercises"]:
        print("No hay ejercicios almacenados.")
        return
    
    for idx, exercise in enumerate(data["exercises"], start=1):
        print(f"{idx}. {exercise['name']} - {exercise['category']} (Peso: {exercise['weight']} kg, Series: {exercise['sets']}, Reps: {exercise['reps']})")
        
        
def update_exercise(index, name=None, category=None, weight=None, sets=None, reps=None):
    """
    Actualiza un ejercicio existente por índice.
    """
    data = load_data()
    if "exercises" not in data or index >= len(data["exercises"]):
        print("Índice inválido o no hay ejercicios.")
        return
    
    # Actualizar el ejercicio seleccionado
    exercise = data["exercises"][index]
    if name:
        exercise["name"] = name
    if category:
        exercise["category"] = category
    if weight is not None:
        exercise["weight"] = weight
    if sets is not None:
        exercise["sets"] = sets
    if reps is not None:
        exercise["reps"] = reps

    save_data(data)
    print(f"Ejercicio actualizado correctamente.")

    
def delete_exercise(index):
    """
    Elimina un ejercicio por índice.
    """
    data = load_data()
    if "exercises" not in data or index >= len(data["exercises"]):
        print("Índice inválido o no hay ejercicios.")
        return

    # Eliminar el ejercicio seleccionado
    deleted = data["exercises"].pop(index)
    save_data(data)
    print(f"Ejercicio '{deleted['name']}' eliminado correctamente.")

    



