"""
Inheritance allows new classes to inherit properties and methods
from existing class to promote code use.

Types:
1 Single,
2 Multilevel
3 Multiple inheritance


"""



# ! 

class Transport:
    def start(self):
        print("Start Transport......")


class Car(Transport):
    def drive(self):
        print("Car is moving......")

my_car=Car()
my_car.start()  #Inheritance method from Transport class
my_car.drive()  # method from Car class



