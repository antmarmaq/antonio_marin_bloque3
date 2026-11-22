class Vehiculos:
    """
    Clase padre para todos los vehículos
    """

    def __init__(self, plate, brand, model):
        self.brand = brand
        self.plate = plate
        self.model = model
        self.reservations = []

    def add_reservation(self, reservation):
        """
        Añade una reserva a la lista de reservas del vehículo.
        """
        self.reservations.append(reservation)

    def remove_reservation(self, reservation):
        """
        Elimina una reserva de la lista de reservas del vehículo.
        """
        self.reservations.remove(reservation)

    def start_engine(self):
        """
        Arranca el motor del vehículo.
        """

        self._status = "Arrancado"
        print(
            f"Motor de {self.kind} {self.brand} con matrícula {self.plate} {self._status}."
        )

    def __str__(self):
        return f"{self.kind} {self.brand} {self.model} con matrícula ({self.plate})"


class Coche(Vehiculos):
    """
    Clase que representa a los coches
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Coche"
        self._status = "Apagado"


class Moto(Vehiculos):
    """
    Clase que representa a las motos
    """

    def __init__(self, plate, brand, model):
        super().__init__(plate, brand, model)
        self.kind = "Moto"
        self._status = "Apagado"
