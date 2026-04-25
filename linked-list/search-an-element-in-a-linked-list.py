"""
Problem Statement: 
Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.


"""

# node class to represent each element in the linked list
class Node:
    # constructor to initialize data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchValue(self, head, key):

    	"""
        Time O(n) - traverse the entire linked list to check the target value
        Space O(1)
    	"""
        # pointer to traverse the list
        curr = head

        # traverse until end
        while curr:
            # check if current node matches key
            if curr.data == key:
                # return True if found
                return True
            # move to next node
            curr = curr.next

        # return False if not found
        return False