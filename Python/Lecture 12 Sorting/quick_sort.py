"""

Sorting algorithm  based on divide and conquer method
that picks an element as a pivot and partitions the given array around the picked pivot by
placing the  pivot and its correct position in the sorted array

? Steps To Perform Quick sort
1.Choosing pivot : Select an element from the array as the pivot element and choice of pivot can be anything
2.partition the array: Re arranging everything around the pivot.
After partitioning all elements smaller than pivot will be on the left side and all grater element will be in right
3. Recursive call: Apply recusrsively the same process
to get two potioned sub array
    *Base case: The recursion would stop when there is only one elemeent left in the sub array,as single element in already sorted

"""


def partition(arr,low,high):
    pivot=arr[high] #Last element  qill be pivot element
    i=low-1  #Index of smaller element
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1  # Increment index of the smaller element
            arr[i],arr[j]=arr[j],arr[i]  # Swap the element
    arr[i+1],arr[high]=arr[high],arr[i+1] #Swap pivot ele with element at index [i+1]
    return i+1

def Quick_sort(arr,low,high):
    if low<high:
        partitionIndex=partition(arr,low,high) # Partition index
        Quick_sort(arr,low,partitionIndex - 1)  # Recursively sort ele before partition (left side of pivot)
        Quick_sort(arr,partitionIndex +1,high)  # # Recursively sort ele before partition (right side of pivot)





arr=[10,2,8,9,1,5]
n=len(arr)
Quick_sort(arr,0,n-1)
print("sorted array is:",arr)