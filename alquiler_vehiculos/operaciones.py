from datetime import date

from colorama import *
from logger import logger


def validate_plate(plate):
    """
    Se asegura de que la matricula sea valida
    """
    return len(plate) == 7 and plate[:4].isdigit() and plate[3:].isalpha()


def input_date():
    """
    Muestra una serie de inputs para dia, mes y año y devuelve una fecha en formato string DD/MM/AAAA
    """
    while True:
        day = input(Fore.YELLOW + "Escriba el día (en formado dd): " + Style.RESET_ALL)
        month = input(
            Fore.YELLOW + "Escriba el mes (en formato mm): " + Style.RESET_ALL
        )
        year = input(
            Fore.YELLOW + "Escriba el año (en formato yyyy): " + Style.RESET_ALL
        )
        try:
            selected_date = date(day=int(day), month=int(month), year=int(year))
            if selected_date < date.today():
                raise ValueError(
                    "La fecha introducida no puede ser anterior a la fecha actual."
                )
        except ValueError:
            logger.error(
                "La fecha introducida no es valida, asegurese de introducirla en el formato adecuado."
            )
            continue
        else:
            break
    return f"{selected_date}"
