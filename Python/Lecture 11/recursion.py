"""

Function Call itself is called recursion

"""
# ! Problem 1: Add without Operator
def add(a,b):
    if b==0:
        return a
    else:
        return add(a+1,b-1)
    
# print(add(3,4))
# ! Problem 2: Fibonacci series 
# def fibonacci(num):
#     if num<=1:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)
    
# num=10
# # print("Fibonacci series:")
# for i in range(num):
#     # print(fibonacci(i),end=' ')


# ! Problem 3: Print all increasing sequence of length k from a set of n natural number
# !Describtion: Given two numbers n and k , write a recursive function to print all increasing sequences 
# ! of length k that can be formed the first n natutral numbers
# Input:  n=3 k=2
# Output: 
#  1 2 
#  1 3
#  2 3



# def printArr(arr , k):
#     for i in range(k):
#         print(arr[i],end='')
#     print()


# def sequence(n,k,len,arr):
#     if len==k:
#         printArr(arr,k)
#         return 
#     i=1 if len==0 else arr[len-1] +1

#     len+=1
#     while(i<=n):
#         arr[len-1] 


# ! Problem 4: Factorial

def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n*factorial(n-1)
    
num=5
# * 1*2*3*4*5
print("Factorial Number is:",factorial(num))