""" Python Script to create a binary search tree and perform search operation """

# Write your code from here

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("\nIs UK in the list ? ", country_tree.search("UK"))
    print("\nIs Sweden in the list ? ", country_tree.search("Sweden"))

## OUTPUT :
"""
Building tree with these elements: ['India', 'Pakistan', 'Germany', 'USA', 'China', 'India', 'UK', 'USA']

Is UK in the list ?  True

Is Sweden in the list?  False
"""
