# http://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
# Solution:

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

# check if given trees are isomorphic
def is_isomorphic(r1, r2):
    # two empty trees are isomorphic
    if r1 is None and r2 is None:
        return True
 
    # one of tree is None, then they are not isomorphic
    if r1 is None or r2 is None:
        return False
    
    # if two nodes are not same, then they are not isomorphic
    if r1.data != r2.data :
        return False

    # Case 1: Cross ISO
    # CAse 2: Same ISO => they are same
    return ( (is_isomorphic(r1.left, r2.left) and is_isomorphic(r1.right, r2.right)) or
             (is_isomorphic(r1.left, r2.right) and is_isomorphic(r1.right, r2.left))
           )

if __name__ == "__main__":
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)
    r1.left.right = Node(5)
    r1.right.left = Node(6)
    r1.left.right.left = Node(7)
    r1.left.right.right = Node(8)

    r2 = Node(1)
    r2.left = Node(3)
    r2.right = Node(2)
    r2.right.left = Node(4)
    r2.right.right = Node(5)
    r2.left.right = Node(6)
    r2.right.right.left = Node(8)
    r2.right.right.right  = Node(7)

    print(is_isomorphic(n1, n2))
