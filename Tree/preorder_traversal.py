class Node():
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

# preorder traversal of binary tree 
# root, left, right
def preorder_traversal(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# postorder traversal using 2 stacks
# left, right, root
def postorder_two_stacks(root):
    if not root:
        return
    stack_1 = []
    stack_2 = []
    stack_1.append(root)
    while len(stack_1) > 0:
        node = stack_1.pop()
        stack_2.append(node.val)
        if node.left:
            stack_1.append(node.left)
        if node.right:
            stack_1.append(node.right)
    while len(stack_2) > 0:
        print(stack_2.pop())


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder traversal of a binary tree:")
preorder_traversal(root)
print("\npostorder traversal with two stacks:")
postorder_two_stacks(root)