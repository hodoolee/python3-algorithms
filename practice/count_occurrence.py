# http://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
# Given a sorted array arr[] and a number x,
# write a function that counts the occurrences of x in arr[]
# Expected time complexity is O(log n)

def count_occurrence(A, x):
    # base case
    if len(A) <= 1:
        # it matches
        if A[0] == x:
            return 1
        # does not match
        else:
            return 0

    mid = len(A) // 2
    left = count_occurrence(A[0:mid], x)
    right = count_occurrence(A[mid:len(A)], x)

    return left + right


if __name__ == "__main__":
    A = [1, 1, 2, 2, 2, 3]
    print(count_occurrence(A, 1)) #=> expect 2
