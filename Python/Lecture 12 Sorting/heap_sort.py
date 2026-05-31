"""Heap Sort:
1.It is a comparison Based sorting technique that uses a binary heap as data structure.
2.It convert data into Binary tree then perform sorting algorithm
3.It is Similar to selection sort where we repeatedly extract the maximum element and move it to the end of the array.

# *Algorithm

Step 1:.Majority works into two main phase:
    1.Build  a Max heap from the input data
    2.Extract element from the heap one by one place the maximum element at the end each time
Step 2:Rearrange the element to form Max Heap
Steo 3:Repeat untill the heap has only on element
Steo 4:Swap the Maximum eleent (root) with the last
Steo 5:Reduce the heap size by 1
Steo 6:create heap with the root to restore the heap properly
Steo 7:The array is  now sorted in the ascending order

"""