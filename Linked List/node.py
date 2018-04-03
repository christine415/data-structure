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

    def remove_duplicates(self):
        ''' Remove duplicates from a linked list'''
        ele = []
        node = self
        ele.append(node.val)
        while node:
            if node.next.val in ele:
                node.next = node.next.next
            else:
                ele.append(node.next.val)
            node = node.next
                
            
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.remove_duplicates()
    node1.traverse()