"""
Homework #1: Heaps
Given an Array as shown below. Use Python to implement the program including the following require
    1) Write a function to input the tree values from the keyboard
    2) Heap Sort for decreasing order using Min Heap.
    3) Write a function to print the values after sorting to the screen
"""
def heapify(arr,n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr,n,smallest)

def heapSortDecreasing(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1,):
        heapify(arr,n,i)

    for i in range(n -1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)

def treeValues():
    userInput = input("Please enter the array that you want to use (make sure they are separated by spaces): ")
    return [int(x) for x in userInput.split()]

def printTree(arr):
   print("Your printed tree (in descending order) is: ", arr)

if __name__ == "__main__":
    data = treeValues()

    heapSortDecreasing(data)

    printTree(data)