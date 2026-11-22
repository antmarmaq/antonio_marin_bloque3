from alquiler_vehiculos.display import cls, menu, title
from alquiler_vehiculos.modulos import *

"""
// 1. INICIALIZACIÓN
MIENTRAS Verdadero:
    MOSTRAR Titulo
    MOSTRAR Menu
    accion = PEDIR Seleccione el número de la operación a realizar: 

    // 2. Procesar la selección
    SI accion == "1":
        
"""

# Inicializamos creando la lista vacía de tareas.
tasks = []
try:
    while True:
        cls()
        title()
        menu()
        action = input("Seleccione el número de la operación a realizar: ")

        if action == "1":
            option1()

        if action == "2":
            option2()

        if action == "3":
            option3()

        if action == "4":
            option4()

        if action == "5":
            print("Cerrando el programa...")
            break
        else:
            continue

except KeyboardInterrupt:
    print("\nCerrando el programa...")
