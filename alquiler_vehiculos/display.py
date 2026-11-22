import os

from art import *
from colorama import *


def cls():
    """
    Limpia la pantalla
    """
    os.system("cls" if os.name == "nt" else "clear")


def confirm():
    input("Presione Enter para continuar...")


def title():
    """
    Imprime el título de la aplicación
    """
    print(
        Fore.BLUE,
        Style.BRIGHT + text2art("Alquiler de Vehiculos") + Style.RESET_ALL,
    )


def menu():
    """
    Imprime el menu de gestion de la aplicacion
    """
    print(Fore.YELLOW + "\U00002554" + 35 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Ver vehiculos de la flota.  \U0001f697 " + "\U00002551")
    print("\U00002551" + " 2. Añadir vehiculo a la flota. \U00002795 " + "\U00002551")
    print("\U00002551" + " 3. Reservar un vehiculo.       \U0001f4c5 " + "\U00002551")
    print("\U00002551" + " 4. Consultar reservas.         \U0001f50e " + "\U00002551")
    print("\U00002551" + " 5. Cerrar el programa.         \U0001f6aa " + "\U00002551")
    print("\U0000255a" + 35 * "\U00002550" + "\U0000255d\n" + Style.RESET_ALL)


def gestion_menu():
    """
    Imprime el menu de añadir vehículos
    """
    print(Fore.YELLOW + "\nBienvenido a la gestión de flota de vehículos.")
    print("\U00002554" + 28 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Añadir Coche            " + "\U00002551")
    print("\U00002551" + " 2. Añadir Moto             " + "\U00002551")
    print("\U00002551" + " 3. Volver al menú principal" + "\U00002551")
    print("\U0000255a" + 28 * "\U00002550" + "\U0000255d\n" + Style.RESET_ALL)


def fleet_menu():
    """
    Imprime el menu para ver los vehículos
    """
    print(Fore.YELLOW + "\nBienvenido a la gestión de flota de vehículos.")
    print("\U00002554" + 28 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Ver Coches              " + "\U00002551")
    print("\U00002551" + " 2. Ver Motos               " + "\U00002551")
    print("\U00002551" + " 3. Volver al menú principal" + "\U00002551")
    print("\U0000255a" + 28 * "\U00002550" + "\U0000255d\n" + Style.RESET_ALL)
