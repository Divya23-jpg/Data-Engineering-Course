"""
print 1st negative number and if positive window them print 0
window=2
input: arr[-8,2,3,-6,1]
Output: [-8,0,-6,-6]
"""
from collections import deque
def window(arr,k):
    n=len(arr)
    li=[]
    for i in range(k-1):
        if i<0:
            li.append(arr[i])
    
    for j in range(1,k+1):
        
    
  






arr=[-8,2,3,-6,1]
k=2
print(window(arr,k))