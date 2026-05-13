"""
print negative number and if positive window them print 0
window=2
input: arr[-8,2,3,-6,1]
Output: [-8,0,-6,-6]
"""

def window(arr,k):
    n=len(arr)
    for i in range(n+1):
        Sum=sum(arr[:k])
        li=[]
        if Sum<0:
            li.append(0)
        else:
            li.append(i)
    return li






arr=[-8,2,3,-6,1]
k=2
print(window(arr,k))