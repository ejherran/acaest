from NodoSimple import Node

class ListaCircularSimple:
    
    def __init__(self):
        
        self.head = None
    
    def addStack(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.head.prox = self.head
        
        else:
            
            new.prox = self.head
            
            last = self.getLast()
            last.prox = new
            
            self.head = new
    
    def addTail(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            
            self.head = new
            self.head.prox = self.head
        
        else:
            
            last = self.getLast()
            last.prox = new
            
            new.prox = self.head
    
    def getLast(self):
        
        aux = self.head
        
        while(aux.prox != self.head):
            aux = aux.prox
        
        return aux
    
    def insert(self, pos, value):
        
        tar = self.search(pos)
        
        if(tar != None):
            
            new = Node()
            new.value = value
            new.prox = tar.prox
            
            tar.prox = new
    
    def edit(self, old, new):
        
        tar = self.search(old)
        if(tar != None):
            tar.value = new
    
    def search(self,value):
        
        aux=self.head
        while(aux.prox != self.head):
            if(aux.value == value):
                break
            aux=aux.prox
        
        if(aux.value != value):
            return None 
        else:
            return aux
    
    def moveToBefore(self, node):
        
        aux = self.head
        
        while(aux.prox != node):
            aux = aux.prox
        
        return aux
    
    def delete(self, value):
        
        tar = self.search(value)
        
        if(tar != None):
            
            if(tar == self.head):
                
                last=self.getLast ()
                self.head = tar.prox
                last.prox=self.head
                
            else:
                
                bef = self.moveToBefore(tar)
                bef.prox = tar.prox
            
            tar.prox = None
            del(tar)
    
    def print(self):
        
        aux = self.head
        
        while(True):
            
            print(aux.value)
            
            if(aux.prox == self.head):
                break
            else:
                aux = aux.prox

