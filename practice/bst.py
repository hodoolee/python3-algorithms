class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right 

def is_bst(node, low=-float('INF')-1, high=float('INF')):
    if not node:
        return True
    return (node.data > low and node.data < high) and is_bst(node.left, low, node.data) and is_bst(node.right, node.data, high)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    
    print(is_bst(root)) #=> expect True
    
