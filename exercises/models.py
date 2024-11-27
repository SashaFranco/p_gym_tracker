class Exercise:
    def __init__(self, name, category, weight=0, sets=0, reps=0):
        """Inicializa un ejercicio.
        :param name: Nombre del ejercicio (str).
        :param category: Categoría del ejercicio (ejemplo: fuerza, cardio).
        :param weight: Peso utilizado (float).
        :param sets: Número de series (int).
        :param reps: Número de repeticiones por serie (int).
        """
        
        self.name = name
        self.category = category
        self.weight = weight
        self.sets = sets
        self.reps = reps
        
    def to_dict(self):
        """
        Convierte el objeto en un diccionario para almacenarlo en JSON.
        """
        
        return {
            "name": self.name,
            "category": self.category,
            "weight": self.weight,
            "sets": self.sets,
            "reps":self.reps
        }
        
    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Exercise a partir de un diccionario.
        """
        return cls(
            name=data["name"],
            category=data["category"],
            weight=data.get("weight", 0),
            sets=data.get("sets", 0),
            reps=data.get("reps", 0),
        )
            
        