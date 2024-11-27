from exercises.controller import add_exercise, load_data
from exercises.models import Exercise 

# # Agregar un nuevo ejercicio
# add_exercise("Sentadilla", "Fuerza", 50, 3, 10)

# # Mostrar los datos almacenados
data = load_data()
# print("Datos actuales en el archivo JSON:")
# print(data)

ejercicio_data = data["exercises"][0]  # Acceder al primer ejercicio
ejercicio = Exercise.from_dict(ejercicio_data)
print(ejercicio.name)  # "Sentadilla"
