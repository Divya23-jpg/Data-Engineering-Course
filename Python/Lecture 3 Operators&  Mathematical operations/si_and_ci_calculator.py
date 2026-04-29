"""
Operators:

Calculate Simple Interest

Calculate Compund Interest
Amount=p*[1+(annual Interest rate /100)**t]
CI=Amount-principal
"""


# Simple Interest and  Compund Interest

principal=float(input("Enter Principle::"))
rate=float(input("Enter Rate::"))
time=float(input("Enter Time::"))
si=(principal*rate*time)/100
amount = principal * (1 + rate/100) ** time
ci = amount - principal
print("Simple Interest is:",si)
print("Simple Interest is:",ci)


