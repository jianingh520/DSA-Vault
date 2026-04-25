"""
what is linked list -
(from strivers A2Z Sheet)

Linked List is a linear data structure that can be visualized as a chain with different nodes connected, where each node represents a different element. The difference between arrays and linked lists is that, unlike arrays, the elements are not stored at a contiguous location.

For any element to be added in an array, we need the exact next memory location to be empty and it is impossible to guarantee that it is possible. Hence adding elements to an array is not possible after the initial assignment of size.

A linked list is a data structure containing two crucial pieces of information, the first being the data and the other being the pointer to the next element. The ‘head’ is the first node, and the ‘tail’ is the last node in a linked list.

Pointers -
A pointer is a variable that stores the memory address of another variable. In simpler terms, it "points" to the location in memory where data is stored. This allows you to indirectly access and manipulate data by referring to its memory address.

Applications of Linked Lists -
Creating Data Structures: Linked lists serve as the foundation for building other dynamic data structures, such as stacks and queues.
Dynamic Memory Allocation: Dynamic memory allocation relies on linked lists to manage and allocate memory blocks efficiently.
Web Browser is one important application of Linked List.


Types of Linked Lists - 
Singly Linked Lists: In a singly linked list, each node points to the next node in the sequence. Traversal is straightforward but limited to moving in one direction, from the head to the tail.
Doubly Linked Lists: In this each node points to both the next node and the previous node, thus allowing it for bidirectional connectivity.
Circular Linked Lists: In a circular linked list, the last node points back to the head node, forming a closed loop.

"""

# node class represents a node in the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data      # data value
        self.next = next      # pointer to next node


if __name__ == "__main__":
    # create an array
    arr = [2, 5, 8, 7]

    # create first node
    y = Node(arr[0])

    # print memory reference of node
    print(y)

    # print data stored in node
    print(y.data)