
# ! Craete "Vehicle" class defines a common interface with "Start_engine" method.
# ! The "Car" and "Motorcycle" classes overrides this method to provide their Specific implementation.
# ! The "Initiate_engine" function accepts objects of different type and incokes the correct "start_engine" method



class Vehicle:
    def start_engine(self):
        return "Engine has started..."
    
class Car(Vehicle):
    def start_engine(self):
        return "Car has started..."
    
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle has started..."

def initiate_engine(vehicle_obj):
    print(vehicle_obj.start_engine())

vehicle=Vehicle()
car = Car()
motorcycle = Motorcycle()

initiate_engine(vehicle)
initiate_engine(car)         
initiate_engine(motorcycle)