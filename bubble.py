def bubble_sort(arr):
    n = len(arr)
    # outer loop to iterate through the list n times
    for i in range(n - 1):
        # inner loop to compare adjacent elemnets
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swapping the elements in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 2, 8, 3, 1, 6, 4]
arr = bubble_sort(arr)
print(arr)
