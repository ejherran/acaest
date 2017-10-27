# -*- coding: utf-8 -*-

import sys
import pickle

class Nodo:

    def __init__(self):                         # Nodo principal

        self.peso = -1                          # Peso del simbolo
        self.simbolo = None                     # Simbolo a codificar

        self.l = None                           # Hijo izquierdo Tag: 0
        self.r = None                           # Hijo derecho Tag: 1
        self.f = None                           # Padre


class Huffman():                                # Clase principal
    
    def __init__(self):
        
        self.apa = None                         # Contenedor de apariciones de los simbolos
        self.codigos = None                     # Contenedor de los codigos prefijos
        self.meta = None                        # Contenedor de los metadatos de compresion          
    
    
    def getCodes(self, path):                   # Metodo para calcular los codigos prefijos
        
        self.apa = {}
        
        i = open(path, "rb")

        while(True):
            
            b = i.read(1)
            
            if b != b'':
                
                if( b in self.apa.keys()):
                    self.apa[b] = self.apa[b]+1
                else:
                    self.apa[b] = 1

            else:
                break

        i.close()

        self.apa = list(self.apa.items())
        
        for i in range(0, len(self.apa)-1):
            
            for j in range(0, len(self.apa)-(i+1)):
                
                if(self.apa[j][1] > self.apa[j+1][1]):
                    
                    t = self.apa[j]
                    self.apa[j] = self.apa[j+1]
                    self.apa[j+1] = t

        i = 0
        z = len(self.apa)
        
        while(i < z):
        
            nuevo = Nodo()
            nuevo.peso = self.apa[i][1]
            nuevo.simbolo = self.apa[i][0]
            self.apa[i] = nuevo

            i = i + 1

        hojas = []

        while(len(self.apa) > 1):
            
            a = self.apa[0]
            b = self.apa[1]
            
            peso = a.peso + b.peso
            
            nuevo = Nodo()
            nuevo.peso = peso
            nuevo.l = a
            nuevo.r = b
            
            a.f = nuevo
            b.f = nuevo
            
            if a.simbolo != None:
                hojas.append(a)
            
            if b.simbolo != None:
                hojas.append(b)
            
            self.apa = self.apa[2:]

            i = 0
            while(i < len(self.apa)):
                
                if(nuevo.peso >= self.apa[i].peso):
                    i = i+1
                else:
                    break

            self.apa[i:i] = [nuevo]
            

        arbol = self.apa[0]
        del(self.apa)

        self.codigos = {}

        for h in hojas:
            
            cod = ''
            aux = h
            
            while(aux.f != None):
                p = aux.f
                
                if(p.l == aux):
                    cod = "0"+cod
                else:
                    cod = "1"+cod
                
                aux = aux.f
            
            self.codigos[h.simbolo] = (cod, h.peso)
        
        del(arbol)
        
        self.meta = {}
        for e in self.codigos.items():
            self.meta[e[1][0]] = e[0]
    
    
    def compress(self, path):                   # Metodo para comprimir
        
        self.getCodes(path)
        
        i = open(path, "rb")
        o = open(path+".huf", "wb")
        
        pickle.dump(self.meta, o)
        
        buf = ""
        while(True):
            
            b = i.read(1)
            if b != b'':
                
                buf = buf + self.codigos[b][0]
                
                while(len(buf) >= 8):
                    val = buf[0:8]
                    val = int(val, 2)
                    val = bytes([val])
                    o.write(val)
                    
                    buf = buf[8:]

            else:
                break

        if(len(buf) > 0):
            pk = ""

            if("0" in self.meta.keys()):
                pk = "1"
            else:
                pk = "0"

            dif = 8-len(buf)
            buf = buf+(pk*dif)

            print("\nOk File Compressed.\nExcedente de compresion: ", pk*dif,"\n")
            buf = int(buf, 2)
            o.write(bytes([buf]))

        i.close()
        o.close()
    
    
    def decompress(self, path):                 # Metodo para descomprimir
        
        sl = path.split(".")
        sl = sl[:-1]
        sl = '.'.join(sl)
        
        k = open(path,"rb")
        q = open(sl, "wb")
        head = pickle.load(k)
        
        buf = ""
        flag = True
        
        while(True):
            
            if(flag):
                
                b = k.read(1)
                
                if b != b'':
                
                    flag = False
                    
                    b = ord(b)
                    b = bin(b)
                    b = b.split("b")[1]
                    b = ("0"*(8-len(b)))+b
                    
                    buf = buf + b
                    
                else:
                    
                    break
                    
            else:
                
                l = 1
                while(l <= len(buf)):
                    
                    p = buf[0:l]
                    
                    if p in head.keys():
                    
                        q.write(head[p])
                        buf = buf[l:]
                        l = 1
                    
                    else:
                    
                        l = l+1
                
                flag = True
        
        print("\nOk File Decompressed.")
        
        if(len(buf) > 0):
            print("Excedente de descompresion: ", buf, "\n")
        else:
            print("\n")
        
        k.close()
        q.close()


def main(args):                                         # Punto de arranque    
    
    try:
        
        h = Huffman()
        
        if(len(args) == 3):
            
            if(args[1] == '-c'):
                h.compress(args[2])
                
            elif(args[1] == '-d'):
                h.decompress(args[2])
                
            else:
                print("\nUse: python3 comp.py -c [FILE] # To compress\nUse: python3 comp.py -d [FILE] # To decompress\n")
        else:
            
            print("\nUse: python3 comp.py -c [FILE] # To compress\nUse: python3 comp.py -d [FILE] # To decompress\n")
            
    except:
        
        print("\nUse: python3 comp.py -c [FILE] # To compress\nUse: python3 comp.py -d [FILE] # To decompress\ns")
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
