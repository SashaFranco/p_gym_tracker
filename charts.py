import matplotlib.pyplot as plt
from exercises.controller import load_data

def plot_weight_evolution():
    """
    Genera un gráfico de la evolución del peso corporal a lo largo del tiempo.
    """
    data = load_data()
    if "metrics" not in data or not data["metrics"]:
        print("No hay métricas disponibles para generar el gráfico.")
        return

    # Extraer datos de las métricas
    dates = [metric["date"] for metric in data["metrics"]]
    weights = [metric["weight"] for metric in data["metrics"]]

    # Crear el gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(dates, weights, marker='o', linestyle='-', color='b', label="Peso (kg)")
    plt.title("Evolución del Peso Corporal", fontsize=14)
    plt.xlabel("Fecha", fontsize=12)
    plt.ylabel("Peso (kg)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()


def plot_exercise_categories():
    """
    Genera un gráfico de barras para las categorías de ejercicios.
    """
    data = load_data()
    if "exercises" not in data or not data["exercises"]:
        print("No hay ejercicios disponibles para generar el gráfico.")
        return

    # Contar las categorías de ejercicios
    categories = {}
    for exercise in data["exercises"]:
        category = exercise["category"]
        categories[category] = categories.get(category, 0) + 1

    # Crear el gráfico
    plt.figure(figsize=(8, 5))
    plt.bar(categories.keys(), categories.values(), color='g')
    plt.title("Distribución por Categoría de Ejercicios", fontsize=14)
    plt.xlabel("Categorías", fontsize=12)
    plt.ylabel("Número de Ejercicios", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()


def plot_reps_vs_weight():
    """
    Genera un gráfico de dispersión para mostrar peso vs repeticiones.
    """
    data = load_data()
    if "exercises" not in data or not data["exercises"]:
        print("No hay ejercicios disponibles para generar el gráfico.")
        return

    # Extraer datos
    weights = [exercise["weight"] for exercise in data["exercises"]]
    reps = [exercise["reps"] for exercise in data["exercises"]]

    # Crear el gráfico
    plt.figure(figsize=(8, 5))
    plt.scatter(weights, reps, color='r', label="Ejercicios")
    plt.title("Relación entre Peso y Repeticiones", fontsize=14)
    plt.xlabel("Peso (kg)", fontsize=12)
    plt.ylabel("Repeticiones", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
