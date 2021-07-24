
## Creating and implementing Stack with some functions
## Using pythons in built list to create a stack
class stack:

    def __init__(self):
        self.size = 0
        self.top = None
        self.data=[]
    
    def push(self,val):
        self.data.append(val)
    
    def pop(self):
        deleted = self.data[-1]
        del self.data[-1]

    def __len__(self):
        return (len(self.data))

    
if name == __main__:
    print("executing file")




