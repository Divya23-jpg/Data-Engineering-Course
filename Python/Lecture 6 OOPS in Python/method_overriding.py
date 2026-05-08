
class DataEngineering:  #Parent class
    def course(self):
        return "Data Engeeniring Course"
    

class Python(DataEngineering):  # Child Class 
    def course(self):           # Method Overriding 
        return "Python Course"
    

class data(DataEngineering):  # Child Class
    def course(self):         # Method Overriding 
        return "Data Course"
    



