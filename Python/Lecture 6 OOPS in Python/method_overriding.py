"""
Benifits:

1. It makes Simplified code as a single interface can handle multiple data type
2. Functions and methods of a class can be used for different purposes, which provide code reusability
3.It offers code flexibility as child classes can be use method of parent classes
"""
class DataEngineering:  #Parent class
    def course(self):
        return "Data Engeeniring Course"
    

class Python(DataEngineering):  # Child Class 
    def course(self):           # Method Overriding 
        return "Python Course"
    

class data(DataEngineering):  # Child Class
    def course(self):         # Method Overriding 
        return "Data Course"
    

for i in [Python(),data()]:
    print(i.course())

