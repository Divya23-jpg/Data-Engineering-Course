"""

WAR to creatre a class name Shape . Include methods to calculates 
area and perimeter of different shape like Sqaue , circle,Triangle using
Inheritance and polymerphrism
Implement subclasses for each shape and override the area and perimeter method accordingle

"""

class Shape:
    def area(self):
        self.s=int(input("Enter side:"))
     
    

class Square(Shape):
    def area(self):
        return f"Area of Square is { self.s*4}"
    

class Circle(Shape):
    def area(self):
        return " Area of Circle"
    

s=Square()
s.area()

