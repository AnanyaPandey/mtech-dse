
# Creating a linked list (single linked list)

class Node:
    def __init__(self,element):
        self.element = element
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head == None

    def length(self):
        n = self.head
        i=1
        while n.next != None:
            n = n.next
            i+=1
        return i

    def traversal(self):
        n = self.head
        if n == None:
            print("Empty list")
        else:
            while n != None:
                print(n.element)
                n = n.next
    
    def insert_at_front(self,e):
        new = Node(e)
        new.next = self.head
        self.head = new
        self.size+=1
    
    def insert_at_end(self,e):
        if self.head == None:
            print("List is empty")
            return
        new = Node(e)
        n = self.head
        while n.next != None:
            n = n.next
        n.next = new
        self.size+=1

    def insert_at_position(self,pos,e):
        if(pos < 1):
            print("\nposition should be >= 1.")
        elif (pos == 1):
            insert_at_end(e)
        elif self.is_empty():
            print("empty list")
            return
        else:
            new = Node(e)
            n = self.head
            for i in range(1,pos-1):
                n = n.next
        new.next = n.next
        n.next = new
        self.size+=1
    
    def deletefront(self):
        if self.head == None:
            print("Empty List")
            return
        self.head = self.head.next
        self.size-=1
    
    def deletelast(self):
        if self.head == None:
            print("Empty List")
            return
        else:
            n = self.head
            while n.next.next != None:
                n = n.next
            lstnode = n.next
            lstnode.next = None
            n.next = None
            self.size-=1

    def deleteposition(self,pos):
        if self.head == None:
            print("Empty List")
            return
        elif pos == 1 :       
            self.deletefront()
        elif pos == self.length():
            self.deletelast()
        else:
            n=self.head
            for i in range(1,pos-1):
                n = n.next
            
            nodetodel = n.next
            n.next = n.next.next
            nodetodel = None 
            # if we delete this it will delete the actual object

    def deleteallnode(self):
        while self.head != None :
            n = self.head
            self.head = self.head.next
            n = None
        print("Deleted all Nodes Succesfully")

    def push(self,e):
        self.insert_at_front(e)
    
    def pop(self):
        self.deletefront()
    
    def top():
        if self.is_empty():
            print("List Empty")
            return
        else:
            return print(self.head.element)