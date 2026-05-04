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

# !Default argument Example
def myfunc(x,y=30):
    print("X:",x)
    print("Y:",y)

# print(myfunc(50))
# print(myfunc(50,100))

# ! Keyword Argument (Order not  matters)
def student(fname,lname):
    print(fname,lname)

# student(fname="Divya",lname="Kumawat")
# student(lname="Kumawat",fname="Divya")

# ! Positional Argument (Order matters)
def nameage(name,age):
    print("Hy , I am" , name)
    print("Hi , My age is " , age)

# nameage("Divya",22)

# ! lambda Function
lambda_var=lambda x: x*x*x
print(lambda_var(3))

# ! Recursion Function

