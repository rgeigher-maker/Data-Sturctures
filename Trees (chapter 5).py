"""
Homework #1:Tree
Write a Python program to insert a node with value 6 into the following binary tree. With the following specific
requirements:
    1) Write the InsertPreorder function to insert node 6 into the tree using the Preorder- DFS traversal method.
    2) Write a function to display the tree using the Postorder - DFS traversal method.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insertPreorder(node, value):
    if node is None:
        return Node(value)

    if node.left is None:
        node.left = Node(value)
        return True
    if node.right is None:
        node.right = Node(value)
        return True

    if insertPreorder(node.left, value):
        return True
    if insertPreorder(node.right, value):
        return True

    return False


def printPostorder(node):
    if node is None:
        return

    printPostorder(node.left)
    printPostorder(node.right)
    print(node.value, end=" ")


root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)

print("Original Tree (Postorder):")
printPostorder(root)

insertPreorder(root, 6)

print("\n\nTree after inserting 6 (Postorder):")
printPostorder(root)

"""
Homework #2: Tree
Given a Binary Search Tree as shown below. Use Python to implement the program including the following requirements
(any tree traversal algorithm can be used):
    1) Write a function to input the tree values from the keyboard
    2) Calculate the sum of the values of the tree nodes with the condition that those nodes are divisible by 5.
    3) Write a function to print the values of the tree to the screen
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def createTree():
    user_Input = input("Please enter the tree values (note: separate the values by spaces): ").split()

    root = None
    for x in user_Input:
        root = insert(root, int(x))
    return root

def sum(root):
    if root is None:
        return 0

    current_val = 0
    if root.val % 5 == 0:
        current_val = root.val

    return current_val + sum(root.left) + sum(root.right)


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)


if __name__ == "__main__":
    my_tree = createTree()

    print("\nTree values (In-order traversal):")
    print_tree(my_tree)

    total = sum(my_tree)
    print(f"\nSum of nodes divisible by 5: {total}")

"""
Homework #3: Tree
Given a Binary Search Tree (BST) as shown below. Use Python to implement the program including the following
requirements (any tree traversal algorithm can be used):
    1) Write a function to input the tree values from the keyboard
    2) Sum of k largest elements in BST: Find Sum Of All Elements greater than or equal to Kth largest Element In BST.
    3) Write a function to print the values of the tree to the screen
"""
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def print_tree(self, root):
        if root:
            self.print_tree(root.left)
            print(root.val, end=" ")
            self.print_tree(root.right)

    def sum_k(self, root, k):
        self.count = 0
        self.total_sum = 0

        def reverse_inorder(node):
            if not node or self.count >= k:
                return

            reverse_inorder(node.right)

            if self.count < k:
                self.count += 1
                self.total_sum += node.val

                reverse_inorder(node.left)

        reverse_inorder(root)
        return self.total_sum


if __name__ == "__main__":
    tree = BinarySearchTree()

    val_input = input("Enter the tree values separated by space: ")
    values = list(map(int, val_input.split()))

    for val in values:
        tree.root = tree.insert(tree.root, val)

    k_val = int(input("Enter the value of k: "))

    print("\nTree values (In-order):", end=" ")
    tree.print_tree(tree.root)

    result = tree.sum_k(tree.root, k_val)
    print(f"\nSum of the {k_val} largest elements: {result}")