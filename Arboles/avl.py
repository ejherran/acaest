import sys
import math

class Node:
    
    def __init__(self, value):
        
        self.value = value              # Carga del node
        
        self.pl = 0                     # Profundidad izquierda
        self.pr = 0                     # Profundidad derecha
        
        self.f = None                   # Nodo padre
        self.l = None                   # Rama izquierda
        self.r = None                   # Rama derecha
    
    def getMaxPro(self):
        
        if(self.pl > self.pr):
            return self.pl + 1
        else:
            return self.pr + 1


class AvlTree:
    
    
    def __init__(self):
        
        self.root = None                # Raiz del arbol
        self.needBalance = True         # Bandera de control para balancear
    
    
    def updatePro(self, tree):
        
        p = 0
        
        if(tree != None):
            
            pl = self.updatePro(tree.l) + 1
            pr = self.updatePro(tree.r) + 1
            
            if(pl > pr):
                p = pl
            else:
                p = pr
            
            tree.pl = pl-1
            tree.pr = pr-1
        
        return p
    
    
    def add(self, value):
        
        nuevo = Node(value)
        
        self.addNode(nuevo)
    
    
    def addNode(self, node):
        
        if(self.root == None):
            self.root = node
        else:
            self.addRecursive(self.root, node)
        
        self.launchBalance()
    
    
    def addRecursive(self, tree, nue):
        
        if(nue.value < tree.value):
            
            if(tree.l == None):
                tree.l = nue
                nue.f = tree
            else:
                self.addRecursive(tree.l, nue)
        
        if(nue.value > tree.value):
            
            if(tree.r == None):
                tree.r = nue
                nue.f = tree
            else:
                self.addRecursive(tree.r, nue)
    
    
    def launchBalance(self):
        
        self.updatePro(self.root)
        
        self.needBalance = True
        
        while(self.needBalance):
            
            self.needBalance = False
            self.doBalance(self.root)
    
    
    def doBalance(self, tree):
        
        if(tree != None):
            
            fl = self.doBalance(tree.l)
            fr = self.doBalance(tree.r)
            
            if(fl and fr):
                
                if( abs(tree.pl-tree.pr) > 1):
                    
                    self.needBalance = True
                    
                    if(tree.pl > tree.pr):
                        
                        if(tree.l.pl > tree.l.pr):
                            self.rotRight(tree)
                        else:
                            self.doubleRotRight(tree)
                        
                    else:
                        
                        if(tree.r.pr > tree.r.pl):
                            self.rotLeft(tree)
                        else:
                            self.doubleRotLeft(tree)
                    
                    return False
                
                else:
                    
                    return True
            
            else:
                
                return False
        
        else:
        
            return True

    
    def rotLeft(self, node):
        
        print("> ROTLEFT", node.value)
        
        father = node.f
        
        node.f = None
        
        aux = node.r
        node.r = None
        aux.f = father
        
        if(father != None):
            if(father.l == node):
                father.l = aux
            else:
                father.r = aux
        else:
            self.root = aux
        
        while(aux.l != None):
            aux = aux.l
        
        aux.l = node
        node.f = aux
        
        self.updatePro(self.root)
    
    
    def rotRight (self, node):
        
        print("> ROTRIGHT", node.value)
        
        father = node.f
        node.f = None
        
        aux = node.l
        node.l = None
        aux.f = father
        
        if(father != None):
            if(father.l == node):
                father.l = aux
            else:
                father.r = aux
        else:
            self.root = aux
        
        while(aux.r != None):
            aux = aux.r
        
        aux.r = node
        node.f = aux
        
        self.updatePro(self.root)
    
    
    def doubleRotLeft(self, tree):
        
        self.rotRight(tree.r)
        self.rotLeft(tree)
    
    
    def doubleRotRight(self, tree):
        
        self.rotLeft(tree.l)
        self.rotRight(tree)


    def getNode(self, val):
        
        tail = [self.root]
        
        res = None
        
        while(len(tail) > 0):
            
            res = tail[0]
            tail = tail[1:]
            
            if(res.value == val):
                break
            else:
                
                if(res.l != None):
                    tail.append(res.l)
                
                if(res.r != None):
                    tail.append(res.r)
                
                res = None
                
        return res
    
    
    def getListNodes(self, node):
        
        tail = [node]
        
        res = []
        
        while(len(tail) > 0):
            
            tmp = tail[0]
            tail = tail[1:]
               
            if(tmp.l != None):
                tail.append(tmp.l)
            
            if(tmp.r != None):
                tail.append(tmp.r)
            
            res.append(tmp)
                
        return res
    
    
    def delNode(self, val):
        
        node = self.getNode(val)
        
        if(node == None):                           # Si no existe el nodo a eliminar
            return -1
        
        elif(node.l == None and node.r == None):    # Si se elimina una hoja
            
            aux = node.f
            
            if(aux != None):
                if(aux.l == node):
                    aux.l = None
                else:
                    aux.r = None
            else:
                self.root = None
            
            node.f = None
            del(node)
            
            self.launchBalance()
            
            return 0
        
        elif(node == self.root):    # Si elimina la raiz
            
            cl = node.l             # Hijo Izq
            cr = node.r             # Hijo Der
            
            self.root.l = None
            self.root.r = None
            del(self.root)
            
            if(cl.getMaxPro() > cr.getMaxPro()):
                
                self.root = cl
                
                cl.f = None
                tmp = cl
                
                while(tmp.r != None):
                    tmp = tmp.r
                
                tmp.r = cr
                cr.f = tmp
            
            else:
                
                self.root = cr
                
                cr.f = None
                tmp = cr
                
                while(tmp.l != None):
                    tmp = tmp.l
                
                tmp.l = cl
                cl.f = tmp
            
            self.launchBalance()
            
            return 0
        
        else:
            
            aux = node.f
            
            cl = node.l
            cr = node.r
            
            pcl = 0
            pcr = 0
            
            if(cl != None):
                pcl = cl.getMaxPro()
            
            if(cr != None):
                pcr = cr.getMaxPro()
            
            if(pcl > pcr):
                
                cl.f = aux
                
                if(aux.l == node):
                    aux.l = cl
                else:
                    aux.r = cl
                
                tmp = cl 
                while(tmp.r != None):
                    tmp = tmp.r
                
                tmp.r = cr
                
                if(cr != None):
                    cr.f = tmp
            
            else:
                
                cr.f = aux
                
                if(aux.l == node):
                    aux.l = cr
                else:
                    aux.r = cr
                
                tmp = cr 
                while(tmp.l != None):
                    tmp = tmp.l
                
                tmp.l = cl
                
                if(cl != None):
                    cl.f = tmp
            
            node.f = None
            node.l = None
            node.r = None
            del(node)
            
            self.launchBalance()
            return 0
    
    
    def editNode(self, ov, nv):
        
        exist = self.getNode(nv)
        
        if(exist == None):
            node = self.getNode(ov)
            
            if(node != None):
                
                if(node == self.root or (node.l == None and node.r == None)):
                    
                    self.movEdit(node, nv)
                    return 0
                
                else:
                    
                    if( (node.value < self.root.value and nv < self.root.value) or (node.value > self.root.value and nv > self.root.value)):
                        
                        self.fullEdit(node, nv)
                        return 0
                        
                    else:
                        
                        self.movEdit(node, nv)
                        return 0
                    
            else:
                
                return -1
        else:
            
            return 1
    
    
    def movEdit(self, node, nv):
        
        node.value = nv
        self.launchEcua(self.root)
        

    def fullEdit(self, node, nv):
        
        node = self.cutNode(node)
        node.value = nv
        self.launchEcua(node)
        
        self.addNode(node)
    
    
    def launchEcua(self, node):
        
        l = self.getListNodes(node)
        
        while(True):
            
            c = 0
            
            for n in l:
                
                c = c + self.ecuTree(n)
            
            if(c == 0):
                break    
            else:
                print("> NODES MOVED:", c)
        
    
    def ecuTree(self, node):
        
        cnt = 0
        
        fat = node.f
        tmp = node
        
        while(fat != None):
            
            if( ((fat.l == tmp) and (node.value > fat.value)) or((fat.r == tmp) and (node.value < fat.value)) ):
                
                tpv = fat.value
                fat.value = node.value
                node.value = tpv
                
                cnt = cnt+1
                
                cnt = cnt + self.ecuTree(fat)
            
            else:
                
                tmp = fat
                fat = fat.f
        
        cl = node.l
        
        if(cl != None):
            
            if( cl.value > node.value):
                
                tpv = cl.value
                cl.value = node.value
                node.value = tpv
                
                cnt = cnt + 1
                
                cnt = cnt + self.ecuTree(cl)
        
        cr = node.r
        
        if(cr != None):
            
            if( cr.value < node.value):
                
                tpv = cr.value
                cr.value = node.value
                node.value = tpv
                
                cnt = cnt+1
                
                cnt = cnt + self.ecuTree(cr)
        
        return cnt
    
    
    def cutNode(self, node):
        
        aux = node.f
        
        node.f = None
        
        if(aux.l == node):
            aux.l = None
        else:
            aux.r = None
        
        return node
    
    
    def preOrder(self): 
        self.pre(self.root)
        
    
    def pre(self, tree):
        if(tree != None):
            print("(",tree.value, ",", tree.pl, ",", tree.pr, ")")
            self.pre(tree.l)
            self.pre(tree.r)
    
    
    def inOrder(self):
        self.ino(self.root)
    
        
    def ino(self, tree):
        if(tree != None):
            self.ino(tree.l)
            print("(",tree.value, ",", tree.pl, ",", tree.pr, ")")
            self.ino(tree.r)
    
    
    def posOrder(self):
        self.pos(self.root)
    
    
    def pos(self, tree):
        if(tree != None):
            self.pos(tree.l)
            self.pos(tree.r)
            print("(",tree.value, ",", tree.pl, ",", tree.pr, ")")

    
    def expand(self, tree):
        
        if(tree != None):
            c = 1
            tail = [tree]
            res = []
            
            while(c > 0):
                
                node = tail[0]
                tail = tail[1:]
                
                if(node.value != None):
                    c = c-1
                
                res.append(node)
                
                if(node.l != None):
                    tail.append(node.l)
                    c = c+1
                else:
                    tail.append(Node(None))
                
                if(node.r != None):
                    tail.append(node.r)
                    c = c+1
                else:
                    tail.append(Node(None))
            
            base = int(math.log(len(res)+1) / math.log(2))
            sob = len(res) - ((2 ** base)-1) 
            
            if(sob > 0):
                base = base+1
            
            lim = (2**base)-1
            
            while(len(res) < lim):
                res.append(Node(None))
            
            return res
        
        else:
            return []
    
    
    def toComplete(self, val, tam):
        
        val = str(val)
        lim = len(val)
        dif = tam-lim
        
        ad = int(dif/2)
        re = dif % 2
        
        val = (" "*re)+(" "*ad)+val+(" "*ad)
        
        return val
    
    
    def draw(self):
        
        self.toDraw(self.root)
    
    
    def toDraw(self, ori):
        
        datos = self.expand(ori)
        
        niv = len(datos)+1
        niv = int(math.log(niv) / math.log(2))
        
        tam = 3
        
        for d in datos:
            
            if(d.value != None):
                
                l = len( str(d.value) )
                
                if(l > tam):
                    tam = l
        
        if (tam % 2 == 0):
            tam = tam + 1
        
        row = (2 ** niv) - 1
        trow = row * tam
        
        for i in range(niv):
            
            h = int( ((2 ** niv) - (2 ** (i + 1))) / (2 ** i) / 2)
            c = (2 ** i)
            s = row - (2*h) - c
            
            if(c > 1):
                s = int( s / (c-1) )
            
            h = h*tam
            s = s*tam
            y = int((h-1)/2)
            
            linea = []
            poste = []
            
            for j in range( (2**i)-1, (2**(i+1))-1 ):
                
                d = datos[j]
                
                if(d.value == None):
                    dv = self.toComplete(" ", tam)
                else:
                    dv = self.toComplete(d.value, tam)
                
                if(d.l != None):
                    poste.append("|")
                else:
                    poste.append(" ")
                
                if(i < (niv-1)):
                    
                    if(d.l != None):
                        dv =  "+"+("-"*y)+dv
                    else:
                        dv =  " "+(" "*y)+dv
                    
                    if(d.r != None):
                        dv = dv+("-"*y)+"+"
                    else:
                        dv = dv+" "+(" "*y)
                    
                linea.append(dv)
                
                if(d.r != None):
                    poste.append("|")
                else:
                    poste.append(" ")
            
            if(i < (niv-1)):
                print( (" "*y) + ( ( " " * ( s - (2 * y) - 2 ) ) .join(linea)) + (" "*y) )
                print( (" "*y) + ( (" " * ((2*y) + tam) ).join(poste) ) + (" "*y) )
            else:
                print( (" "*s).join(linea) )



