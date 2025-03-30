from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,brand,model,color):
       self.brand=brand
       self.model=model
       self.color=color
    @abstractmethod
    def start(self):
        raise NotImplementedError("This method is not implemented")
    def stop(self):
        raise NotImplementedError("This method is not implemented")
    def drive(self):
        raise NotImplementedError("This method is not implemented")
class Car(Vehicle):

    def start(self):
        print("The car is starting")
    def stop(self):
        print("The car is stopping")
    def drive(self):
        print("You are driving the car")
class Truck(Vehicle):


    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("You are driving the truck")
class Jeep(Vehicle):

    def start(self):
        print("The Jeep is starting")
    def drive(self):
        print("You are driving the Jeep")
vehicles =[Car("BMW","M5","Black"), Truck("Ford","F150","Red"), Jeep("Jeep","260LX","White")]
for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
    vehicle.drive()



