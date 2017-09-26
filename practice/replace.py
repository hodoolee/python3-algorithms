# A recursive function to replace all 0s with 5s in an integer
def convert_five(n):
    if len(n) <= 1:
        if n == '0':
            return '5'
        else:
            return n
    
    mid = len(n) // 2
    left = convert_five(n[0:mid])
    right = convert_five(n[mid:len(n)])
    
    return left + right

if __name__ == "__main__":
    print(convert_five(105)) #=> "155"
