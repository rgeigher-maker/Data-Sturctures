"""
Homework #1: Arrays
"""
# Step One: Initialization
dataArray = [3, 6, 4, 8] #this line create the array with the given values [3, 6, 4, 8]
print("Original Array:") #this line would print the array before adding addition numbers
print(dataArray)
print()

# Step Two: Insertion
dataArray.insert(0,7) #this line tells the code where to insert the 7. (0: the beginning position.)

# Step Three: Finalization
print("Updated Array:")
print(dataArray) #this line would print the array after adding addition numbers

"""
Homework #2: Lists
"""
def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


def average(arr):
    total = 0
    count = 0

    for x in arr:
        if x % 2 == 0:
            total += x
            count += 1

    return total/count if count > 0 else 0


list = [2, 5, 3, 1, 4, 7, 6]

print("Your list in descending order: ")
print(selectionSort(list.copy()))
print()
print("Your average of even numbers is: ")
print(average(list))

"""
Homework #3: Linked List
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def inputData():
    print("Enter the integers (please separate them by spaces): ")

    nums = list(map(int, input().split()))
    if not nums: return None

    head = Node(nums[0])
    curr = head

    for i in range(1, len(nums)):
        curr.next = Node(nums[i])

        curr = curr.next
    return head


def average(head):
    total = 0
    count = 0
    curr = head

    while curr:

        if curr.data % 2 == 0:
            total += curr.data

            count += 1

        curr = curr.next

    return total / count if count > 0 else 0


def split(head):
    if not head or not head.next:
        return None

    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    curr = head

    for _ in range((length // 2) - 1):
        curr = curr.next

    second_half = curr.next
    curr.next = None  # Break the link

    return second_half


def merge(first, second):
    if not first: return second

    if not second: return first

    if first.data <= second.data:
        first.next = merge(first.next, second)
        return first

    else:
        second.next = merge(first, second.next)

        return second


def merge_sort(head):
    if not head or not head.next:
        return head

    second = split(head)
    head = merge_sort(head)
    second = merge_sort(second)

    return merge(head, second)


def print_list(head):
    curr = head

    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print()


def main():
    head = inputData()

    if head:
        avg = average(head)

        print(f"\nAverage of even elements: {avg}")
        print()

        head = merge_sort(head)

        print("Sorted Linked List:")

        print_list(head)


if __name__ == "__main__":
    main()

"""
Homework #4: Stack
"""
def getUserInput():
    user_input = input("Please enter numbers separated by spaces: ")

    data_list = []
    for x in user_input.split():
        data_list.append(int(x))
    return data_list


def reverseArray(arr):

    stack = []

    for item in arr:
        stack.append(item)

    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr


def main():

    myArray = getUserInput()
    if not myArray:
        print("Array is empty.")
        return

    print(f"\nOriginal Data: {myArray}")


    reversedData = reverseArray(myArray)
    print(f"Reversed Data: {reversedData}")


if __name__ == "__main__":
    main()

"""
Homework #5: Queue
"""
from collections import deque


def userInput():
    try:
        user = input("Please enter the integers for the array (Note: make sure they are separated by spaces): ")
        arr = [int(x) for x in user.split()]
        return arr

    except ValueError:
        print("Error: Please enter only integers.")
        return []


def reverseArray(arr):
    if not arr:
        return []

    queue = deque()
    stack = []


    for element in arr:
        queue.append(element)

    while len(queue) > 0:
        stack.append(queue.popleft())

    reversed_arr = []
    while len(stack) > 0:
        reversed_arr.append(stack.pop())

    return reversed_arr


def main():
    arr = userInput()

    if arr:
        print(f"\nOriginal Array: {arr}")

        reversed_result = reverseArray(arr)

        print("Output: ", end="")
        print(*(reversed_result))


if __name__ == "__main__":
    main()