class Nodo:
	
	valor = None
	
	l = None
	r = None
	
	def __init__(self, valor):
		self.valor = valor

class Arbol:
	
	root = None
	tail = None
	
	def __init__(self):
		self.tail = []
	
	def addCom(self, val):
		
		new = Nodo(val)
		
		if(self.root == None):
			self.root = new
			
		else:
			
			if(self.tail[0].l == None):
				self.tail[0].l = new
			else:
				self.tail[0].r = new
			
			if(self.tail[0].r != None):
				self.tail = self.tail[1:]
		
		self.tail.append(new)	
	
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
a1.addCom(1)
a1.addCom(2)
a1.addCom(3)
a1.addCom(4)
a1.addCom(5)
a1.addCom(6)
a1.addCom(7)

a1.preorden(a1.root)
print("===")
a1.inorden(a1.root)
print("===")
a1.posorden(a1.root)
