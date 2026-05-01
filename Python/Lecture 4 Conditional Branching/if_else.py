"""
Conditional statements allows you to execute s specific
block of code on whether a condition is TRUE or FALSE

These are fundamental for decision making and controlling
a program flow.

core keyword:
if: condition is TRUE
else: default block that runs when all condition is FALSE
elif: check additional condition if the preceding if is FALSE


"""
"""
# ? Syntax

if (conditiona):
    # instruction
elif(condition):
    # instruction
else:
     # instruction
"""

# ! Check person is allowed to enter in club, consert or not basis on age

# *check student is pass or not
# ? short method or ternary operator

marks=45
result="pass" if marks>=44 else "Fail"
print(f"Result: {result}")

# * Senior Citizen Quotas (NESTED CONDITIONAL STATEMENT)

"""Railway ticket booking app
condition:
if senior citizen age>60 provisw 20% discount
if senior citizen age>70 provisw 20% discount
"""
age=int(input("Enter age::"))
if(age>=60):
    if(age>=70):
        print("You got 30 percent discount")
    else:
         print("You got 20 percent discount")

else:
    print("You are Eligible for 5 percent discount")


