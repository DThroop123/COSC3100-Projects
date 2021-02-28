"""
babyBullet.py - developing a skip list with one additional level
Date - 02/29/21 
Author - Daniel Throop
Class - COSC 3100

"""
import random

class Node:
    def __init__(self, key, value, next_node, next_bullet):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.next_bullet = next_bullet

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        new_node = Node(key, value, None, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif self.head.key > key: 
            # connect to next baby node since it is the new head
            new_node.next_bullet = self.head.next_bullet
            # setting previous head's next bullet pointer to null
            self.head.next_bullet = None
            # connecting to local node
            new_node.next_node = self.head
            # re-assinging head
            self.head = new_node
        else:
            current = self.head
            # traverse bullet nodes
            while current.next_bullet and current.next_bullet.key < key :
                current = current.next_bullet
            # tracks previous bullet before entering local nodes
            prevBullet = current
            # traverse local nodes
            while current.next_node and current.next_node.key < key :
            	current = current.next_node
            # calculate probablity of 1/3 
            prob = random.randint(1,3)
            # create new baby bullet node
            if(prob == 1):
            	# connect bullet nodes
            	new_node.next_bullet = prevBullet.next_bullet
            	prevBullet.next_bullet = new_node
            # connect local nodes
            new_node.next_node = current.next_node
            current.next_node = new_node
            if not new_node.next_node:
                self.tail = new_node

    # writes the order of the given list
    def writeOrder(self):
        print("Head {}: {}".format(self.head.key, self.head.value))
        print("Tail {}: {}".format(self.tail.key, self.tail.value))
        current_node = self.head
        while current_node:
            print("{}: {}".format(current_node.key, current_node.value))
            current_node = current_node.next_node	

    # writes both normal list structure and baby bullet structure of the given list
    def writeStructure(self):
        print("Head {}: {}".format(self.head.key, self.head.value))
        print("Tail {}: {}".format(self.tail.key, self.tail.value))
        current_node = self.head
        # regular structure
        print("List Structure:")
        while current_node:
            print("[{}: {}]-->".format(current_node.key, current_node.value), end = '')
            current_node = current_node.next_node
        # baby bullet structure
        print("\n" + "Baby Bullet Structure:")
        current_node = self.head
        while current_node:
        	print("[{}: {}]-->".format(current_node.key, current_node.value), end = '')
        	current_node = current_node.next_bullet

records = [ (1,'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'),
            (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), (10, 'ten'),
            (11, 'eleven'), (12, 'twelve') ]

# five sample runs 
for _ in range(5):
    lista = List()
    random.shuffle(records)
    for r in records:
        lista.insert(* r)
    lista.writeOrder()
    lista.writeStructure()
    print("\n" + 10*'-')