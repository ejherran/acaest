from NodoDoble import Node

class ListaDoble:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
    
    def addFordward(self, value):
        
        new = Node()
        new.value = value
        
        if(self.tail == None):
            
            self.head = new
            self.tail = new
        
        else:
            
            self.tail.R = new
            new.L = self.tail
            self.tail = new
    
    def addBackward(self, value):
        
        new = Node()
        new.value = value
        
        if(self.tail == None):
            
            self.head = new
            self.tail = new
        
        else:
            
            self.head.L = new
            new.R = self.head
            self.head = new
        
    
    def print(self):
        
        aux = self.head
        
        while(aux != None):
            print(aux.value)
            aux = aux.R


l = ListaDoble()
#l.addFordward(1)
#l.addFordward(2)
#l.addFordward(3)
#l.addFordward(4)
#l.print()
print("==========")
l.addBackward(10)
l.addBackward(11)
l.addBackward(12)
l.print()
