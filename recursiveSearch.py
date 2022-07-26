def binarySearch(arr, val=0):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid + 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# List of numbers
a = [1, 3, 4, 5, 6, 7, 11, 12, 23, 34, 51, 53, 55, 61, 70, 72]
# User provided number
val = 5
print(binarySearch(a, val))