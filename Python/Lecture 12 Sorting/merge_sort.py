"""

Merge Sort:
    1.It is a divide and conquer technique
    2.It divides the input array in two halves, call itself for the two halves and then merge the two sorted halves
    3.The merge() function is used for merging two sorting halves

    Divide: Divide untill gets individual element
    conquer: compare and Sort to the individual element 
    merge: Merge after sorting


    l=length r=1st element


    mid point=l+(r-1)/2
    left divide=[:mid]
    right divide: [mid:]
"""

def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    




arr=[12,11,13,5,6,7]
print("Given Array is: ",arr)
arr1=merge_sort(arr)
print("Sorted Arrays is :",arr1)