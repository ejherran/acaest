# - Class to build a simple circular list.

from SimpleNode import SimpleNode

class SimpleLoopList():
    
    def __init__(self):
        
        self.head = None                             # Master reference to the list header.    
    
    def getBeforeTo(self, tar):
        
        aux = self.head                             # Auxiliary reference for scrolling through the list.
        while(aux.next != tar):
            aux = aux.next                          # Go to the next list item.
        
        return aux
    
    def getLast(self):
        
        aux = self.head
        while(aux.next != self.head):
            aux = aux.next
        
        return aux
    
    def addStack(self, value):
        
        new = SimpleNode()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.head.next = self.head              # The header is linked to itself.
        
        else:
        
            last = self.getLast()                   # Get the last node in the list.
            
            new.next = self.head
            last.next = new                         # The last node in the list links to the new node.
            
            self.head = new                         # The header moves to the new node.
    
    def addTail(self, value):
        
        new = SimpleNode()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.head.next = self.head
        
        else:
            
            last = self.getLast()
            last.next = new
            new.next = self.head
    
    def search(self, value):
        
        aux = self.head
        while(aux.next != self.head):
            if(aux.value == value):
                break
            
            aux = aux.next
        
        if(aux.value == value):                     # Check that the auxiliary contains the target load.
            return aux
        else:
            return None
    
    def edit(self, old, new):
        
        target = self.search(old)                   # Gets the node containing a specified load.
        
        if(target != None):
            target.value = new                      # Updates the node payload.
    
    def insertBefore(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            if(target != self.head):
                
                new = SimpleNode()
                new.value = value
                
                bef = self.getBeforeTo(target)      # Obtains the node immediately preceding the target node.
                
                bef.next = new                      # The previous node links to the new node.
                new.next = target
                
            else:
                
                self.addStack(value)
    
    def insertAfter(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            new = SimpleNode()
            new.value = value
            
            new.next = target.next
            target.next = new
    
    def delete(self, value):
        
        target = self.search(value)
        
        if(target != None):
            
            if(target == self.head):
                self.head = self.head.next          # Save the header by moving it to the next node in the list.
            
            bef = self.getBeforeTo(target)
            bef.next = target.next
            
            target.next = None                      # Break the node link.
            del(target)                             # Deletes the node from memory.
    
    def print(self):
        
        aux = self.head
        
        while(True and aux != None):
            print(aux.value)
            aux = aux.next
            
            if(aux == self.head):
                break
