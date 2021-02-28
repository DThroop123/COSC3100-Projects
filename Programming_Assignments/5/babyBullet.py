"""
babyBullet.py - developing a skip list with one additional level
Date - 02/29/21 
Author - Daniel Throop
Class - COSC 3100

"""
# class defining a arbitrary node in the list
class Node:
    def __init__(self, key, value, next_node, next_bullet):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.next_bullet = next_bullet

# testNode = Node("two", 2, None, None)

class List:
	# fine
    def __init__(self):
        self.head = None
        self.tail = None

    # needs to be modified
    def insert(self, key, value):
    	# now inserts extra next_bullet
        new_node = Node(key, value, None, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif self.head.key > key: 
            # connect to next baby node since it is the new head
            new_node.next_bullet = self.head.next_bullet
            # should we set the previous heads baby bullet pointer to None?
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.key < key:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
            if not new_node.next_node:
                self.tail = new_node