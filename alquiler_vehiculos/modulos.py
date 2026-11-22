from colorama import *

from .display import cls, confirm, fleet_menu, gestion_menu, title
from .gestor import *
from .logger import logger
from .operaciones import *
from .persistencia import save
from .vehiculos import *

gestor = GestorSistema()


def option1():
    """
    Muestra los vehículos de la flota.
    """
    while True:
        if not gestor.vehicles:
            logger.info(Fore.RED + "No hay vehículos en la flota." + Style.RESET_ALL)
            confirm()
            break
        else:
            cls()
            title()
            fleet_menu()
            action = input("Seleccione una opción (1,2 o 3): ")
            if action == "1":
                cls()
                title()
                i = 1
                logger.info("Lista de Coches registrados:")
                for vehicle in gestor.vehicles:
                    if vehicle.kind == "Coche":
                        print(f"{i}. {vehicle}")
                        i += 1
                confirm()
                break
            if action == "2":
                cls()
                title()
                i = 1
                logger.info("Lista de Motos registradas:\n")
                for vehicle in gestor.vehicles:
                    if vehicle.kind == "Moto":
                        print(f"{i}. {vehicle}")
                        i += 1
                confirm()
                break
            if action == "3":
                input("Volviendo al menú principal\nPulse enter para continuar...")
                break
            else:
                continue


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
                plate = (
                    input(
                        Fore.YELLOW
                        + "Introduzca la matrícula del coche (formato: 0000AAA): "
                        + Style.RESET_ALL
                    )
                    .upper()
                    .replace(";", ",")
                )
                if validate_plate(plate) is False:
                    logger.error(
                        Fore.RED
                        + "La matrícula introducida no es válida."
                        + Style.RESET_ALL
                    )
                    continue
                brand = (
                    input(
                        Fore.YELLOW
                        + "Introduzca la marca del coche: "
                        + Style.RESET_ALL
                    )
                    .capitalize()
                    .replace(";", ",")
                )
                model = (
                    input(
                        Fore.YELLOW
                        + "Introduzca el modelo del coche: "
                        + Style.RESET_ALL
                    )
                    .capitalize()
                    .replace(";", ",")
                )
                vehicle = Coche(plate, brand, model)
                gestor.add_vehicle(vehicle)
                save(gestor)
                logger.info(
                    Fore.GREEN
                    + f"Vehículo {vehicle} añadido correctamente a la flota."
                    + Style.RESET_ALL
                )
                confirm()
                break
        if action == "2":
            while True:
                plate = (
                    input(
                        Fore.YELLOW
                        + "Introduzca la matrícula de la moto (formato: 0000AAA): "
                        + Style.RESET_ALL
                    )
                    .upper()
                    .replace(";", ",")
                )
                if validate_plate(plate) is False:
                    logger.error(
                        Fore.RED
                        + "La matrícula introducida no es válida."
                        + Style.RESET_ALL
                    )
                    continue
                brand = (
                    input(
                        Fore.YELLOW
                        + "Introduzca la marca de la moto: "
                        + Style.RESET_ALL
                    )
                    .capitalize()
                    .replace(";", ",")
                )
                model = (
                    input(
                        Fore.YELLOW
                        + "Introduzca el modelo de la moto: "
                        + Style.RESET_ALL
                    )
                    .capitalize()
                    .replace(";", ",")
                )
                vehicle = Moto(plate, brand, model)
                gestor.add_vehicle(vehicle)
                save(gestor)
                logger.info(
                    Fore.GREEN
                    + f"Vehículo {vehicle} añadido correctamente a la flota."
                    + Style.RESET_ALL
                )
                confirm()
                break
        if action == "3":
            input("Volviendo al menú principal\nPulse enter para continuar...")
            break
        else:
            continue
        break


def option3():
    pass


def option4():
    pass
