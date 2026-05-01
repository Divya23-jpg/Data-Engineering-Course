"""
Flow Control statement:

1.break: Immediatly exit the loop directly
2.continue:skip the current iteration and jumps to next one
3.pass: Null operation used AS  a placeholder when a statement is
syntactically required but no action required


"""


# * Example
# for x in range(3):
#     if x==2:
#         print(x)
#         break

# for x in range(3,30,2):
#     if x==1:  #No chnage because we dont have 1 in range
#         break
#     print(x)

# for x in range(3,30,2):
#     if x==11:  #break on 11
#         break
#     print(x)


#! WAP to identify prime number from a list of number
import math

def is_prime(n):
    if n<=1:
        print("Not a prime number")
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
list=[2,3,5,7,9,11,13,15,17,19,20]
prime_num=[num for num in list if is_prime(num)]

print("Prime Number list:",prime_num)