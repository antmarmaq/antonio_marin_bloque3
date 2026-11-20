from colorama import *

from .display import cls, confirm, menu_de_detalles, title
from .gestor import *
from .logger import logger


def new_task(tasks):
    cls()
    title()
    # Input de información de la tarea
    name = input("Introduzca el nombre de la tarea: ")
    details = {}
    while True:
        cls()
        title()
        print(Fore.GREEN + "Añadiendo tarea: " + Style.RESET_ALL + f"{name}")
        menu_de_detalles()
        opcion = input("Escriba el número del detalle que quiere añadir: ")
        if opcion == "1":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["descripcionion"] = input(
                Fore.YELLOW
                + "Escriba una breve descripción de su tares: "
                + Style.RESET_ALL
            )

        if opcion == "2":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            while True:
                try:
                    priority = int(
                        input(
                            Fore.YELLOW
                            + "Evalue la prioridad de su tare del 1 al 10: "
                            + Style.RESET_ALL
                        )
                    )
                    if priority not in range(11):
                        continue
                    else:
                        details["prioridad"] = priority
                        break
                except ValueError:
                    continue

        if opcion == "3":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["fecha limite"] = input_date()

        if opcion == "4":
            cls()
            title()
            print(Fore.GREEN + "Añadiendo tarea:" + Style.RESET_ALL + f"{name}")
            details["etiquetas"] = (
                input(
                    Fore.YELLOW
                    + "Escriba las etiquetas que le gustaría añadir a la tarea: "
                    + Style.RESET_ALL
                )
                .lower()
                .replace(",", " ")
                .split()
            )

        if opcion == "5":
            cls()
            title()
            name = input(
                Fore.YELLOW + "Escriba el nuevo nombre de la tarea: " + Style.RESET_ALL
            )

        if opcion == "6":
            cls()
            title()
            print(Fore.GREEN + f"Tarea {name} añadida correctamente" + Style.RESET_ALL)
            tasks.append(add_task(name, **details))
            confirm()
            break
    return tasks


def show_list(tasks):
    cls()
    title()
    if not tasks:
        print(Fore.RED + "No hay ninguna tarea en la lista" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + Style.BRIGHT + "Lista de tareas:\n" + Style.RESET_ALL)
        for task in tasks:
            print(f"- {task['nombre']}")
        print()
    confirm()


def search_task(tasks):
    cls()
    title()
    if not tasks:
        print(Fore.RED + "No hay ninguna tarea en la lista" + Style.RESET_ALL)
        confirm()
        return
    else:
        search = input("Escriba la tarea de la que quiere los detalles: ")
        results = []
        for task in tasks:
            if search.lower() in task["nombre"].lower():
                results.append(task)
        if results == []:
            print(
                Fore.RED
                + f"No se ha encontrado ninguna tarea con nombre: {search}"
                + Style.RESET_ALL
            )
            confirm()
        else:
            cls()
            title()
            print(
                Fore.YELLOW
                + Style.BRIGHT
                + f"Se han encontrado {len(results)} resultados para: {search}"
                + Style.RESET_ALL
            )
            index = 1
            for task in results:
                if search.lower() in task["nombre"].lower():
                    print(Fore.YELLOW + f"\nResultado {index}:")
                    index += 1
                    for key, value in task.items():
                        print(Fore.GREEN + f"{key}:" + Style.RESET_ALL + f" {value}")
            print(Style.RESET_ALL)
            confirm()
