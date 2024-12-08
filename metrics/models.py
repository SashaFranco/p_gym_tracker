class Metrics:
    def __init__(self, date, weight, chest=None, waist=None, hips=None):
        """
        Inicializa las métricas corporales.
        :param date: Fecha (str o datetime).
        :param weight: Peso corporal (float).
        :param chest: Medida del pecho (float).
        :param waist: Medida de la cintura (float).
        :param hips: Medida de las caderas (float).
        """
        self.date = date
        self.weight = weight
        self.chest = chest
        self.waist = waist
        self.hips = hips

    def to_dict(self):
        return {
            "date": self.date,
            "weight": self.weight,
            "chest": self.chest,
            "waist": self.waist,
            "hips": self.hips
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            date=data["date"],
            weight=data["weight"],
            chest=data.get("chest"),
            waist=data.get("waist"),
            hips=data.get("hips")
        )
