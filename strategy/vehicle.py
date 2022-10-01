from abc import ABC, abstractmethod
class Vehicle(ABC):
    def fuelConsumption(self,speed):
        pass
    

class Bus(Vehicle):
    def fuelConsumption(self,speed):
        fuelCapacity = 300
        consumptionRate = 0.25
        distance = (speed*consumptionRate)/fuelCapacity
        return distance
       
    
class Car(Vehicle):
    def fuelConsumption(self,speed):
        fuelCapacity = 150
        consumptionRate = 0.5
        distance = (speed*consumptionRate)/fuelCapacity
        return distance
       

class Truck(Vehicle):
    def fuelConsumption(self,speed):
        fuelCapacity = 250
        consumptionRate = 0.15
        distance = (speed*consumptionRate)/fuelCapacity
        return distance
        
        