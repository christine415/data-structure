class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal 
# left, root, right
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val)
        printinorder(root.right)

# root, left, right
def printpreorder(root):
    if root:
        print(root.val)
        printpreorder(root.left)
        printpreorder(root.right)
        
# left, right, root
def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val)

# create a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder tree traversal is")
printinorder(root)
print("\nPreorder tree traversal")
printpreorder(root)
print("\nPostorder tree traversal")
printpostorder(root)
