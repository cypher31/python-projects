def binary_search(list, target):
    first = 0
    end = len(list) - 1

    while first <= end:
        mid = (first + end)//2

        if list[mid] == target: return mid

        if list[mid] > target:
            end = mid - 1
        else:
            first = mid + 1
    
    return None

def verify(index):
    if index is not None:
        print("Target is at:", index)
    else:
        print("No target found.")

numbers = range(0, 100)

result = binary_search(numbers, 99)
verify(result)

result = binary_search(numbers, 101)
verify(result)
