from PyQt5.QtWidgets import QWidget , QApplication, QInputDialog
from PyQt5.QtGui import QPainter, QPen, QFont, QFontMetrics, QPolygon
from PyQt5.QtCore import Qt, QPoint
import sys

class Test(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.nodos = []
        self.aristas = []
        self.estado = 0         # 0 - Normal, 1 - Agarrar
        self.target = None
        self.div = None
        
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
            
            pen = QPen(Qt.blue)
            pen.setWidth(3)
            qp.setPen(pen)
            
            points = []
            ct = 0
            while(ct < len(a)):
                points.append(QPoint(a[ct][0], a[ct][1]))
                ct = ct+1
            
            poly = QPolygon(points)
            qp.drawPolyline(poly)
                
            foo = self.arrow(a[1][0], a[1][1], a[0][0], a[0][1], 25)
            fod = self.arrow(a[ct-2][0], a[ct-2][1], a[ct-1][0], a[ct-1][1], 25)
            
            pen = QPen(Qt.red)
            pen.setWidth(3)
            qp.setPen(pen)
            qp.setBrush(Qt.red)
            
            if(foo != None):
                poly = QPolygon([QPoint(foo[0], foo[1]), QPoint(foo[2], foo[3]), QPoint(foo[4], foo[5])])
                qp.drawPolygon(poly)
            
            if(fod != None):
                poly = QPolygon([QPoint(fod[0], fod[1]), QPoint(fod[2], fod[3]), QPoint(fod[4], fod[5])])
                qp.drawPolygon(poly)
                
        qp.setBrush(Qt.green)
        pen = QPen(Qt.black)
        pen.setWidth(1)
        qp.setPen(pen)
        
        for a in self.aristas:
            ct = 1
            while(ct < len(a)-1):
                
                qp.drawEllipse(a[ct][0]-5, a[ct][1]-5, 10, 10)
                
                if(len(a[ct]) == 3):
                    
                    fb = QFont('Linux Libertine Mono O', 10)
                    fm = QFontMetrics(fb)
                    
                    qp.setFont(fb)
                    w = fm.width(a[ct][2])
                    
                    qp.setBrush(Qt.white)
                    qp.drawRect(a[ct][0]-(w/2)-10, a[ct][1], w+20, 20)
                    
                    qp.setBrush(Qt.green)
                    pen = QPen(Qt.black)
                    pen.setWidth(1)
                    qp.setPen(pen)
                    
                    qp.drawText(a[ct][0]-(w/2), a[ct][1]+15, a[ct][2])
                    
                ct = ct+1
            
        qp.setPen(Qt.green)
        qp.setBrush(Qt.red)
        qp.setFont(QFont('Linux Libertine Mono O', 30))

        for n in self.nodos:
            qp.drawEllipse(n[0]-25, n[1]-25, 50, 50)
            qp.drawText(n[0]-12, n[1]+12, n[2])
        
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
        
        if(self.estado == 3):
            arista = self.div[0]
            punto = self.div[1]
            
            if(len(arista[punto]) == 3):
                arista[punto] = [e.x(), e.y(), arista[punto][2]]
            else:
                arista[punto] = [e.x(), e.y()]
                
            self.update()
        
    def mousePressEvent(self, e):
        
        if(e.button() == 2):
            
            self.touch(e.x(), e.y(), 2)
            
            if(self.div != None):
                
                arista = self.div[0]
                punto = self.div[1]
                
                if(len(arista[punto]) < 3):
                    del(arista[punto])
                    self.update()
                    
            else:
                
                text, ok = QInputDialog.getText(self, "Node Value", "Please provide a value for this node?:")
                
                if(ok):
                    self.nodos.append([e.x(), e.y(), text[0]])
                    self.update()
            
        elif(e.button() == 1 and self.estado == 0):
            
            ind = self.touch(e.x(), e.y())
            
            if(ind != None):
                
                self.target = self.nodos[ind]
                self.estado = 1
            
            elif(self.div != None):
                self.estado = 3
        
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
                    
                    text, ok = QInputDialog.getText(self, "Edge Value", "Please provide a value for this edge?:")
                    
                    if(ok):
                        
                        mx = (tmp[0]-self.target[0])/2
                        my = (tmp[1]-self.target[1])/2
                        
                        self.aristas.append([self.target, [ mx + self.target[0] , my+self.target[1], text ], tmp])
                    
                    self.target = None
                    self.estado = 0
                    self.update()
        
        elif(e.button() == 1 and self.estado == 3):
            
            self.div = None
            self.estado = 0
        
        self.update()
                
    def touch(self, x, y, btn = 1):
        
        # Nodos
        i = 0
        while(i < len(self.nodos)):
            
            d = ((self.nodos[i][0]-x)**2)+((self.nodos[i][1]-y)**2)
            d = d ** 0.5
            
            if(d <= 25):
                return i
            else: 
                i = i + 1
        
        for a in self.aristas:
            ct = 1
            while(ct < len(a)-1):
                
                d = (((x-a[ct][0])**2)+((y-a[ct][1])**2))**0.5
                if(d <= 10):
                    self.div = (a, ct)
                    return None
                
                ct = ct+1
            
        # Rompe Aristas
        if(btn == 1):
            for a in self.aristas:
                
                ct = 0
                while(ct < len(a)-1):
                
                    x1 = a[ct][0]
                    y1 = a[ct][1]
                    
                    x2 = a[ct+1][0]
                    y2 = a[ct+1][1]
                    
                    d = self.disToLine(x, y, x1, y1, x2, y2)
                    
                    if(d != None):
                        if(d[0] <= 10):
                            a.insert(ct+1, [d[1], d[2]])
                            self.estado = 3
                            self.div = (a, ct+1)
                            break
                    ct = ct+1
    
    def disToLine(self, px, py, x1, y1, x2, y2):
        
        if(x1 != x2 and y1 != y2):
            
            m1 = (y2-y1) / (x2-x1)
            b1 = y1 - (m1*x1)
            
            m2 = -1 / m1
            b2 = py - (m2*px)
            
            xc = (b2-b1) / (m1-m2)
            yc = (m2*xc)+b2
            
            d = (((px-xc)**2) + ((py-yc)**2))**0.5
            
            dm = (((x2-x1)**2) + ((y2-y1)**2))**0.5
            dc = (((xc-x1)**2) + ((yc-y1)**2))**0.5
            
            if(dc <= dm):
                return (d, xc, yc)
            else:
                return None
    
    def arrow(self, x1, y1, x2, y2, d):
        
        if(x1 != x2 and y1 != y2):
            
            xb = x2-x1
            yb = y2-y1
            
            m = yb / xb
            b = yb - (m*xb)
            
            D = d**2
            
            P = xb
            Q = yb
            
            A = 1 + (m**2)
            B = (-2*P)+(2*b*m)-(2*Q*m)
            C = (P**2)+(Q**2)+(b**2)-(2*b*Q)-D
            
            xp = ((-1*B) + ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
            yp = (m*xp) + b
            
            xn = ((-1*B) - ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
            yn = (m*xn) + b
            
            dp = ((xp**2) + (yp**2))**0.5
            dn = ((xn**2) + (yn**2))**0.5
            
            if(dp < dn):
                
                D = (d+20)**2
            
                A = 1 + (m**2)
                B = (-2*P)+(2*b*m)-(2*Q*m)
                C = (P**2)+(Q**2)+(b**2)-(2*b*Q)-D
                
                xp2 = ((-1*B) + ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yp2 = (m*xp2) + b
                
                D = 100
                P = xp2
                Q = yp2
                
                m2 = -1 / m
                b2 = Q-(m2*P)
                
                A = 1 + (m2**2)
                B = (-2*P)+(2*b2*m2)-(2*Q*m2)
                C = (P**2)+(Q**2)+(b2**2)-(2*b2*Q)-D
                
                xp3 = ((-1*B) + ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yp3 = (m2*xp3) + b2
                
                xn3 = ((-1*B) - ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yn3 = (m2*xn3) + b2
                
                return (xp+x1, yp+y1, xp3+x1, yp3+y1, xn3+x1, yn3+y1)
                
            else:
                
                D = (d+20)**2
            
                A = 1 + (m**2)
                B = (-2*P)+(2*b*m)-(2*Q*m)
                C = (P**2)+(Q**2)+(b**2)-(2*b*Q)-D
                
                xn2 = ((-1*B) - ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yn2 = (m*xn2) + b
                
                D = 100
                P = xn2
                Q = yn2
                
                m2 = -1 / m
                b2 = Q-(m2*P)
                
                A = 1 + (m2**2)
                B = (-2*P)+(2*b2*m2)-(2*Q*m2)
                C = (P**2)+(Q**2)+(b2**2)-(2*b2*Q)-D
                
                xp3 = ((-1*B) + ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yp3 = (m2*xp3) + b2
                
                xn3 = ((-1*B) - ( ( (B**2) -(4*A*C) ) ** 0.5 )) / (2*A)
                yn3 = (m2*xn3) + b2
                
                return (xn+x1, yn+y1, xp3+x1, yp3+y1, xn3+x1, yn3+y1)
        elif(x1 == x2):
            
            if(y1 < y2):
                return(x2,y2-25, x2-10, y2-45, x2+10, y2-45)
            else:
                return(x2,y2+25, x2-10, y2+45, x2+10, y2+45)
        
        elif(y1 == y2):
            
            if(x1 < x2):
                return(x2-25,y2, x2-45, y2-10, x2-45, y2+10)
            else:
                return(x2+25,y2, x2+45, y2-10, x2+45, y2+10)
    
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
