import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self._insert(data, self.root)
        else:
            self.root = Node(data)
    
    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)
    
    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return -1
    
    def _height(self, node):
        if node:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1
        else:
            return -1
    
    def search(self, data):
        if self.root:
            return self._search(self.root, data)
        else:
            return None
    
    def _search(self, node, data):
        if not node or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)
    
    def delete(self, data):
        if self.root:
            return self._delete(self.root, data)
        else:
            return None
        
    def _delete(self, node, data):
        if node and data == node.data:
            if not node.left and not node.right:
                return None
            elif not node.left and node.right:
                return node.right
            elif node.left and not node.right:
                return node.left
            else:
                successor = self.get_inorder_successor(node)
                node.data = successor.data
                node.right = self._delete(node.right, successor.data)
        elif node and data < node.data:
            node.left = self._delete(node.left, data)
        elif node and data > node.data:
            node.right = self._delete(node.right, data)
        else:
            return None
        return node
    
    def get_inorder_successor(self, node):
        if node:
            node = node.right
            while node and node.left:
                node = node.left
            return node
        else:
            return None
        
    def display(self, indent=8):
        if self.root:
            self._display(self.root, 0, self._height(self.root), indent)
        else:
            return
    
    def _display(self, node, level, height, indent):
        if node:
            self._display(node.right, level+1, height, indent)
            print(" "*indent*level + "-"*indent + str(node.data))
            self._display(node.left, level+1, height, indent)
        else:
            return

bst = BinarySearchTree()

inserted = []

for i in range(10):
    value = random.randint(0, 100)
    bst.insert(value)
    inserted.append(value)

bst.display()
print(f"\nHeight of BST: {bst.height()}\n")

for i in range(10):
    value = random.randint(0, 100)
    if bst.search(value):
        print(f"{value} found in BST")
    else:
        print(f"{value} NOT found in BST")

random.shuffle(inserted)

for value in inserted:
    print(f"\nDeleting {value}")
    bst.delete(value)
    bst.display()