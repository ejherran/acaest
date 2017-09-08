from SimpleNode import Node

class SimpleList():
    
    def __init__(self):
        
        self.head = None
    
    def getBeforeTo(self, tar):
        
        aux = self.head
        while(aux.next != tar):
            aux = aux.next
        
        return aux
    
    def getLast(self):
        
        aux = self.head
        while(aux.next != None):
            aux = aux.next
        
        return aux
    
    def addStack(self, value):
        
        new = Node()
        new.value = value
        
        new.next = self.head
        
        self.head = new
    
    def addTail(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
        
        else:
            
            last = self.getLast()
            last.next = new
    
    def search(self, value):
        
        aux = self.head
        while(aux != None):
            if(aux.value == value):
                break
            
            aux = aux.next
        
        return aux
    
    def edit(self, old, new):
        
        target = self.search(old)
        
        if(target != None):
            target.value = new
    
    def insertBefore(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            if(target != self.head):
                
                new = Node()
                new.value = value
                
                bef = self.getBeforeTo(target)
                
                bef.next = new
                new.next = target
                
            else:
                
                self.addStack(value)
    
    def insertAfter(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            new = Node()
            new.value = value
            
            new.next = target.next
            target.next = new
    
    def delete(self, value):
        
        target = self.search(value)
        
        if(target != None):
            
            if(target == self.head):
                self.head = self.head.next
            else:
                
                bef = self.getBeforeTo(target)
                bef.next = target.next
            
            target.next = None
            del(target)
    
    def print(self):
        
        aux = self.head
        while(aux != None):
            print(aux.value)
            aux = aux.next


