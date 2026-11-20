class Vehiculos:
    def __init__(self, plate, brand):
        self.brand = brand
        self.plate = plate
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def remove_reservation(self, reservation):
        self.reservations.remove(reservation)

    def start_engine(self):
        self.status = "Arrancado"
        print(
            f"Motor de {self.kind} {self.brand} con matrícula {self.plate} {self.status}."
        )

    def __str__(self):
        return f"{self.kind} - {self.brand} - ({self.plate})"


class Coche(Vehiculos):
    def __init__(self, plate, brand):
        super().__init__(plate, brand)
        self.kind = "Coche"
        self.status = "Apagado"

    def __str__(self):
        return f"{self.kind} - {self.brand} - ({self.plate})"


class Moto(Vehiculos):
    def __init__(self, plate, brand):
        super().__init__(plate, brand)
        self.kind = "Moto"
        self.status = "Apagado"

    def __str__(self):
        return f"{self.kind} - {self.brand} - ({self.plate})"
