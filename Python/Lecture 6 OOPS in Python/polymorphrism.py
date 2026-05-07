
"""

# ?Polymerphrism

This enables one interface to be used for diffrent data types and 
methods to behave diffferently based on the context

It al achivesd by Method Overriding and Method Overloading
"""


# Example
class Shape:
    def area(self):
        pass

    
class Square(Shape):
    def area(self):
        return "Area of Square"
    

class Circle(Shape):
    def area(self):
        return " Area of Circle"
    
shape=[Square(),Circle()]
for s in shape:
    print(s.area())