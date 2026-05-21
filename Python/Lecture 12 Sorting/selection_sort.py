"""

Selection Sort
    1.Comparison based technique .
    2. It sorts array by repeatedly finding the smallest and largest elementin
       the unsorted portion and place them in its correct position

working:
    1.start with the 1st ele and find smallest ele in entire array by iterating overwrite
    2. Swap this smallest element with the 1st ele
    3. Move to 2nd ele find 2nd smallest and place with 2nd ele
    4. Repeat this proccess untill the entire array becomes sorted

"""
def selection(arr,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if arr[j]<arr[min]:
                min=j 
            arr[i] , arr[min]= arr[min],arr[i]

      
# def selection(arr, size):
#     for i in range(size):
#         min_index = i
#         for j in range(i+1, size):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         # Swap after finding the minimum in the remaining array
#         arr[i], arr[min_index] = arr[min_index], arr[i]




arr=[-2,45,0,11,-9,88,-97,-202,747]
size=len(arr)
selection(arr,size)
print(arr)