"""
specific symbols which are used to perform any operations in python

*Types of operators:__++_-
1.Arithmetic operator:
    +,-,*,/,//,%
2.Relational operators(compare):
    <,>,<=,>=,==,!=
3.Bitwise operators(perform bitwise calculation):
    & , 1 , ~,^,>> ,<<

4. Logical Operatons:
    And , or , not

5. Assignment Operator :
    ==,+=,-=
6.Identity Operators (check)
    is not , is 
7. Membership operator:
     in , not in
"""
# ?Arithmetic Operatons
# a=11
# b=4
# print("Addition:",a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Division:",a/b)
# print("Floor division:",a//b)  #whole number after division
# print("Modulus:",a%b)  
# print("Exponent:",a**b)  

#? Relational or compare Operatons
# a=20
# b=4
# print("Compare::",a>b)
# print("Compare::",a<b)
# print("Compare::",a>=b)
# print("Compare::",a<=b)
# print("Compare::",a==b)
# print("Compare::",a!=b)


#? Bitwise Operator
# a=10
# b=4
# print("Bitwise end:",a&b)
# print("Bitwise OR:",a|b)
# print("Bitwise Not:",~a)
# print("Bitwise Shift:",a>>2)
# print("Bitwise Shift:",a<<2)

# ?Logical Operatons

# a=True
# b=False
# print("Logical And::",a and b)
# print("Logical OR::",a or b)
# print("Logical NOT::",not a)


# ?Assignment Operator

# a=10 
# b=10
# print("Print b:",b)
# b+=a
# print("Addition:",b)
# b-=a
# print("Negation:",b)
# print("Identity Operator::",a is b)

# ?Stores Marks and check availability
# list=[10,20,5,15,28]
# x=15
# if(x not in list):  #check  is it available or not
#     print("X is not available student")
# else:
#      print("X is  available")

# y=20
# if(y  in list):  #check  is it available or not
#     print("Y is  available in List")
# else:
#      print("Y is  not available")


#? 2nd way to assignment or ternary operator
# a,b=10,20
# min= a if a<b else b
# print(min)


# a,b=30,20
# min= a if a<b else b
# print(min)

# ? Multiple conditions
num=10+20*30
print(num)

# ! 1st block output 
name="Divya"
age=20
if name== "Rohan" or name=="Divya" and age>=18:
    print("You are member of my club and also you are an adult")

else:
    print("Either you're not a member or you're not an adult")

# ! 2nd block output 
name="Sourabh"
age=20
if name== "Rohan" or name=="Divya" and age>=18:
    print("You are member of my club and also you are an adult")

else:
    print("Either you're not a member or you're not an adult")
