
"""

# ?Polymerphrism

This enables one interface to be used for diffrent data types and 
methods to behave diffferently based on the context

It al achivesd by Method Overriding and Method Overloading

It allows developers to create more flexible code because, it makes object behaves similarly
even when they have separate implementation


Greek word: Poly + Morphism  = Multiple/Multi + froms
"""


# Example
class Shape:
    def area(self):
        self.s=int(input("Enter side:"))
        # self.b=int(input("Enter breadth:"))
    
# ! wrong output TRY
class Square(Shape):
    def area(self):
        self.s*self.s
        return f"Area of Square is {self.s}"
    

class Circle(Shape):
    def area(self):
        return " Area of Circle"
    
shape=[Shape(),Square(),Circle()]
for s in shape:
    print(s.area())