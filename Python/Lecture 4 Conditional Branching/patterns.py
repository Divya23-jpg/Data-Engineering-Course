"""
1
2 2
3 3 3


"""

# ? Simple
n = int(input("Enter number: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

# ? String Multiplication
"""
    multiply str version of int
"""
n=int(input("Enter number:"))
for i in range(1,n+1):
    print(str(i)*i)


# ? Mathematical 
n=int(input("Enter number:"))
for i in range(1,n+1):
    print((10**i//9)*i)