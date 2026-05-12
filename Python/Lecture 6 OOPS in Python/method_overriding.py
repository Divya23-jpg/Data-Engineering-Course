"""
In Method overriding inheritance concept is taken

Benifits:

1. It makes Simplified code as a single interface can handle multiple data type
2. Functions and methods of a class can be used for different purposes, which provide code reusability
3. It offers code flexibility as child classes can be use method of parent classes wihtout changin code
4. Multiple team can work on different parts of code without any conflict
5. It allows function to take various types of data input. The eleminates the need to separate functions for multiple data types like str,list,int etc

"""

# ! Method Overriding in Polymerphrism
# class DataEngineering:  #Parent class
#     def course(self):
#         return "Data Engeeniring Course"
    

# class Python(DataEngineering):  # Child Class 
#     def course(self):           # Method Overriding 
#         return "Python Course"
    

# class data(DataEngineering):  # Child Class
#     def course(self):         # Method Overriding 
#         return "Data Course"
    

# for i in [Python(),data()]:
#     print(i.course())


#! Polymerphrism in operators
# ? IN Integer
print("+ in Integers:",1+2)
# ? IN String
print("+ in String:","Divya"+"Kumawat")
