"""
def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        
        # Find the index of the minimum element in the unsorted part of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the elements

# Get array size from user
size = int(input("Enter the size of the array: "))

# Get array elements from user
arr = []
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Sort the array
selection_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
