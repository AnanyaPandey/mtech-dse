# Implementing a queue

from collections import deque
from typing import ChainMap


class cqueue:
    def __init__(self,size):
        self.Q = [None]*size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def size(self):
        return self.count
    
    def isfull(self):
        return self.size() == self.capacity

    def isempty(self):
        return self.size() ==0 
    
    def enqueue(self,e):
        if self.isfull():
            print("Queue is full, please resize")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = e
            self.count +=1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        else:
            self.Q[self.front] = None
            self.front = (self.front +1) % self.capacity
            self.count -= 1
    
    def front(self):
        if self.isempty():
            print("Queue is empty")
            return       
        else:
            return self.Q[self.front]
    
    def rear(self):
        if self.isempty():
            print("Queue is empty")
            return
        else:
            return self.Q[self.rear]

    def printqueue(self):
        print(self.Q)

if __name__ == '__main__'     :
    myQ = cqueue(10)
    myQ.enqueue(2)
    myQ.enqueue(3)
    myQ.enqueue(4)
    myQ.printqueue()
    myQ.dequeue()
    myQ.dequeue()
    myQ.printqueue() 
    print("Current Queue Size",myQ.size())
    myQ.dequeue()
    print("After deleting Queue Size",myQ.size())
    myQ.enqueue(11)
    myQ.printqueue()   
        



        

