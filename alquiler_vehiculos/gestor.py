from datetime import date

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
        """
        Añade un objeto vehiculo al gestor
        """
        self.vehicles.append(vehicle)

    def find_vehicle(self, plate):
        """
        Funcion que usa el gestor y un numero de matricula para devolver el vehiculo que tiene dicha matricula
        """
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                return vehicle

    def reserve_vehicle(self, vehicle, reservation_date):
        """
        function that takes a vehicle from gestor and a date and adds the reservation to the vehicles reservations list atribute
        """
        if vehicle not in self.vehicles:
            logger.error(
                Fore.RED
                + "El vehiculo no se ha encontrado en la flota"
                + Style.RESET_ALL
            )
            return False
        if reservation_date < date.today():
            logger.error(
                Fore.RED
                + "La fecha de reserva no puede ser anterior a la fecha actual"
                + Style.RESET_ALL
            )
            return False
        if reservation_date in vehicle.reservations:
            logger.error(
                Fore.RED
                + f"El vehiculo {vehicle} está ocupado en la fecha {reservation_date}"
                + Style.RESET_ALL
            )
            return False
        else:
            vehicle.add_reservation(reservation_date)
            logger.info(
                Fore.GREEN
                + f"Reserva del vehiculo {vehicle} añadida correctamente para el día {reservation_date}."
                + Style.RESET_ALL
            )
            return True
