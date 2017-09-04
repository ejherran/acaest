from NodoSimple import Node

class ListaSimple:
    
    def __init__(self):
        
        self.head = None
    
    def addStack(self, value):
        
        new = Node()                # Create new
        new.value = value
        
        new.prox = self.head        # New references header
        
        self.head = new             # Header is the new
    
    def addTail(self, value):
        
        new = Node()
        new.value = value
        
        if(self.head == None):
            self.head = new
        else:
            tail = self.getTail()
            tail.prox = new
        
    def getTail(self):
        
        aux = self.head
        while(aux.prox != None):
            aux = aux.prox
        
        return aux
    
    def insert(self, pos, value):
        
        tar = self.search(pos)
        
        if(tar != None):
            
            new = Node()
            new.value = value
            new.prox = tar.prox
            
            tar.prox = new
    
    def delete(self, value):
        
        tar = self.search(value)
        
        if(tar != None):
            
            if(tar == self.head):
                
                self.head = tar.prox
            
            else:
                bef = self.moveToBefore(tar)
                bef.prox = tar.prox
            
            tar.prox = None
            del(tar)
    
    def edit(self, old, new):
        
        tar = self.search(old)
        if(tar != None):
            tar.value = new
    
    def moveToBefore(self, node):
        
        aux = self.head
        
        while(aux.prox != node):
            aux = aux.prox
        
        return aux
    
    def search(self, value):
        
        aux = self.head
        while (aux != None):
            
            if(aux.value == value):
                break
            
            aux=aux.prox 
                
        return aux

    def print(self):
        
        aux = self.head
        
        while(aux != None):
            print(aux.value)
            aux = aux.prox




