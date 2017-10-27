from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt
import sys

class Test(QWidget):
    
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
        qp.setBrush(Qt.red)
        
        pen = QPen(Qt.blue)
        pen.setWidth(3)
        
        qp.setPen(pen)
        for a in self.aristas:
            qp.drawLine(a[0][0], a[0][1], a[1][0], a[1][1])
            
        qp.setPen(Qt.green)
        for n in self.nodos:
            qp.drawEllipse(n[0]-25, n[1]-25, 50, 50)
        
    def keyPressEvent(self, e):
        
        if(e.key() == 65):
            self.estado = 2
        elif(e.key() == 32):
            self.estado = 0
    
    def mouseMoveEvent(self, e):
        
        if(self.estado == 1):
            self.target[0] = e.x()
            self.target[1] = e.y()
            self.update()
        
    def mousePressEvent(self, e):
        
        if(e.button() == 2):
            self.nodos.append([e.x(), e.y()])
            self.update()
        elif(e.button() == 1 and self.estado == 0):
            
            ind = self.touch(e.x(), e.y())
            if(ind != None):
                self.target = self.nodos[ind]
                self.estado = 1
        
        elif(e.button() == 1 and self.estado == 1):
            
            self.estado = 0
            self.target = None
        
        elif(e.button() == 1 and self.estado == 2):
            
            ind = self.touch(e.x(), e.y())
            if(ind != None):
                
                if(self.target == None):
                    self.target = self.nodos[ind]
                else:
                    
                    tmp = self.nodos[ind]
                    self.aristas.append([self.target, tmp])
                    self.target = None
                    self.estado = 0
                    self.update()
                
    def touch(self, x, y):
        
        i = 0
        while(i < len(self.nodos)):
            
            d = ((self.nodos[i][0]-x)**2)+((self.nodos[i][1]-y)**2)
            d = d ** 0.5
            
            if(d <= 25):
                return i
            else: 
                i = i + 1
        
        for a in self.aristas:
            
            x1 = a[0][0]
            y1 = a[0][1]
            
            x2 = a[1][0]
            y2 = a[1][1]
        
            
app = QApplication(sys.argv)
t = Test()
sys.exit(app.exec_())




"""
qp = QPainter()
qp.begin(self)
pen = QPen(Qt.green)
pen.setWidth(3)
qp.setPen(pen)
qp.drawLine(50, 50, 100, 100)

qp.setBrush(Qt.red)
qp.drawEllipse(100, 100, 200, 200)

qp.setFont(QFont('Linux Libertine Mono O', 40))
qp.drawText(300, 300, "Hola")
"""
