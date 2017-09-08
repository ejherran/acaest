from DoubleNode import Node

class DoubleLoopList():
    
    def __init__(self):
        
        self.head = None
        self.tail = None
    
    def add(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.tail = new
            
            self.head.R = self.tail
            self.tail.L = self.head
            
        else:
            
            new.L = self.head
            self.head.R = new
            
            new.R = self.tail
            self.tail.L = new
            
            self.head = new
    
    def search(self, value):
        
        aux = self.head
        while(aux.L != self.head):
            if(aux.value == value):
                break
            
            aux = aux.L
        
        if(aux.value == value):
            return aux
        else:
            return None
    
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
                self.head.R = self.tail
                
            target.L = new
            new.R = target
    
    def delete(self, value):
        
        target = self.search(value)
        
        if(target != None):
            
            if(target == self.head):
                
                self.head = self.head.L
                self.head.R = self.tail
                self.tail.L = self.head
            
            elif(target == self.tail):
                
                self.tail = self.tail.R
                self.tail.L = self.head
                self.head.R = self.tail
            
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
