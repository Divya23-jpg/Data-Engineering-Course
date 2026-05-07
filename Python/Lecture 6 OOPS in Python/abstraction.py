"""

Abstraction:

hides underlying complexities while hihglighting what is required.
Implemented using abstract base classes with the abc



"""

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

