from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt
import sys

class Laberinto(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.nodos = []
        self.aristas = []
        self.estado = 0         # 0 - Normal, 1 - Agarrar
        self.target = None
        
        self.crear()
    
    def crear(self):
        
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Test")
        self.setMouseTracking(True)
        self.show()
    
    def paintEvent(self, e):
        
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.white)
        qp.setBrush(Qt.black)
        
        qp.drawRect(0,0,800,600)
        
        qp.setBrush(Qt.white)
        
        a = open("mapa.txt", 'r')
        d = a.read()
        a.close()
        
        d = d.split("\n")
        
        star = None
        goal = None
        gold = []
        terr = []
        
        cy = 0
        
        for l in d:
            
            if(len(l) > 0):
            
                cx = 0
                
                if(l[0] == 'S'):
                    
                    t = l[2:]
                    t = t.split(",")
                    x = int(t[0])
                    y = int(t[1])
                    
                    star = [x,y]
                    
                    qp.setBrush(Qt.blue)
                    qp.drawRect((x*50)+15, (y*50)+10, 20, 30)
                    
                elif(l[0] == 'G'):
                    
                    t = l[2:]
                    t = t.split(",")
                    x = int(t[0])
                    y = int(t[1])
                    
                    goal = [x,y]
                    
                    qp.setBrush(Qt.green)
                    qp.drawRect((x*50), (y*50), 50, 50)
                    
                elif(l[0] == 'T'):
                    
                    t = l[2:]
                    t = t.split(",")
                    x = int(t[0])
                    y = int(t[1])
                    
                    gold.append([x,y])
                    
                elif(l[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                    pass
                else:
                    
                    for c in l:
                        
                        if(c == ' '):
                            qp.setBrush(Qt.white)
                        elif(c == '#'):
                            qp.setBrush(Qt.red)
                            
                        qp.drawRect((cx*50), (cy*50), 50, 50)
                        
                        cx = cx+1 
                
                cy = cy+1
        
        qp.setBrush(Qt.yellow)
        for g in gold:
            
            x = g[0]
            y = g[1]
            
            qp.drawEllipse(x*50+10, y*50+10, 30, 30)

app = QApplication(sys.argv)
l = Laberinto()
sys.exit(app.exec_())
