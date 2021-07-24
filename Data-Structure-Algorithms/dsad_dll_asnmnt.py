class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Create the doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def listWrite(self,filen):
        temp = self.head
        allNodes = ""
        if(temp != None):
            while (temp is not None):
                allNodes = allNodes + " " + temp.data
                temp = temp.next
            allNodes = allNodes + "\n"
            filen.writelines(allNodes)
            print(allNodes)
            
        else:
            print("The list is empty.")

    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode         
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
        
    def addAtPosition(self, pos, NewVal) :
        CurPos = 1
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next != None and CurPos < pos):
            last = last.next
            CurPos = CurPos + 1
            
        if last.next is not None :
            NewNode.next = last.next
            NewNode.prev = last
            last.next = NewNode
        else :
            self.append( NewVal)

    def flipPosition(self, noOfPeople ,startPos) :
        temp = None
        i = 1
        current = self.head
        if current is None or current.next is None:
            print("List is empty")
            return
        # Swap next and prev for all nodes of
        # doubly linked list
        pos = 1
        startNode = current
        # print("traverse node to point it to start position ")
        while startNode is not None and pos < startPos :
            startNode = startNode.next
            pos = pos + 1
        # print("traverse node completed ")
        current = startNode

        while current is not None and i < noOfPeople :
            current = current.next
            tail = current
            i = i + 1
        current = startNode
        i = 1
        while current is not None and i < noOfPeople :
            idata = current.data
            current.data = tail.data
            tail.data = idata
            tail = tail.prev
            current = current.next
            i = i + 1
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev
        
        return
    def remove(self, position):     
        if(position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
            if (self.head != None):
                self.head.prev = None
            return
            
        else:
            temp = self.head
            i = 1
            while i < position-1 :
                i = i + 1
                if(temp != None):
                    temp = temp.next
            if(temp.next != None):
                nodeToDelete = temp.next
                nodeToDelete.next.prev = temp
                temp.next = nodeToDelete.next
                nodeToDelete.prev = None
                nodeToDelete.next = None

            if(temp.next == None):
                print("\nThe node is already null.")
        return

if __name__ == '__main__':
    file = open('inputPS4.txt', 'r')
    opfile = open('outputPS4.txt', 'w')

    Lines = file.readlines()
    dllist = DoublyLinkedList() 
    for ln in Lines:
        line = ln.strip()
        opCode = line.split('::')
        if opCode[0] == "add_at_start" :
            dllist.push(opCode[1])
            dllist.listWrite(opfile)
        if opCode[0] == "add_at_end" :
            dllist.append(opCode[1])
            dllist.listWrite(opfile)
        if opCode[0] == "add_at_pos" and int(opCode[1]) == 1 :
            dllist.push(opCode[2])
            dllist.listWrite(opfile)
        if opCode[0] == "add_at_pos" and int(opCode[1]) > 1 :
            dllist.addAtPosition(int(opCode[1])-1,opCode[2])
            dllist.listWrite(opfile)
        if opCode[0] == "remove_people" :
            for i in range(0,int(opCode[1])):
                dllist.remove(int(opCode[2]))
            dllist.listWrite(opfile)
        if opCode[0] == "flip_order" and int(opCode[1]) > 1 :
            dllist.flipPosition(int(opCode[1]),int(opCode[2]))
            dllist.listWrite(opfile)
    
    opfile.close()
    file.close()
    
    

        
