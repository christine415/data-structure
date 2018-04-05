class Node():
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Use queue to store child nodes
def bfs(root):
    if not root:
        return
    # Create a queue
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].val)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Breadth first research of binary tree is")
bfs(root)
