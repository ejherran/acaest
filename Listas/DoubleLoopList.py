# - Class to create a double-linked circular list.

from DoubleNode import DoubleNode

class DoubleLoopList():
    
    def __init__(self):
        
        self.head = None                            # Master reference to the first item in the list
        self.tail = None                            # Master reference the last item in the list.
    
    def add(self, value):                           # Add elements in stack format.
        
        new = DoubleNode()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.tail = new
            
            self.head.R = self.tail                 # Links the header to the queue in the list.
            self.tail.L = self.head                 # Link the list queue to the header.
            
        else:
            
            new.L = self.head                       # Cross references: L for the next, R for the previous. 
            self.head.R = new
            
            new.R = self.tail
            self.tail.L = new
            
            self.head = new                         # The header moves to the new node.
    
    def search(self, value):
        
        aux = self.head                             # Auxiliary reference for scrolling through the list.
        while(aux.L != self.head):
            if(aux.value == value):
                break
            
            aux = aux.L                             # Go to the next list item.
        
        if(aux.value == value):
            return aux
        else:
            return None
    
    def edit(self, old, new):                       # Gets the node containing a specified load.
        
        target = self.search(old)
        
        if(target != None):
            target.value = new                      # Updates the node payload.
    
    def insertBefore(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            if(target != self.head):
                
                new = DoubleNode()
                new.value = value
                
                bef = target.R                      # Obtains the node immediately preceding the target node.
                
                bef.L = new                         # Cross references.
                new.R = bef
                
                new.L = target
                target.R = new
                
            else:
                
                self.add(value)
    
    def insertAfter(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            new = DoubleNode()
            new.value = value
            
            if(target != self.tail):
                
                aft = target.L                      # Retrieves the node immediately following.        
                aft.R = new
                new.L = aft
            
            else:
                
                self.tail = new
                self.head.R = self.tail
                
            target.L = new
            new.R = target
    
    def delete(self, value):
        
        target = self.search(value)
        
        if(target != None):
            
            if(target == self.head):
                
                self.head = self.head.L             # Save the header by moving it to the next node in the list.
                self.head.R = self.tail             # Updates the double link to the list queue.
                self.tail.L = self.head
            
            elif(target == self.tail):
                
                self.tail = self.tail.R             # Save the queue by moving it to the previous node.
                self.tail.L = self.head             # Update the double link to the list header.
                self.head.R = self.tail
            
            else:
                
                bef = target.R
                aft = target.L
                
                bef.L = aft
                aft.R = bef
            
            target.L = None                         # Break the node links.
            target.R = None
            
            del(target)                             # Deletes the node from memory.
    
    def printHead(self):
        
        aux = self.head
        
        while(True and aux != None):
            
            print(aux.value)
            aux = aux.L
            
            if(aux == self.head):
                break
    
    def printTail(self):
        
        aux = self.tail
        
        while(True and aux != None):
            
            print(aux.value)
            aux = aux.R
            
            if(aux == self.tail):
                break
