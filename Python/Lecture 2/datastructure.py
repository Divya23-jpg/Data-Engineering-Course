# x=y=z="Banana"
# print(x)


# Data Structure in Python

# ? List


"""
List is a collection of same data type

"""
# fruits=["Banana","Mango","Oranges"]
# print(fruits)


# x=56
# print("Your Total Percentage is:",x)
# print(f"Your Total percentage is: {x}")


# y=90.55
# print("Percentage is:",y)
# # f string provide a way to combine a expression inside a string literals using minimal syntax
# print(f"Your Total percentage is: {x}")
# # .formate method for printing
# print("My Percentage is {}.".format(y))



# import datetime
# name="Divya"
# age=16
# dob= datetime.date(2005,9,7) # year,month,date
# print(f'My name is {name} and my age is {age},and DOB is {dob}')



# def sum(a,b):
#     return a+b

# print(sum(3,4))

# ? Variables Types: Global and local
"To define a scope of any variable we need to check the Indentation"

x=10 #Global variable
def abc(a,b):
  
    x=89   #local variable
    print(a,b,x)

# print(f'the value of {abc()}')
abc(11,12)
print(x)  #Global variable



# ?  Case study
"""
A person require for normal  at least 80% of marks than he will be qualified for
a test for physical test.

CONDITION: If he is a sports person then qualification reduces to
75%

1.Decalare a global variable which stores marks
2. create a function to check whether a person is from sports kota or not


"""

# marks=80  #Global
# def sport():
    
#     # global sports
#     sports="True"  #Local
#     if(sports=="True"):
#         return "New Qualifying marks are 75"
#     else:
#         return "You are not a sports person so marks cannot reduces"



# print(f"Hello,you got {marks} and your sports quota {sports},hence {sport()} ")

# OUTPUT 
# NameError: name 'sports' is not defined. Did you mean: 'sport'?


marks=80  #Global
def sport():
    
    global sports
    sports="True"  #Local
    if(sports=="True"):
        return "New Qualifying marks are 75"
    else:
        return "You are not a sports person so marks cannot reduces"


sport()
print(f"Hello,you got {marks} and your sports quota {sports},hence {sport()} ")


# ORRRR
marks=80  #Global
def sport():
    
    global sports
    sports="True"  #Local
    if(sports=="True"):
        return "New Qualifying marks are 75"
    else:
        return "You are not a sports person so marks cannot reduces"


sport()
print(f"Hello,you got {marks} and your sports quota {sports},hence {sport()} ")

