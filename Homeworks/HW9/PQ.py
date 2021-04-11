"""
PQ.py - implementing a priority queue for topological sort (specifically implementing lower())
Date - -04/12/21 
Author - Daniel Throop + Dr. Thomas Schwarz 
Class - COSC 3100

"""

import random 

class Gl:
    INFTY = 2**32-1

class Vertex:
    def __init__(self, x, val = Gl.INFTY):
        self.id = x
        self.degree = val
    def __str__(self):
        return '({},{})'.format(self.id, self.degree)
    def __eq__(self, other):
        return self.degree == other.degree
    def __le__(self, other):
        return self.degree <= other.degree
    def __lt__(self, other):
        return self.degree < other.degree
    def __gt__(self, other):
        return self.degree > other.degree
    def __ne__(self, other):
        return self.degree != other.degree
    def __ge__(self, other):
        return self.degree >= other.degree
    def assign(self, val):
        self.degree = val

class PQ:
    def __init__(self):
        self.array = []
    def up(index):
        return (index+1)//2-1
    def left(index):
        return 2*index + 1
    def right(index):
        return 2*index + 2
    def __str__(self):
        return 'Contents\n'+'\n'.join([str(x) for x in self.array])+'\n'
    def __len__(self):
        return len(self.array)
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        try:
            ret_val = self.array[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return ret_val

    def test_heap(self):
        for i in range(1, len(self.array)):
            if self.array[i] < self.array[PQ.up(i)]:
                return False
        return True

    def insert(self, value):
        n = len(self.array)
        self.array.append(value)
        while n>0:
            parent = PQ.up(n)
            if self.array[parent] > value:
                self.array[n], self.array[parent] = self.array[parent], self.array[n] 
                n = parent
            else:
                return

    def pop(self):
        ret_val = self.array[0]
        if len(self.array) == 1:
            del self.array[-1]
            return ret_val
        last = self.array[-1]
        del self.array[-1]
        self.array[0] = last
        n=0
        while n < len(self.array):
            left = PQ.left(n)
            right = PQ.right(n)
            if right < len(self.array): # current node has two children
                if self.array[n] <= self.array[left] and self.array[n] <= self.array[right]:
                    return ret_val
                if self.array[left] >= self.array[right]:
                    m = right
                else:
                    m = left
                self.array[n], self.array[m] = self.array[m], self.array[n] 
                n = m
            elif left < len(self.array): # current node has one child
                if self.array[n] > self.array[left]:
                    self.array[n], self.array[left] = self.array[left], self.array[n]
                return ret_val
            else:  # current node has no child
                return ret_val
        return ret_val

    def find(self, vertex_number):
        for i in range(len(self.array)):
            if self.array[i].id == vertex_number:
                return i

    # def of interest
    def lower(self, vertex_number, new_degree):
        # find the vertex's index
        i = self.find(vertex_number)
        # check if new_degree is valid
        if(new_degree < self.array[i].degree and new_degree >= 0):
            # assign new degree
            self.array[i].assign(new_degree)
            # determine if the parent has higher priority
            while i>0:
                parent = PQ.up(i)
                if self.array[parent] > self.array[i]:
                    self.array[i], self.array[parent] = self.array[parent], self.array[i] 
                    i = parent
                else:
                    return
        else:
            print("Error: Invalid new degree.")

# testing 
# this version of the gen_ran() method generates nr verticies and then lowers n//2 of them by degree 3
def gen_ran(nr):
    insertions = {}
    pq = PQ()
    for i in range(nr):
        degree = random.randint(0,12)
        insertions[i] = degree
        pq.insert(Vertex(i, degree))
    # print original values
    print(pq.__str__())
    # lower some values
    for j in range(nr//2):
        index = random.randint(0, (nr-1))
        lowDegree = insertions[index]
        # lower the degree of random verticies by 3
        if(lowDegree - 3 >= 0):
            pq.lower(index, lowDegree - 3)
            print("Lowered: ({},{})".format(index, lowDegree))
    print("\n")
    return pq

testPQ = PQ()
testPQ = gen_ran(10)
# print the new lowered graph
print(testPQ)
# determine if the lower graph is still valid 
print(testPQ.test_heap())











           