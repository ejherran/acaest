import math

class Nodo:
	
	valor = None
	p = None
	l = None
	r = None
	
	def __init__(self, valor):
		self.valor = valor
		self.p = 0
	
	def getNivel(self):
		
		return int( math.log(self.p) / math.log(2) )
		
		
class Arbol:
	
	root = None
	tail = None
	
	def __init__(self):
		self.tail = []
	
	def calcularP(self, i):
		nivelPadre = self.tail[i].getNivel()
		nivel = nivelPadre+1
		p = 2**nivel + 2 * ( self.tail[i].p - (2**nivelPadre) )
		
		return p
		
	def insertarOrd(self, new):
		
		lim = len(self.tail)
		i = 0
		while(i < lim):
			if(self.tail[i].p > new.p):
				break
			else:
				i = i+1
		
		self.tail[i:i] = [new]
		
	def addCom(self, val):
		
		new = Nodo(val)
		
		if(self.root == None):
			new.p = 1
			self.root = new
			self.tail.append(new)
		else:
			
			if(self.tail[0].l == None):
				new.p = self.calcularP(0)
				self.tail[0].l = new
			else:
				new.p = self.calcularP(0)+1
				self.tail[0].r = new
			
			if(self.tail[0].l != None and self.tail[0].r != None):
				self.tail = self.tail[1:]
		
		self.insertarOrd(new)	
	
	def addLeft(self, val):
		
		new = Nodo(val)
		
		if(self.root == None):
			new.p = 1
			self.root = new
			self.tail.append(new)
		else:
			
			i = 0
			while(True):
				if(self.tail[i].l == None):
					break
				else:
					i = i+1
			
			new.p = self.calcularP(i)
			
			self.tail[i].l = new
			
			if(self.tail[i].l != None and self.tail[i].r != None):
				self.tail = self.tail[:i]+self.tail[i+1:]
			
			self.insertarOrd(new)
			
	def addRight(self, val):
		
		new = Nodo(val)
		
		if(self.root == None):
			new.p = 1
			self.root = new
			self.tail.append(new)
		else:
			
			i = 0
			while(True):
				if(self.tail[i].r == None):
					break
				else:
					i = i+1
			
			new.p = self.calcularP(i)+1
			
			self.tail[i].r = new
			
			if(self.tail[i].l != None and self.tail[i].r != None):
				self.tail = self.tail[:i]+self.tail[i+1:]
			
			self.insertarOrd(new)
			
	
	def preorden(self, arb):
		if(arb != None):
			print(arb.valor)
			self.preorden(arb.l)
			self.preorden(arb.r)
	
	def inorden(self, arb):
		if(arb != None):
			self.inorden(arb.l)
			print(arb.valor)
			self.inorden(arb.r)
	
	def posorden(self, arb):
		if(arb != None):
			self.posorden(arb.l)
			self.posorden(arb.r)
			print(arb.valor)

a1 = Arbol()
a1.addLeft(1)
a1.addRight(2)
a1.addRight(3)
a1.addLeft(4)
a1.addRight(5)
a1.addLeft(6)
a1.addRight(7)
a1.addCom(8)
a1.addCom(9)
a1.addCom(10)
a1.addCom(11)
a1.addCom(12)
a1.addCom(13)
a1.addCom(14)
a1.addCom(15)

print("   ")

a1.preorden(a1.root)
print("===")
a1.inorden(a1.root)
print("===")
a1.posorden(a1.root)







