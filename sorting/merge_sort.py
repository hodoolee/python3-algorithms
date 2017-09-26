# it takes an array and returns a sorted array
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2 # it gives an integer otherwise a float

    left = merge_sort(A[0:mid])
    right = merge_sort(A[mid:len(A)])
    
    return merge(left, right)

# it merges in sorted list n-1 times
def merge(left, right):
    sorted_list = []

    while len(left) != 0 and len(right) != 0:
        if left[0] >= right[0]:
            sorted_list.append(right.pop(0))
        else:
            sorted_list.append(left.pop(0))
    
    # it ensures that no element is left in left and right list
    return sorted_list + left + right

