from alquiler_vehiculos.display import cls, menu, title

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
            pass

        if action == "2":
            pass

        if action == "3":
            pass

        if action == "4":
            break

        else:
            continue

except KeyboardInterrupt:
    print("\nCerrando el programa...")
