class Vehiculos:
    """
    Clase padre para todos los vehículos
    """

    def __init__(self, plate, brand, model):
        self.brand = brand
        self._plate = plate
        self.model = model
        self._reservations = []

    @property
    def plate(self):
        return self._plate

    @property
    def reservations(self):
        return tuple(self._reservations)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        value = value.strip()
        if not value:
            raise ValueError("El vehículo tiene que tener una marca")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        value = value.strip()
        if not value:
            raise ValueError("El vehículo debe tener un modelo")
        self._model = value

    def add_reservation(self, reservation):
        """
        Añade una reserva a la lista de reservas del vehículo.
        """
        self._reservations.append(reservation)

    def __str__(self):
        return f"{self.kind} {self.brand} {self.model} con matrícula ({self.plate})"


class Coche(Vehiculos):
    """
    Clase que representa a los coches
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Coche"


class Moto(Vehiculos):
    """
    Clase que representa a las motos
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Moto"
