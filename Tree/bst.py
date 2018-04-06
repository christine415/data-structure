class Node():
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Insert a new node with the given key
def insert(root, node):
    if not root:
        root = node
    else:
        if root.val < node.val:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)

# Want to find key in binary search tree
def search(root, key):
    if key == root.val or not root:
        return root
    if root.val < key:
        return search(root.right, key)
    elif root.val > key:
        return search(root.left, key)

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
insert(r, Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

inorder(r)