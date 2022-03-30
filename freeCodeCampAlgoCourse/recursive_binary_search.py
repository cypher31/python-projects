def recursive_binary_search(list, target):
    if len(list) == 0: return False
    else:
        mid = (len(list))//2

        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)

def verify(result):
    print("Target found:", result)

numbers = range(9)

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)