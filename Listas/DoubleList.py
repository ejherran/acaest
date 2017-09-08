from DoubleNode import Node

class DoubleList():
    
    def __init__(self):
        
        self.head = None
        self.tail = None
    
    def add(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.tail = new
        
        else:
            
            new.L = self.head
            self.head.R = new
            
            self.head = new
    
    def search(self, value):
        
        aux = self.head
        while(aux != None):
            if(aux.value == value):
                break
            
            aux = aux.L
        
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
                
                bef = target.R
                
                bef.L = new
                new.R = bef
                
                new.L = target
                target.R = new
                
            else:
                
                self.add(value)
    
    def insertAfter(self, tar, value):
        
        target = self.search(tar)
        
        if(target != None):
            
            new = Node()
            new.value = value
            
            if(target != self.tail):
                
                aft = target.L
                aft.R = new
                new.L = aft
            
            else:
                self.tail = new
                
            target.L = new
            new.R = target
    
    def delete(self, value):
        
        target = self.search(value)
        
        if(target != None):
            
            if(target == self.head):
                
                self.head = self.head.L
                self.head.R = None
            
            elif(target == self.tail):
                
                self.tail = self.tail.R
                self.tail.L = None
            
            else:
                
                bef = target.R
                aft = target.L
                
                bef.L = aft
                aft.R = bef
            
            target.L = None
            target.R = None
            
            del(target)
    
    def printHead(self):
        
        aux = self.head
        while(aux != None):
            print(aux.value)
            aux = aux.L
    
    def printTail(self):
        
        aux = self.tail
        while(aux != None):
            print(aux.value)
            aux = aux.R



