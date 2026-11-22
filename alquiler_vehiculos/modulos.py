from colorama import *

from .display import cls, confirm, gestion_menu, title
from .gestor import *
from .logger import logger
from .operaciones import *
from .vehiculos import *

gestor = GestorSistema()


def option1():
    pass


def option2():
    """
    Añade un vehículo a la flota.
    """
    while True:
        cls()
        title()
        gestion_menu()
        action = input("Seleccione una opción (1,2 o 3): ")
        cls()
        title()
        if action == "1":
            while True:
                plate = input("Introduzca la matrícula del coche (formato: 0000AAA): ")
                if validate_plate(plate) is False:
                    logger.error(
                        Fore.RED
                        + "La matrícula introducida no es válida."
                        + Style.RESET_ALL
                    )
                    continue
                brand = input("Introduzca la marca del coche: ")
                model = input("Introduzca el modelo del coche: ")
                vehicle = Coche(plate, brand, model)
                gestor.add_vehicle(vehicle)
                logger.info(f"Vehículo {vehicle} añadido correctamente a la flota.")
                break
        if action == "2":
            while True:
                plate = input("Introduzca la matrícula de la moto (formato: 0000AAA): ")
                if validate_plate(plate) is False:
                    logger.error(
                        Fore.RED
                        + "La matrícula introducida no es válida."
                        + Style.RESET_ALL
                    )
                    continue
                brand = input("Introduzca la marca de la moto: ")
                model = input("Introduzca el modelo de la moto: ")
                vehicle = Moto(plate, brand, model)
                gestor.add_vehicle(vehicle)
                logger.info(f"Vehículo {vehicle} añadido correctamente a la flota.")
                break
            if action == "3":
                logger.info("Volviendo al menú principal...")
                break
            else:
                continue
        break
    confirm()


def option3():
    pass


def oprion4():
    pass
