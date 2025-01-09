def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = [14, 11, 17, 3, 21]
print("Original array:", array)
insertion_sort_descending(array)
print("Sorted array:", array)
