class Vehiculo:
    """
    Clase padre para todos los vehículos
    """

    def __init__(self, plate, brand, model):
        self.brand = brand
        self.__plate = plate
        self.model = model
        self.__reservations = []

    @property
    def plate(self):
        return self.__plate

    @property
    def reservations(self):
        return tuple(self.__reservations)

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        value = value.strip()
        if not value:
            raise ValueError("El vehículo tiene que tener una marca")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        value = value.strip()
        if not value:
            raise ValueError("El vehículo debe tener un modelo")
        self.__model = value

    def add_reservation(self, reservation):
        """
        Añade una reserva a la lista de reservas del vehículo.
        """
        self.__reservations.append(reservation)

    def __str__(self):
        return f"{self.kind} {self.brand} {self.model} con matrícula ({self.plate})"


class Coche(Vehiculo):
    """
    Clase que representa a los coches
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Coche"


class Moto(Vehiculo):
    """
    Clase que representa a las motos
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Moto"
