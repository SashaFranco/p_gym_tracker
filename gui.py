import tkinter as tk
from tkinter import messagebox
from exercises.controller import add_exercise, list_exercises, update_exercise, delete_exercise, load_data
from metrics.controller import add_metric, list_metrics, update_metric, delete_metric
from charts import plot_weight_evolution, plot_exercise_categories, plot_reps_vs_weight


def main_window():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gym Tracker")
    root.geometry("400x300")

    # Título principal
    title = tk.Label(root, text="Gym Tracker", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    # Botones del menú principal
    btn_exercises = tk.Button(root, text="Gestionar Ejercicios", width=25, command=exercises_menu)
    btn_exercises.pack(pady=5)

    btn_metrics = tk.Button(root, text="Gestionar Métricas", width=25, command=metrics_menu)
    btn_metrics.pack(pady=5)

    # Botón para mostrar gráficos
    btn_charts = tk.Button(root, text="Mostrar Gráficos", width=25, command=charts_menu)
    btn_charts.pack(pady=5)

    btn_exit = tk.Button(root, text="Salir", width=25, command=root.quit)
    btn_exit.pack(pady=20)

    # Iniciar la ventana principal
    root.mainloop()

def charts_menu():
    """
    Menú gráfico para seleccionar gráficos.
    """
    window_charts = tk.Toplevel()
    window_charts.title("Gráficos")

    tk.Button(window_charts, text="Evolución del Peso", command=plot_weight_evolution).pack(pady=5)
    tk.Button(window_charts, text="Categorías de Ejercicios", command=plot_exercise_categories).pack(pady=5)
    tk.Button(window_charts, text="Peso vs Repeticiones", command=plot_reps_vs_weight).pack(pady=5)
    tk.Button(window_charts, text="Cerrar", command=window_charts.destroy).pack(pady=20)

# Menú para gestionar ejercicios
def exercises_menu():
    """
    Menú gráfico para gestionar ejercicios.
    """
    data = load_data()
    
    def add_new_exercise():
        """
        Ventana para añadir un nuevo ejercicio.
        """
        def save_exercise():
            name = entry_name.get()
            category = entry_category.get()
            try:
                weight = float(entry_weight.get())
                sets = int(entry_sets.get())
                reps = int(entry_reps.get())
                add_exercise(name, category, weight, sets, reps)
                messagebox.showinfo("Éxito", "Ejercicio añadido correctamente.")
                window_add.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

        window_add = tk.Toplevel()
        window_add.title("Añadir Ejercicio")

        tk.Label(window_add, text="Nombre:").pack(pady=5)
        entry_name = tk.Entry(window_add)
        entry_name.pack()

        tk.Label(window_add, text="Categoría:").pack(pady=5)
        entry_category = tk.Entry(window_add)
        entry_category.pack()

        tk.Label(window_add, text="Peso (kg):").pack(pady=5)
        entry_weight = tk.Entry(window_add)
        entry_weight.pack()

        tk.Label(window_add, text="Series:").pack(pady=5)
        entry_sets = tk.Entry(window_add)
        entry_sets.pack()

        tk.Label(window_add, text="Repeticiones:").pack(pady=5)
        entry_reps = tk.Entry(window_add)
        entry_reps.pack()

        tk.Button(window_add, text="Guardar", command=save_exercise).pack(pady=10)

    def show_exercises():
        """
        Ventana para listar ejercicios.
        """
        if "exercises" not in data or not data["exercises"]:
            messagebox.showinfo("Ejercicios", "No hay ejercicios almacenados.")
            return

        window_list = tk.Toplevel()
        window_list.title("Lista de Ejercicios")
        text_area = tk.Text(window_list, wrap="word", font=("Arial", 12))
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        for idx, exercise in enumerate(data["exercises"], start=1):
            text_area.insert(
                "end",
                f"{idx}. {exercise['name']} - {exercise['category']}\n"
                f"   Peso: {exercise['weight']} kg, Series: {exercise['sets']}, Repeticiones: {exercise['reps']}\n\n"
            )
        text_area.config(state="disabled")

    # Crear ventana para el menú de ejercicios
    window_exercises = tk.Toplevel()
    window_exercises.title("Gestionar Ejercicios")

    tk.Button(window_exercises, text="Añadir Ejercicio", command=add_new_exercise).pack(pady=5)
    tk.Button(window_exercises, text="Listar Ejercicios", command=show_exercises).pack(pady=5)
    tk.Button(window_exercises, text="Cerrar", command=window_exercises.destroy).pack(pady=20)


# Menú para gestionar métricas
def metrics_menu():
    """
    Menú gráfico para gestionar métricas.
    """
    data = load_data()
    
    def add_new_metric():
        """
        Ventana para añadir una nueva métrica.
        """
        def save_metric():
            date = entry_date.get()
            try:
                weight = float(entry_weight.get())
                chest = float(entry_chest.get()) if entry_chest.get() else None
                waist = float(entry_waist.get()) if entry_waist.get() else None
                hips = float(entry_hips.get()) if entry_hips.get() else None
                add_metric(date, weight, chest, waist, hips)
                messagebox.showinfo("Éxito", "Métrica añadida correctamente.")
                window_add.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

        window_add = tk.Toplevel()
        window_add.title("Añadir Métrica")

        tk.Label(window_add, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        entry_date = tk.Entry(window_add)
        entry_date.pack()

        tk.Label(window_add, text="Peso (kg):").pack(pady=5)
        entry_weight = tk.Entry(window_add)
        entry_weight.pack()

        tk.Label(window_add, text="Pecho (cm, opcional):").pack(pady=5)
        entry_chest = tk.Entry(window_add)
        entry_chest.pack()

        tk.Label(window_add, text="Cintura (cm, opcional):").pack(pady=5)
        entry_waist = tk.Entry(window_add)
        entry_waist.pack()

        tk.Label(window_add, text="Caderas (cm, opcional):").pack(pady=5)
        entry_hips = tk.Entry(window_add)
        entry_hips.pack()

        tk.Button(window_add, text="Guardar", command=save_metric).pack(pady=10)

    def show_metrics():
        """
        Ventana para listar métricas.
        """
        if "metrics" not in data or not data["metrics"]:
            messagebox.showinfo("Métricas", "No hay métricas almacenadas.")
            return

        window_list = tk.Toplevel()
        window_list.title("Lista de Métricas")
        text_area = tk.Text(window_list, wrap="word", font=("Arial", 12))
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        for idx, metric in enumerate(data["metrics"], start=1):
            text_area.insert(
                "end",
                f"{idx}. Fecha: {metric['date']}\n"
                f"   Peso: {metric['weight']} kg, Pecho: {metric.get('chest', 'N/A')} cm\n"
                f"   Cintura: {metric.get('waist', 'N/A')} cm, Caderas: {metric.get('hips', 'N/A')} cm\n\n"
            )
        text_area.config(state="disabled")

    # Crear ventana para el menú de métricas
    window_metrics = tk.Toplevel()
    window_metrics.title("Gestionar Métricas")

    tk.Button(window_metrics, text="Añadir Métrica", command=add_new_metric).pack(pady=5)
    tk.Button(window_metrics, text="Listar Métricas", command=show_metrics).pack(pady=5)
    tk.Button(window_metrics, text="Cerrar", command=window_metrics.destroy).pack(pady=20)


if __name__ == "__main__":
    main_window()
