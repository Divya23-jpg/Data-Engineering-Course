"""

Sliding Window is a Technique in DSA We can apply in list / array
problem solved by sliding window
1.Sub array,/sub string 
2.Array/ String

Optimiziation is possible where something is repeating


Types of  sliding window
1. Fixed size window (k is given)
2. Variable size window 
"""
# ?  Fixed size window (k is given)
# ! Find Sum of a Maximum sub array and  window size will be k=3

"""
1,2,3,4,5,6
subarray: 123 , 234, 345, 456,
Sum:       6,    9,  12,  15


"""
# ? Btrute force aprroach
# ! iteration : n-k+1  n is a size of array
# * Time complexity is O(n2)
# def subarray(arr,n, k):    
#     max_sum=0
#     for i in range(n-k+1):
#         curr_sum=0
#         for j in range(k):
#             curr_sum=curr_sum+arr[i+j]
#         max_sum=max(max_sum,curr_sum)
#     return f"Maximum sum of array is: {max_sum}"

   
# if __name__=="__main__":
#     arr=[5,2,-1,0,3]
#     k=3
#     n=len(arr)
#     print(subarray(arr,n,k))

# ! using sliding window
# * Time complexity is O(n)
def sub_array_window(arr,k):
    n=len(arr)
    if n<k:
        return -1
    
    window=sum(arr[:k])
    max_sum=window
    
    for i in range(k,n):
        window+= arr[i]-arr[i-k]
        max_sum=max(max_sum,window)
    return f"Maximum sum of array By sliding windowis: {max_sum}"

if __name__ =="__main__":
    arr=[5,2,-1,0,3]
    k=3
    n=len(arr)
    print(sub_array_window(arr,k))




# ?  Variable  size window 
# ! Find Sum of a Maximum sub array  that gives target 5 and  window size will be anything

"""
1,5,4,3,7,1,1,1,1,1
subarray: [5], [1 4], [1,1,1,1,1]
Sum:     5


"""


