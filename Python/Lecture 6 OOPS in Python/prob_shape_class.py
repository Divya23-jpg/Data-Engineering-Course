"""

WAR to creatre a class name Shape . Include methods to calculates 
area and perimeter of different shape like Sqaue , circle,Triangle using
Inheritance and polymerphrism
Implement subclasses for each shape and override the area and perimeter method accordingle

"""

import math

class Shape:
    def area(self):
       pass

    def perimeter(self):
       pass
     
    

class Square(Shape):
    def area(self,l):
        return f"Area of Square is {l*l}"
    
    def perimeter(self,l):
          return f"Perimeter of Square is {4*l}"
        
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return f" Area of Circle: {2 * math.pi * self.radius **2}"
    
    def perimeter(self):
         return f" Perimeter of Circle: { math.pi * self.radius * self.radius}"
          
 
    

s=Circle()
print(s.area(2))
print(s.perimeter(4))

