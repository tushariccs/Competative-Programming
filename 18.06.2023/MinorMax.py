import math

def min_or_max_array(arr):
    arr.sort()
    

    # array will be in sorted order and mostly 1 element will be minimum and last one max
    
    minmax ={"min":arr[0],"max":arr[-1 ]}
    return minmax 


arr = [1000, 11, 445, 1, 330, 3000]
minmax = min_or_max_array(arr)
print("Max element is: ",minmax["max"])
print("Min element is: ",minmax["min"])


# Time Complexity is O(n log n) due to sorting time complexity
#Space complexity is O(1) only as we are not much memory.