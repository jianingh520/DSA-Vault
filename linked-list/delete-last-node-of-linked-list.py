"""
Problem Statement: 
Given a Linked List, delete the tail of the list and print the updated list.

"""
# node class to represent each element in the linked list
class Node:
    # constructor to initialize data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
	def deleteTail(self, head):
		"""
		To delete the tail of a linked list, we update the linkage between its last node 
			and its second last node. The main intuition is to point the second last node to null to get the updated linked list.

		edge cases: empty list, only one node

		Time O(n), Space O(1)
		"""

		# empty list or only one node
		if not head or not head.next:
			return None

		# traverse to the second last node
		curr = head
		while cur.next.next:
			curr = curr.next

		# delete tail node
		curr.next = None

		# return updated head
		return head

    def deleteNode(self, node):
        """
        To Delete node, we redirect the previous node's next pointer to the subsequent node of the one being deleted.

        Time O(1), Space O(1)
        """
        if not node or not node.next:
            return 

        # overwrite data of next node on current node
        node.val = node.next.val
        # make current node point to next of next node
        node.next = node.next.next



if __name__ == "__main__":
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)

	obj = Solution()
	head = obj.deleteTail(head)

	# print list after delete the tail
	temp = head
	while temp:
		print(temp.data, end=" ")
		temp = temp.next
