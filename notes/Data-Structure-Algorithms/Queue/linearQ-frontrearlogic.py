# Creating using front rear logic
# Circular Queue

class cqueue:
    def __init__(self,N):
        self.front = -1
        self.rear = -1
        self.Q = [None]*N
        self.N = N
    
    def size(self):
        return (self.N -self.front + self.rear) % self.N
    
    def isempty(self):
        return self.front == self.rear == -1
    
    def front(self):
        if self.isempty():
            print("Queue empty")
            return
        else:
            return self.Q[self.front]
    
    def enqueue(self,e):
        if (self.rear +1) % self.N == self.front:
            print("List is full")
            return
        elif self.front == -1:
            self.front =0
            self.rear = 0
            self.Q[self.rear] = e
        else:
            self.Q[self.rear] = e
            self.rear = (self.rear +1 ) % self.N
                
    def dequeue(self):
        if self.isempty():
            print("Queue empty")
            return
        elif (self.rear == self.front):
            temp = self.Q[self.rear]
            self.rear = None
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.Q[self.front]
            self.front = None           
            self.front = (self.front+1)%self.N
            return temp
            
    def printqueue(self):
        if self.front == -1:
            print("empty list")
            return
        elif self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print(self.Q[i],end=" ")
            print()
        else:
            for i in range(self.front,self.N):
                print(self.Q[i], end=" ")
            for i in range(0,self.rear+1):
                print(self.Q[i],end=" ")
            print()

if __name__ == "__main__":
    myQ = cqueue()
    myQ.enqueue(10)
    myQ.enqueue(20)
    myQ.enqueue(30)
    myQ.enqueue(50)
    print(myQ.size())
    print("Queue:",myQ.printqueue())
    myQ.dequeue()
    myQ.dequeue()
    myQ.dequeue()
    myQ.dequeue()
    myQ.dequeue()
    print("Queue:",myQ.printqueue())
    myQ.enqueue(50)

