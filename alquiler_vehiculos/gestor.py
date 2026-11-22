from colorama import *

from .logger import logger
from .persistencia import load


class GestorSistema:
    """
    Clase que gestiona el sistema de alquiler de vehiculos
    """

    def __init__(self):
        self.vehicles = []
        # Cargamos los datos de persistencia.py
        load(self)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def reserve_vehicle(self, vehicle, date):
        if vehicle not in self.vehicles:
            logger.error("El vehiculo no se ha encontrado en la flota")
            return False
        if date < date.today():
            logger.error("La fecha de reserva no puede ser anterior a la fecha actual")
            return False
        if date in vehicle.reservations:
            logger.error(f"El vehiculo {vehicle} está ocupado en la fecha {date}")
            return False
        else:
            vehicle.add_reservation(date)
            logger.info(
                f"Reserva del vehiculo {vehicle} añadida correctamente para el día {date}."
            )
            return True
