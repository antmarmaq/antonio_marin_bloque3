from datetime import date
from pathlib import Path

from .vehiculos import Coche, Moto

VEHICLES_FILE = Path(__file__).parent.parent / "vehiculos.txt"
RESERVATIONS_FILE = Path(__file__).parent.parent / "reservas.txt"


def save(gestor):
    with VEHICLES_FILE.open("w", encoding="utf-8") as f:
        for vehicle in gestor.vehicles:
            f.write(f"{vehicle.kind};{vehicle.plate};{vehicle.brand};{vehicle.model}\n")
    with RESERVATIONS_FILE.open("w", encoding="utf-8") as f:
        for vehicle in gestor.vehicles:
            for reservation in vehicle.reservations:
                f.write(f"{vehicle.plate};{reservation.isoformat()}\n")


def load(gestor):
    if VEHICLES_FILE.exists():
        for line in VEHICLES_FILE.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            kind, plate, brand, model = line.split(";")
            if kind == "Coche":
                gestor.add_vehicle(Coche(plate, brand, model))
            elif kind == "Moto":
                gestor.add_vehicle(Moto(plate, brand, model))
            else:
                raise ValueError

    if RESERVATIONS_FILE.exists():
        # Hacemos un diccionario que asocia matriculas con sus vehiculos
        plates_dict = {vehicle.plate: vehicle for vehicle in gestor.vehicles}
        for line in RESERVATIONS_FILE.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            plate, day = line.split(";")
            vehicle = plates_dict.get(plate)
            vehicle.add_reservation(date.fromisoformat(day))
