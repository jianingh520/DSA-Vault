"""
Problem Statement: 
Given the head of a linked list, print the length of the linked list.

"""

# node class to represent each element in the linked list
class Node:
    # constructor to initialize data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
	def lenthOfLinkedList(self, head):
		"""
		traverse the linked list and count the number of node on the fly using a counter
		Time O(n), Space O(1)
		"""
		cnt = 0
		temp = head # initialize a temporary pointer to head to keep the original head for returning or reusing
		while temp:
			cnt += 1
			temp = temp.next
		return cnt


if __name__ == "__main__":
    # creating a sample linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # create Solution object
    obj = Solution()

    # find and print the length of linked list
    print("Length of Linked List:",
          obj.lengthOfLinkedList(head))