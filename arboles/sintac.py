# -*- coding: utf-8 -*-

import math
import sys

class Node():                                           # Nodo principal
    
    def __init__(self, value):
        
        self.value = value                              # Contenio del nodo
        self.l = None                                   # Referencia al hijo izquierdo
        self.r = None                                   # Referencia al hijo derecho
        self.f = None                                   # Referencia al padre


class MetaArbol:
    
    # Lisas de referencia para los posibles simbolos
    
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "P", "E"]
    binarios = ["+", "-", "/", "*", "^", "r", "l", "%"]
    unarios = ["sin", "cos", "tan", "csc", "sec", "cot", "asin", "acos", "atan", "acsc", "asec", "acot"]
    
    def __init__(self):
        
        self.root = None                                # Raiz del arbol
        self.cmd = None                                 # Lista de ordenes del AST                                   
    
    
    def expand(self, tree):                             # Metodo para expandir el arbol a su maxima amplitud
        
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
    
    
    def toComplete(self, val, tam):                     # Metodo para completar el valor de un nodo a un tamaño fijo    
        
        val = str(val)
        lim = len(val)
        dif = tam-lim
        
        ad = int(dif/2)
        re = dif % 2
        
        val = (" "*re)+(" "*ad)+val+(" "*ad)
        
        return val
    
    
    def draw(self):                                     # Metodo para invocar al proceso de dibujado
        
        self.toDraw(self.root)
    
    
    def toDraw(self, ori):                              # Matodo para dibujar un arbol
        
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
                        dv =  "·"+("·"*y)+dv
                    else:
                        dv =  " "+(" "*y)+dv
                    
                    if(d.r != None):
                        dv = dv+("·"*y)+"·"
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
    
    
    def subir(self, aux):                               # Metodo para subir de nivel en el AST    
        
        while(True):
            
            if(aux.value in self.binarios):
                
                if(aux.f == None or aux.r == None):
                    break
                else:
                    aux = aux.f
            
            elif(aux.value in self.unarios):
                
                if(aux.f == None):
                    break
                else:
                    aux = aux.f
            else:
                break
            
        if(aux.f == None):
            
            t = Node(None)
            t.l = aux
            aux.f = t
            aux = aux.f
        
        return aux
    
    
    def generate(self, equ):                            # Metodo para invocar la creación del AST
        
        self.root = self.create(equ)
    
    
    def create(self, equ):                              # Metodo principal recursivo para crear el AST
        
        ant = ""
        
        aux = None
        error = False
    
        equ = self.toList(equ)
        
        c = 0
        
        while(c < len(equ)):
            
            t = equ[c]

            if(t == "("):
                
                mk = 1
                r = c+1
                sub = ""
                tks = 0
                
                while(True):

                    if(equ[r] == '('):
                        mk = mk+1
                    elif(equ[r] == ')'):
                        mk = mk - 1
                    
                    tks = tks+1
                    sub = sub+equ[r]
                    
                    if((mk == 0) or (r == len(equ)-1)):
                        break
                    else:
                        r = r+1
                
                if(mk == 0):
                    
                    stree = self.create(sub[:-1])
                    c = c + tks

                    if(aux == None):
                        aux = stree
                    elif(aux.l == None):
                        aux.l = stree
                    else:
                        aux.r = stree
                    
                    aux = self.subir(aux)
                    
                else:
                    error = True
                    print("Syntax error!")
                    break
            
            elif(t == ")"):
                
                error = True
                print("Syntax error!")
                break
            
            else:
                
                flag = True
                
                if(t != 'E' and t != 'P'):
                    try:
                        tmp = float(t)
                    except:
                        flag = False
                
                
                if(flag):
                    
                    ant = ""
                    
                    nuevo = Node(t)
                    
                    if(aux != None):
                        
                        if(aux.value in self.unarios):
                            
                            aux.l = nuevo
                            nuevo.f = aux
                            
                            aux = self.subir(aux)
                            
                        
                        elif(aux.value in self.binarios):
                            
                            aux.r = nuevo
                            nuevo.f = aux
                            
                            aux = self.subir(aux)
                        
                        elif(aux.value == None):
                            
                            tmp = Node(None)
                            aux.l = tmp
                            tmp.f = aux
                            
                            aux = aux.l
                            
                            aux.l = nuevo
                            nuevo.f = tmp
                            
                    else:
                        
                        nodo = Node(None)
                        nodo.l = nuevo
                        nuevo.f = nodo
                        
                        aux = nodo
                        
                else:
                    
                    if(ant == "" or (t in self.unarios and ant in self.unarios) or (t in self.unarios and ant in self.binarios) or (t in self.binarios and ant in self.unarios) ):
                        
                        ant = t
                        
                        if(t in self.binarios):
                            
                            aux.value = t
                            
                        elif(t in self.unarios):
                            
                            if(aux == None):
                                nuevo = Node(t)
                                aux = nuevo
                            else:
                                nuevo = Node(t)
                                
                                if(aux.l == None):
                                    aux.l = nuevo
                                else:
                                    aux.r = nuevo
                                
                                nuevo.f = aux
                                aux = nuevo
                                
                    else:
                        
                        error = True
                        print("Syntax error!")
                        break
                        
            c = c+1
        
        
        if(not(error)):

            if(aux.value == None):
                nodo = aux.l
                nodo.f = None
                aux.l = None
                del(aux)
            else:
                nodo = aux
                
            return nodo
        else:
            return None
    
    
    def toList(self, equ):                              # Metodo para convertir texto en una lista de tokens
        
        l = []
        
        par = ""
        num = ""
        
        for c in equ:
            
            if( not (c in self.numeros)):
                
                if(num != ""):
                    
                    l.append(num)
                    num = ""
                
                if(c == "(" or c == ")"):
                    
                    l.append(c)
                
                else:
                    
                    par = par + c
                    
            else:
                num = num + c
        
            if(par in self.unarios or par in self.binarios):
                
                if(par == '-'):
                    
                    if(len(l) == 0):
                        num = num+par
                        par = ''
                    else:
                        last = l[-1]
                        if(last in self.unarios or last in self.binarios or last == '('):
                            num = num+par
                            par = ''
                        else:
                            l.append(par)
                            par = ""
                else:
                    l.append(par)
                    par = ""
        
        if(num != ""):
            l.append(num)
            num = ""
                
        return l    
    
    
    def getPostFix(self):                               # Metodo para obtener los comandos en notacion posfija
        
        if(self.root != None):
            self.cmd = []
            self.pos(self.root)
            
            return(' '.join(self.cmd))
    
    
    def pos(self, node):                                # Metodo recursivo para recorrer el arbol en posfijo
        
        if(node.l != None):
            self.pos(node.l)
        
        if(node.r != None):
            self.pos(node.r)
        
        self.cmd.append(node.value)
    
    
    def exe(self, pre):                                 # Metodo para evaluar la expresion mediante una pila
        
        if(self.cmd != None):
            stack = []
            
            try:
            
                for c in self.cmd:
                    
                    if c in self.binarios:
                        
                        a = float(stack[0])
                        b = float(stack[1])
                        stack = stack[2:]
                        
                        if (c == '+'):
                            a = b+a
                        elif (c == '-'):
                            a = b-a
                        elif (c == '*'):
                            a = b*a
                        elif (c == '/'):
                            a = b/a
                        elif (c == '^'):
                            a = b**a
                        elif (c == 'r'):
                            a = a ** (1/b)
                        elif (c == 'l'):
                            a = math.log(a) / math.log(b)
                        elif (c == '%'):
                            a = b % a
                        
                        stack[0:0] = [a]
                    
                    elif c in self.unarios:
                        
                        a = float(stack[0])
                        stack = stack[1:]
                        
                        if(c == "sin"):
                            a = math.sin(a)
                        elif(c == "cos"):
                            a = math.cos(a)
                        elif(c == "tan"):
                            a = math.tan(a)
                        elif(c == "csc"):
                            a = 1/math.sin(a)
                        elif(c == "sec"):
                            a = 1/math.cos(a)
                        elif(c == "cot"):
                            a = 1/math.tan(a)
                        elif(c == "asin"):
                            a = math.asin(a)
                        elif(c == "acos"):
                            a = math.acos(a)
                        elif(c == "atan"):
                            a = math.atan(a)
                        elif(c == "acsc"):
                            a = math.asin(1/a)
                        elif(c == "asec"):
                            a = (math.pi/2)-math.asin(1/a)
                        elif(c == "acot"):
                            a = (math.pi/2)-math.atan(a)
                        
                        stack[0:0] = [a]
                        
                    else:
                        
                        if(c == 'E'):
                            stack[0:0] = [math.e]
                        elif(c == 'P'):
                            stack[0:0] = [math.pi]
                        else:
                            stack[0:0] = [c]
                    
                return round(stack[0], pre)
                    
            except:
                print("Math error!")
            

def main(args):                                         # Punto de arranque    
    
    try:
        a = MetaArbol()
        
        if(len(args) == 2):
            
            a.generate(args[1])
            print("\n=============================== AST   ==============================\n")
            a.draw()
            print("\n=============================== POST  ==============================\n")
            print(a.getPostFix())
            print("\n=============================== VALUE ==============================\n")
            print(a.exe(4))
            print("\n")
        
        elif(len(args) == 3):
            
            a.generate(args[1])
            print("\n=============================== AST   ==============================\n")
            a.draw()
            print("\n=============================== POST  ==============================\n")
            print(a.getPostFix())
            print("\n=============================== VALUE ==============================\n")
            print(a.exe(int(args[2])))
            print("\n")
            
        else:
            
            print("\nUse: python3 sintac.py \"MATH EXP\" [DEC PRE]\nEJ: python3 sintac.py \"sin(30)/10l89\" 6\n")
            
    except:
        print("\nUse: python3 sintac.py \"MATH EXP\" [DEC PRE]\nEJ: python3 sintac.py \"sin(30)/10l89\" 6\n")
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
