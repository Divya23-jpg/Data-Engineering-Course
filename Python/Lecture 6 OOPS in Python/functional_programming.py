"""
Functional Programming:

It is programming paradigm in which we try to bind everything
in a pure mathematical functions

Any functional programming language is expected to have the following concept

1. pure function: These function should have main properties
    a.They always produce the same output for same argument
    irrespective of anything else.
    b. They have no side effects that is they do not modify any argument or global variable or output


2. Recursion : There are no "for" or "while" loops in functional 
language . Iteration in Func. Prog. done through recursion



3.Variables are Immutable: In functional programming we cannot modify
a variable after its been initialized.But we can create new variable


4. Functions are First class and can be Higher Order:
    First class (functions) are treated as First class variable
    The first class variable can be passed to function as a peramter and can be return from functions
    or store in data structure



"""

# ! PURE FUNCTION

# def pure_func(list):
#     new_list=[]
#     for i in list:
#         new_list.append(i**2)
#     return new_list

# my_list=[1,2,3,4]
# modified=pure_func(my_list)
# print(modified)


# ! Recursion

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(5))


# ! Functions are First class Citizens in Python

def shout(text):
    return text.upper() + "!!!"
def whisper(text):
    return text.lower() + "..."
def greet(func):
    greeting=func("Hello World")
    print(greeting)

greet(shout)
greet(whisper)

"""
A function is an instamce of object type.
You can store the function in a variable
You can pass the function as an argument to another function
You can return a function from another function
You can store functions in data structure such as list,dict,etc


"""