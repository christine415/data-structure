class Node():
    ''' Create nodes for linked list'''
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        ''' Traverse the linked list'''
        # Start from the header
        node = self
        while node:
            print(node.val)
            node = node.next
