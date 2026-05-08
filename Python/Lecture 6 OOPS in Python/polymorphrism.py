
"""

# ?Polymerphrism

This enables one interface to be used for diffrent data types and 
methods to behave diffferently based on the context

It al achivesd by Method Overriding and Method Overloading

It allows developers to create more flexible code because, it makes object behaves similarly
even when they have separate implementation

Greek word: Poly + Morphism  = Multiple/Multi + froms

Many forms of objects or functions depending on their usage and working.

Functionality:

1. The main role of Polymerphism in OOP is to ensure that different type of objects use the same methods or operators

Types of polymerphrism:
1.Compile time: Functional Overloading and Operator Overloading
2. Run time : Virtual Ex: Random functions(shape and course)


"""


#1. Example
# class Shape:
#     def area(self):
#         self.s=int(input("Enter side:"))
#         # self.b=int(input("Enter breadth:"))
    
# # ! wrong output TRY
# class Square(Shape):
#     def area(self):
#         self.s*self.s
#         return f"Area of Square is {self.s}"
    

# class Circle(Shape):
#     def area(self):
#         return " Area of Circle"
    
# shape=[Shape(),Square(),Circle()]
# for s in shape:
#     print(s.area())



# print(len("Divya"))
# print(len([1,2,3]))
# print(len((1,2,3,3)))


# ! WAP for polymerphrism for multiple Animal like Dog,Cat etc which produce sounds like Dog "Woof" or "Meaow"



class Animal:
    def speak(self):
        return "Sounding......"
    
class Dog(Animal):
    def speak(self):
        return "Dog Sounds:Woof"

class Cat(Animal):
    def speak(self):
        return "Cat sounds:Meowwww"
    
for i in [Animal() ,Dog(),Cat()]:
    print(i.speak())

    