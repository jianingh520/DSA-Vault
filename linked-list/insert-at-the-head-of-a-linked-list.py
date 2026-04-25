
"""
To insert a new node with a value before the head of the list, create 
Create a new node with data as the given value and pointing to the head. This node will be our new head of the linked list.
Return the new node as the head of the updated Linked List.

"""
# node class to represent each element in the linked list
class Node:
    # constructor to initialize data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# class to handle linked list operations
class Solution:
    def insertAtHead(self, head, newData):
    	"""
		function to insert a new node at the head
		- create a new node whose next points to current head
		- return the new node as the head

		Time O(1): creating a new node and updating the head takes constant time
		Space O(1): only one extra node is created to insert at the head of the 
    	"""
        newNode = Node(newData, head)
        return newNode

    def printList(self, head):
    	"""
		function to print the linked list
    	"""
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    sol = Solution()

    # creating a sample linked list: 2 -> 3
    head = Node(2)
    head.next = Node(3)

    print("Original List:", end=" ")
    sol.printList(head)

    # inserting new node at head
    head = sol.insertAtHead(head, 1)

    print("After Insertion at Head:", end=" ")
    sol.printList(head)
