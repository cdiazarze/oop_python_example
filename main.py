from vehicle import Vehicle
from plane import Plane
from car import Car
from gasoline_sensor import GasolineSensor
from temperature_sensor import TemperatureSensor

def main():
    vehicles = [
        Plane('CDA-100', '787', 70, 100),
        Plane('AH-100', '474', 150, 50),
        Car('Renault Latitud', 45, 5)
    ]
    sensors = []
    for vehicle in vehicles:
        print(
            f'{vehicle}:\t'
            f'Capacity: {vehicle.passengers}'
        )
        sensors.append(GasolineSensor(vehicle))
        sensors[-1].check_level()
        vehicle.move()
        sensors[-1].check_level()
        sensors.append(TemperatureSensor(vehicle))
        sensors[-1].check_level()
    
    vehicles[2].temperature_level = 150
    sensors[-1].check_level()


if __name__ == "__main__":
    main()