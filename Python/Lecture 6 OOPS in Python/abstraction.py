"""

Abstraction:
hides underlying complexities while hihglighting what is required.
Implemented using abstract base classes with the abc

"""

# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass


from abc import ABC , abstractmethod

class Banking(ABC):
    def database(self):
        print("Connected with database")
        
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def security(self):
        pass

class Mobile(Banking):
    def security(self):
        print("Biometric is imp")

    # display method os imp because we make it  @abstractmethod without it mobile can not work
    def display(self):
        print("Display Mobile")

m=Mobile()
m.database()