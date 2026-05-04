"""
Syntax:

def function_name(parameter):
    
    / body of function
    return expression


"""

# ! Write a function to check number is even or odd

def evenodd(x):
    if(x%2==0):
        return "Even"
    else:
        return "Odd"
    
# print(evenodd(10))

# ?Default argument Example
def myfunc(x,y=30):
    print("X:",x)
    print("Y:",y)

print(myfunc(50))
print(myfunc(50,100))