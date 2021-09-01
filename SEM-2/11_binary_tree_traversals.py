""" Python Script to create a binary tree and perform various traversals """

# Write your code from here


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
          # add values from left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
          # add values from right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements    

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
  numbers = [17,4,1,20,9,23,18,34]
  numbers_tree = build_tree(numbers)
  print("In order traversal:", numbers_tree.in_order_traversal())
  print("\nPre order traversal:", numbers_tree.pre_order_traversal())
  print("\nPost order traversal:", numbers_tree.post_order_traversal())


## OUTPUT :
"""
In order traversal: [1, 4, 9, 17, 18, 20, 23, 34]

Pre order traversal: [17, 4, 1, 9, 20, 18, 23, 34]

Post order traversal: [1, 9, 4, 18, 34, 23, 20, 17]
"""
