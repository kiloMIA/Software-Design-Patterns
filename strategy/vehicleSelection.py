from vehicle import *

class vehicleSelection:
    
    def __init__(self, vehicle):
        self._vehicle = vehicle
    
    def fuelConsumption(self, speed):
        return self._vehicle.fuelConsumption(speed)
    
if __name__ == '__main__':

    bus = Bus()
    vehicle_selection = vehicleSelection(bus)
    print('You will travel: ', vehicle_selection.fuelConsumption(30),' km')

    car = Car()
    vehicle_selection = vehicleSelection(car)
    print('You will travel: ', vehicle_selection.fuelConsumption(60),' km')

    truck = Truck()
    vehicle_selection = vehicleSelection(truck)
    print('You will travel: ', vehicle_selection.fuelConsumption(90),' km')
