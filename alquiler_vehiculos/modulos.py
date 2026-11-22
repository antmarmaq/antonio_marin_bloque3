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
                print(Fore.YELLOW + "Lista de Coches registrados:" + Style.RESET_ALL)
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
                print(Fore.YELLOW + "Lista de Motos registradas:\n" + Style.RESET_ALL)
                for vehicle in gestor.vehicles:
                    if vehicle.kind == "Moto":
                        print(f"{i}. {vehicle}")
                        i += 1
                print()
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
                    (
                        Fore.RED
                        + logger.error("La matrícula introducida no es válida.")
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
                    (
                        Fore.RED
                        + logger.error("La matrícula introducida no es válida.")
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
    """
    Reservar un vehículo
    """
    cls()
    title()
    print(Fore.YELLOW + "Realizando nueva reserva." + Style.RESET_ALL)

    # Nos aseguramos de que haya vehiculos que reservar
    if not gestor.vehicles:
        logger.error(Fore.RED + "No hay vehiculos registrados." + Style.RESET_ALL)
        confirm()
        return

    search = input(
        Fore.YELLOW
        + "Introduzca la matrícula del vehiculo que desea reservar: "
        + Style.RESET_ALL
    ).upper()
    vehicle = gestor.find_vehicle(search)

    if vehicle is None:
        logger.error(
            Fore.RED
            + f"El vehiculo con matricula {search} no se ha encontrado"
            + Style.RESET_ALL
        )

    reservation = input_date()
    if gestor.reserve_vehicle(vehicle, reservation):
        save(gestor)
        print(Fore.GREEN + "Reserva realizada correctamente" + Style.RESET_ALL)
    else:
        logger.error(
            Fore.RED + "Ha habido un problema al realizar la reserva" + Style.RESET_ALL
        )

    confirm()


def option4():
    """
    Consultar lista de reservas
    """
    cls()
    title()
    print(Fore.YELLOW + "Consulta de reservas:\n" + Style.RESET_ALL)
    all_reservations = [
        (reservation, vehicle)
        for vehicle in gestor.vehicles
        for reservation in vehicle.reservations
    ]
    if not all_reservations:
        logger.info(
            Fore.RED
            + "No hay ninguna reserva registrada en el sistema\n"
            + Style.RESET_ALL
        )
        confirm()
    else:
        i = 1
        for reservation, vehicle in all_reservations:
            print(f"{i} {reservation}, {vehicle}")
            i += 1
        print()
        confirm()
        return