def main(args):
    
    a = AvlTree()

    while(True):
        
        try:
            
            o = int(input("1 - Add | 2 - Del | 3 - Edit\nOption?: "))
            
            if(o in [1, 2, 3]):
                
                if(o == 1):
                
                    v = float(input("\nNew value?: "))
                
                    print("\n====================  ACTIONS  ====================")
                    a.add(v)
                
                elif(o == 2):
                    
                    v = float(input("\nNode to delete?: "))
                
                    print("\n====================  ACTIONS  ====================")
                    
                    r = a.delNode(v)
                    
                    if(r == 0):
                        print("\n\n>> Node deleted! <<\n")
                    else:
                        print("\n\n>> Error! <<\n")
                
                elif(o == 3):
                    
                    v = float(input("\nNode to edit?: "))
                    n = float(input("New value?: "))
                
                    print("\n====================  ACTIONS  ====================")
                    
                    r = a.editNode(v, n)
                    
                    if(r == 0):
                        print("\n\n>> Node edited! <<\n")
                    else:
                        print("\n\n>> Error! <<\n")
                    
                    
                print("\n====================  INORDER  ====================")
                a.inOrder()
                
                print("\n====================   SHAPE   ====================")
                a.draw()
            
            else:
                
                print("\n\n>> Invalid Option! <<\n")
            
            print("\n\n")
        
        except:
            
            print("\n\nEND!.")
            break
    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
