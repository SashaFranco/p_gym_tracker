import json
import os
from metrics.models import Metrics

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


def add_metric(date, weight, chest=None, waist=None, hips=None):
    """
    Añade nuevas métricas al archivo JSON.
    """
    # Cargar los datos existentes
    data = load_data()

    # Crear un nuevo objeto Metrics
    metric = Metrics(date, weight, chest, waist, hips)

    # Añadirlo a la lista de métricas
    if "metrics" not in data:
        data["metrics"] = []
    data["metrics"].append(metric.to_dict())

    # Guardar los datos actualizados
    save_data(data)
    print("Métricas añadidas correctamente.")



def list_metrics():
    """
    Muestra todas las métricas almacenadas en el archivo JSON.
    """
    data = load_data()
    if "metrics" not in data or not data["metrics"]:
        print("No hay métricas almacenadas.")
        return

    print("\nMétricas almacenadas:")
    for idx, metric in enumerate(data["metrics"], start=1):
        print(
            f"{idx}. Fecha: {metric['date']}, Peso: {metric['weight']} kg, "
            f"Pecho: {metric.get('chest', 'N/A')} cm, Cintura: {metric.get('waist', 'N/A')} cm, Caderas: {metric.get('hips', 'N/A')} cm"
        )

  
def update_metric(index, date=None, weight=None, chest=None, waist=None, hips=None):
    """
    Actualiza una métrica existente por índice.
    """
    data = load_data()
    if "metrics" not in data or index >= len(data["metrics"]):
        print("Índice inválido o no hay métricas.")
        return

    # Actualizar la métrica seleccionada
    metric = data["metrics"][index]
    if date:
        metric["date"] = date
    if weight is not None:
        metric["weight"] = weight
    if chest is not None:
        metric["chest"] = chest
    if waist is not None:
        metric["waist"] = waist
    if hips is not None:
        metric["hips"] = hips

    # Guardar los cambios
    save_data(data)
    print("Métrica actualizada correctamente.")

    
def delete_metric(index):
    """
    Elimina una métrica por índice.
    """
    data = load_data()
    if "metrics" not in data or index >= len(data["metrics"]):
        print("Índice inválido o no hay métricas.")
        return

    # Eliminar la métrica seleccionada
    deleted = data["metrics"].pop(index)
    save_data(data)
    print(f"Métrica del día '{deleted['date']}' eliminada correctamente.")


    



