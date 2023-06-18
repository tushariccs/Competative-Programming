class pair:
    def __init__(self):
        self.max = 0
        self.min = 0
        
def getMinMax(arr:list,n:int)->pair:
    minmax = pair()
    
    # If there is one element in the list then we should consider min and max both the same.
    if n==1:
        min = arr[0]
        max = arr[0]
    
    # If there are more than one elements, then initialize min
    # and max
    if arr[0]>arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    elif arr[0]<arr[1]:
        minmax.max = arr[1]
        minmax.min = arr[0]    
    
    for i in range(2,n):
        if arr[i]>minmax.max:
            minmax.max = arr[i]
        elif arr[i]<minmax.min:
            minmax.min = arr[i]
    return minmax

if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
    
    
# Time Complexity: O(n)
# Auxiliary Space: O(1) as no extra space was needed.

# In this method, the total number of comparisons is 1 + 2(n-2) in the worst case and 1 + n – 2 in the best case. 
# In the above implementation, the worst case occurs when elements are sorted in descending order and the best 
# case occurs when elements are sorted in ascending order.
        