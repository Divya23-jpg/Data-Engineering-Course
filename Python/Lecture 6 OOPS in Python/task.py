"""

WAP to create a Temperature class that stores a temperature in celcius .

Add two methods: Celcius to Fahrenheit() , celcius to kelwin() which return the calue of temperature in Fehrenheit and kelvin

Constraints:
Input : t=Temperature(100)
output: Celcius:100
        Fahrenmheit:212.0
        Kelvin: 373.15  



"""


# class Temperature:
#     def __init__(self):
#         self.t=float(input("Enter Temperature in Celcius:"))
    
#     # Kelvin
#     def kelvin(self):
#         return self.t+273.15
       
    
#      # Fahrenheit
#     def fahrenheit(self):
#         return self.t*(1.8)+32
    

# if __name__ == "__main__":
#     temp=Temperature()
#     print(f"Celcius :{temp.t}")
#     print(f"Kelvin: {temp.kelvin()}")
#     print(f"Fahrenheit: {temp.fahrenheit()}")
   
    



"""
1. Create a Class and Object
Create a Student class with attributes:
name
age
Create an object and print the details.

"""

# class student:
#     def stu(self):
#         self.name=input("Enter Name:")
#         self.age=int(input("Enter Age:"))

# stu_detail=student()
# stu_detail.stu()
# print(f"Name of student is: {stu_detail.name}")
# print(f"Name of student is: {stu_detail.age}")

"""
2. Method in Class
Create a Calculator class with a method add(a, b),
multiply, divide, subtract that returns the operation of two numbers.

"""
# class Calculator:
#     def take_input(self):
#         self.num1=int(input("Enter 1st Number::"))
#         self.num2=int(input("Enter 2nd Number::"))


#     def addition(self):
#         return f"Addition is:{self.num1+self.num2}"
    
#     def subtraction(self):
#         return f"Subtraction is:{self.num1-self.num2}"
    
#     def multiplication(self):
#         return f"Multiplication is:{self.num1*self.num2}"
    
#     def division(self):
#         return f"Division is:{self.num1/self.num2}"
    

# operation=Calculator()
# operation.take_input()
# print(operation.addition())
# print(operation.subtraction())
# print(operation.multiplication())
# print(operation.division())

    
"""
3. Inheritance Problem
Create:
Parent class → Animal
Child class → Dog
Add a method sound() in both classes and call the child class method.
"""
# class Animal:
#     def sound(self):
#         return "Sound of Animal..."
# class Dog(Animal):
#     def sound(self):
#         return"Dog is barking"
# for i in [Animal(),Dog()]:
#     print(i.sound())


"""
.4. Employee Management System
Create an Employee class with:
employee name
salary
Add methods to:
display details
increase salary by 10%
Create 2 employee objects and display updated salaries.


"""

class Employee:
    def __init__(self,):
        self.name=input("Enter Name::")
        self.salary=int(input("Enter Salary::"))

    def Salary(self):
        return f"Increased Salary by 10% is:{self.salary+self.salary*0.01}"
    
emp=Employee()
print("Name of Employe is::",emp.name)
print("Salary of Employee is::",emp.salary)
print(emp.Salary())