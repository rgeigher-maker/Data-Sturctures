"""
Homework #1: Graph
Given a Graph as shown below. Use Python to implement the program including the following requirements:
    1) Write a function to input the Graph from the keyboard. Represent the graph using an adjacency matrix
    2) Write a function to delete node 2 in the graph
    3) Display the graph before and after deletion on the screen
"""
def createGraph():
    nodes = int(input("Enter the number of nodes desired: "))
    matrix = [[0] * nodes for _ in range(nodes)]
    userInput = input("Enter the edge pairs (make sure they are separated by spaces): ")
    values = list(map(int, userInput.split()))

    for i in range(0, len(values) - 1, 2):
        u, v = values[i], values[i + 1]
        if u < nodes and v < nodes:
            matrix[u][v] = 1
            matrix[v][u] = 1

    return matrix


def deleteNode(matrix, nodeToDelete):
    matrix.pop(nodeToDelete)
    for row in matrix:
        row.pop(nodeToDelete)
    return matrix


def displayGraph(matrix, title):
    print(f"\n{title}")
    for row in matrix:
        print(row)


graph = createGraph()
displayGraph(graph, "Adjacency Matrix (Before Deletion)")

graph = deleteNode(graph, 2)
displayGraph(graph, "Adjacency Matrix (After Deleting Node 2)")