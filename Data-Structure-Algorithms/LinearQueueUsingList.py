# Implement A queue using list
# program to create a queue 

def createqueue():
    queue = []
    return queue

def enqueue(queue,e):
    queue.append(e)
    print("Element entered :",{e})

def isempty(queue):
    if len(queue) == 0:
        return True
    else:
        False
def printqueue(queue):
    print(queue)

def dequeue(queue):
    if isempty(queue):
        print("Empty queue")
        return
    else:
        queue.pop(0)

def front(queue):
    return queue[0]

def rear(queue):
    return queue[-1]

if __name__ == "__main__":
    myQ = createqueue()
    enqueue(myQ,6)
    enqueue(myQ,7)
    enqueue(myQ,9)
    enqueue(myQ,10)
    enqueue(myQ,11)
    front(myQ)
    rear(myQ)
    dequeue(myQ)




