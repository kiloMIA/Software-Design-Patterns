from vehicle import *

class vehicleSelection:
    
    def __init__(self, vehicle):
        self._vehicle = vehicle
    
    def fuelConsumption(self, speed):
        return self._vehicle.fuelConsumption(self,speed)
