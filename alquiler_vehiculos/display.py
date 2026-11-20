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
    Imprime el menu de la aplicación
    """
    print(Fore.YELLOW + "\U00002554" + 28 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Gestion de Flota     \U00002795 " + "\U00002551")
    print("\U00002551" + " 2. Ver lista de tareas  \U0001f4cb " + "\U00002551")
    print("\U00002551" + " 3. Buscar tarea         \U0001f50d " + "\U00002551")
    print("\U00002551" + " 4. Salir del programa   \U0001f44b " + "\U00002551")
    print("\U0000255a" + 28 * "\U00002550" + "\U0000255d\n" + Style.RESET_ALL)


def menu_de_detalles():
    """
    Imprime el menu de detalles para añadir a la tarea
    """
    print(Fore.YELLOW + "\nElija una opción para añadir información a su tarea: ")
    print("\U00002554" + 28 * "\U00002550" + "\U00002557")
    print("\U00002551" + " 1. Descripción             " + "\U00002551")
    print("\U00002551" + " 2. Prioridad               " + "\U00002551")
    print("\U00002551" + " 3. Fecha límite            " + "\U00002551")
    print("\U00002551" + " 4. Etiquetas               " + "\U00002551")
    print("\U00002551" + " 5. Editar nombre           " + "\U00002551")
    print("\U00002551" + " 6. Terminar                " + "\U00002551")
    print("\U0000255a" + 28 * "\U00002550" + "\U0000255d" + Style.RESET_ALL)
