"""
1. Python allows the create of multiple method with same name depending upon their behaviour
of accepting the number of arguments and data types

2. It helps increse Fexibilty , as it allows simplification of code


3.Python does not allows any traditional Overloading but it manages it to perform that by using default or variable length argument




"""
# ! Method Overloading in Polymerphrism

class Multiplication:
    def mul(self,x,y=1):
        return x*y
    
multiply=Multiplication()
print(multiply.mul(4))
print(multiply.mul(4,5))
#  print(multiply.mul(4,5,4))  # !Error Beacuse it have 3 argument
    


