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
    
print(evenodd(10))