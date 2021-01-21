class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # add data in left sub-tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right sub-tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []

        # Visit left child recursively
        if self.left:
            elements += self.left.inorder_traversal()

        # Visit the root node
        elements.append(self.data)

        # Visit the right child recursively
        if self.right:
            elements += self.right.inorder_traversal()

        return elements


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # value in left sub-tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # value in right sub-tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
            



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])

    return root

# ------------------------------------------------------------------
# 1. List with Numbers
numbers = [17,4,1,20,9,23,18,34,18,4]

numbers_tree = build_tree(numbers)
print(numbers_tree.inorder_traversal())

print(numbers_tree.search(20))

print("#####################################################")

# 2. List with Strings

countries = ["India", "UK", "US", "Australia", "Iceland", "Finland", "Sweden"]
countries_tree = build_tree(countries)

print("Is UK on the list: ", countries_tree.search("UK"))
print("Is Poland on the list: ", countries_tree.search("Poland"))

print(countries_tree.inorder_traversal())


