"""
Insertion sort

    1.This sorting  algorithm works by iteratively each ele of an unsorted list into its correct position in a sorted portion of the list

    Working:

    1.start from the 2nd ele (1st is already sorted)
    2.compare the current ele (key)
    3.shift all larger elements one position to the right
    4.Insert the key ele into its correct position
    5.Repeat untill the entire array is sorted



"""

def insertion (arr):
    n=len(arr)
    for i in range(n):
        key=arr[i]
        
        