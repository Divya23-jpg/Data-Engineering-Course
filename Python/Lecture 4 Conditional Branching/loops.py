"""
 Loops are the block of code used to execute specific code block repeatatively on the basis of a condition

There are 2 types of loops in python:
1.for loop
2.while 


"""
# *syntax for for loop
"""
A for loop is a control structure used to repeat a block of code a specific number of times.
It’s especially useful when you know in advance how many iterations you need.
"""
# range()
# ?No Staring Point By default 0
print("Only end condition\n")
for i in range(11):
    print(i)


# ? Start and end condition
print("Start and  end condition\n")
for i in range(0,11):
    print(i)


# ? start ,end and skip
print("Start ,end and skip  condition")
for i in range(0,11,2):
    print(i)




# *syntax for while loop
"""
A while loop is another control structure in Python, but unlike a for loop (which runs a fixed number of times), 
a while loop keeps running as long as a condition is true.
Use case: when we  unknown  No of Iteration
and depends on Dynamic condition
"""


# i=1
# while i<=10:
#     print(i)
#     i += 1
    

