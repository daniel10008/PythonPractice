class Car:
    def __init__(self, brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    def start(self):
        print("The car is starting")
    def stop(self):
        print("The car is stopping")
    def drive(self):
        print("You are driving the car")
class Truck:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print("The truck is starting")

    def stop(self):
        print("The truck is stopping")

    def drive(self):
        print("You are driving the truck")
class Jeep:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    def start(self):
        print("The Jeep is starting")
    def drive(self):
        print("You are driving the Jeep")


vehicles =[Car("BMW","M5","Black"), Truck("Ford","F150","Red"), Jeep("Jeep","260LX","White")]
for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
    vehicle.drive()



