"""

Bubble sort:
    1.compare each pair of Adjacent element
    2.if the 1st element is greater than second than swap
    3. After each full pass, the largest unsorted element "Bubbles up" to its correct position
    4.Repeat this process for the remaing unsorted portion to the list
    5.Algorithm will stop early if there is no swap occurs in a pass,meaning array is already sorted


"""
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[64,34,25,12,21,11,90]
bubble(arr)
print("Buuble Sort")
print(arr)