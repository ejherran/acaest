from Node import Node
from Edge import Edge

from math import inf as INF

class Graph():
    
    def __init__(self):
        
        self.nodes = []

    def addNode(self, value, x=0, y=0):
        
        new = Node()
        new.value = value
        new.x = x
        new.y = y
        
        self.nodes.append(new)
    
    def addEdge(self, origin, goal, value, double=False):
        
        new = Edge()
        new.origin = origin
        new.goal = goal
        new.value = value
        
        new.pX.append(origin.x)
        new.pY.append(origin.y)
        new.pX.append(goal.x)
        new.pY.append(goal.y)
        
        origin.edges.append(new)
        
        
        if(double):
            
            new.isDouble = True
            
            new = Edge()                        # Create counter edge!
            new.origin = goal
            new.goal = origin
            new.value = value
            
            new.pX.append(goal.x)
            new.pY.append(goal.y)
            new.pX.append(origin.x)
            new.pY.append(origin.y)
            
            goal.edges.append(new)
            new.isDouble = True
    
    def searchNode(self, value):
        
        for node in self.nodes:
            
            if(node.value == value):
                return node
        
        return None
    
    def searchEdge(self, value, origin, goal):
        
        for edge in origin.edges:
            
            if(edge.value == value and edge.goal == goal):
                return edge
            
        return None
    
    def editNode(self, old, new):
        
        node = self.searchNode(old)
        if(node != None):
            node.value = new
    
    def editEdgeValue(self, old, origin, goal, new):
        
        edge = self.searchEdge(old, origin, goal)
        
        if(edge != None):
            edge.value = new
            
            if(edge.isDouble):
                
                edge = self.searchEdge(old, goal, origin)
                edge.value = new
    
    def editEdgeGoal(self, value, origin, goalOld, goalNew):
        
        edge = self.searchEdge(value, origin, goalOld)
        
        if(edge != None):
            
            if( not(edge.isDouble) ):
                
                edge.goal = goalNew
                
            else:
                return -1
    
    def delNode(self, value):
        
        node = self.searchNode(value)
        if(node != None):
            
            for x in self.nodes:
                
                toLive = []
                
                for edge in x.edges:
                    if( edge.goal != node ):
                        toLive.append(edge)
                
                x.edges = toLive
            
            self.nodes.remove(node)
    
    def delEdge(self, value, origin, goal):
        
        target = self.searchEdge(value, origin, goal)
        
        if(target != None):
            
            toLive = []
            
            for edge in origin.edges:
                if( edge != target ):
                    toLive.append(edge)
            
            origin.edges = toLive
            
            if(target.isDouble):
                
                target = self.searchEdge(value, goal, origin)
                
                toLive = []
                
                for edge in goal.edges:
                    if( edge != target ):
                        toLive.append(edge)
                
                goal.edges = toLive  
    
    def show(self):
        
        for node in self.nodes:
            
            print(node.value)
            
            for edge in node.edges:
                print("->", edge.goal.value, ":", edge.value, " | ", edge.isDouble)
    
    def bfs(self, origin, goal=""):
        
        fathers = {}
        costs = {}
        views = []
        tail = []
        
        origin = self.searchNode(origin)
        if(origin != None):
            
            for n in self.nodes:
                fathers[n.value] = None
                costs[n.value] = INF
            
            costs[origin.value] = 0
            tail.append(origin)
            
            while(len(tail) > 0):
                
                q = tail[0]
                tail = tail[1:]
                
                for a in q.edges:
                    
                    v = a.goal
                    
                    if( not (v in views) ):
                        
                        nc = costs[q.value]+1
                        if(nc < costs[v.value]):
                            fathers[v.value] = q.value
                            costs[v.value] = nc
                        
                        if(not (v in tail) ):
                            tail.append(v)
                
                views.append(q)
            
            for n in views:
                print(n.value)
            print("\n---\n")
            
            lk = list(costs.keys())
            lk.sort()
            for k in lk:
                print(k,": ",costs[k])
            print("\n---\n")
            
            for k in lk:
                print(k,": ",fathers[k])
            print("\n---\n")
            
            if(goal != ""):
                
                tmp = [goal]
                while(tmp[0] != origin.value):
                    tmp.insert(0, fathers[tmp[0]])
                
                print("->".join(tmp))
                    
            
            print("========================================================")
    
    def dfs(self, origin, goal=""):
        
        fathers = {}
        costs = {}
        views = []
        stack = []
        
        origin = self.searchNode(origin)
        if(origin != None):
            
            for n in self.nodes:
                fathers[n.value] = None
                costs[n.value] = INF
            
            costs[origin.value] = 0
            stack.append(origin)
            
            while(len(stack) > 0):
                
                q = stack[0]
                stack = stack[1:]
                
                for a in q.edges:
                    
                    v = a.goal
                    
                    if( not (v in views) ):
                        
                        nc = costs[q.value]+1
                        if(nc < costs[v.value]):
                            fathers[v.value] = q.value
                            costs[v.value] = nc
                        
                        if(not (v in stack) ):
                            stack.insert(0, v)
                
                views.append(q)
            
            for n in views:
                print(n.value)
            print("\n---\n")
            
            lk = list(costs.keys())
            lk.sort()
            for k in lk:
                print(k,": ",costs[k])
            print("\n---\n")
            
            for k in lk:
                print(k,": ",fathers[k])
            print("\n---\n")
            
            if(goal != ""):
                
                tmp = [goal]
                while(tmp[0] != origin.value):
                    tmp.insert(0, fathers[tmp[0]])
                
                print("->".join(tmp))
                    
            
            print("========================================================")
    
    def getMin(self, tail, costs):
        
        pos = 0
        i = 1
        while(i < len(tail)):
            
            if(costs[ tail[i].value ] < costs[ tail[pos].value ]):
                pos = i
            i = i + 1
        
        return pos
    
    def dijkstra(self, origin, goal=""):
        
        fathers = {}
        costs = {}
        views = []
        tail = []
        
        origin = self.searchNode(origin)
        if(origin != None):
            
            for n in self.nodes:
                fathers[n.value] = None
                costs[n.value] = INF
            
            costs[origin.value] = 0
            tail.append(origin)
            
            while(len(tail) > 0):
                
                ind = self.getMin(tail, costs)
                q = tail[ind]
                del(tail[ind])
                
                for a in q.edges:
                    
                    v = a.goal
                    
                    if( not (v in views) ):
                        
                        nc = costs[q.value]+a.value
                        if(nc < costs[v.value]):
                            fathers[v.value] = q.value
                            costs[v.value] = nc
                        
                        if(not (v in tail) ):
                            tail.append(v)
                
                views.append(q)
            
            for n in views:
                print(n.value)
            print("\n---\n")
            
            lk = list(costs.keys())
            lk.sort()
            for k in lk:
                print(k,": ",costs[k])
            print("\n---\n")
            
            for k in lk:
                print(k,": ",fathers[k])
            print("\n---\n")
            
            if(goal != ""):
                
                tmp = [goal]
                while(tmp[0] != origin.value):
                    tmp.insert(0, fathers[tmp[0]])
                
                print("->".join(tmp))
                    
            
            print("========================================================")
    
    def getHeuro(self, tail, costs, goal):
        
        pos = 0
        i = 1
        while(i < len(tail)):
            
            d1 = (((tail[pos].x - goal.x)**2) + ((tail[pos].y - goal.y)**2))**0.5
            d2 = (((tail[i].x - goal.x)**2) + ((tail[i].y - goal.y)**2))**0.5
            
            if( (costs[ tail[i].value ]+d2) < (costs[ tail[pos].value ]+d1)):
                pos = i
            i = i + 1
        
        return pos
    
    def aStar(self, origin, goal):
        
        fathers = {}
        costs = {}
        views = []
        tail = []
        
        origin = self.searchNode(origin)
        goal = self.searchNode(goal)
        if(origin != None and goal != None):
            
            for n in self.nodes:
                fathers[n.value] = None
                costs[n.value] = INF
            
            costs[origin.value] = 0
            tail.append(origin)
            
            stop = False
            
            while(len(tail) > 0):
                
                ind = self.getHeuro(tail, costs, goal)
                q = tail[ind]
                del(tail[ind])
                
                for a in q.edges:
                    
                    v = a.goal
                    
                    if( not (v in views) ):
                        
                        nc = costs[q.value]+a.value
                        if(nc < costs[v.value]):
                            fathers[v.value] = q.value
                            costs[v.value] = nc
                        
                        if(not (v in tail) ):
                            tail.append(v)
                    
                    if(v == goal):
                        stop = True
                        break
                
                views.append(q)
                
                if(stop):
                    break
            
            for n in views:
                print(n.value)
            print("\n---\n")
            
            lk = list(costs.keys())
            lk.sort()
            for k in lk:
                print(k,": ",costs[k])
            print("\n---\n")
            
            for k in lk:
                print(k,": ",fathers[k])
            print("\n---\n")
               
            tmp = [goal.value]
            while(tmp[0] != origin.value):
                tmp.insert(0, fathers[tmp[0]])
            
            print("->".join(tmp))
                    
            
            print("========================================================")
    
g = Graph()
g.addNode("A", 0, 0)
g.addNode("B", 30, 40)
g.addNode("C", 10, 5)
g.addNode("D", 20, 18)
g.addNode("E", 5, 3)
g.addNode("F", 21, 20)
g.addNode("G", 12, 12)
g.addNode("H", 7, 9)
g.addNode("I", 9, 9)
g.addNode("J", 40, 40)

g.addEdge(g.searchNode("A"), g.searchNode("B"), 10)
g.addEdge(g.searchNode("A"), g.searchNode("C"), 5)
g.addEdge(g.searchNode("A"), g.searchNode("D"), 8, True)
g.addEdge(g.searchNode("B"), g.searchNode("C"), 11)
g.addEdge(g.searchNode("D"), g.searchNode("E"), 5)
g.addEdge(g.searchNode("D"), g.searchNode("F"), 6)
g.addEdge(g.searchNode("E"), g.searchNode("J"), 9)
g.addEdge(g.searchNode("F"), g.searchNode("C"), 8)
g.addEdge(g.searchNode("C"), g.searchNode("G"), 6)
g.addEdge(g.searchNode("G"), g.searchNode("F"), 6)
g.addEdge(g.searchNode("G"), g.searchNode("H"), 4)
g.addEdge(g.searchNode("H"), g.searchNode("I"), 8, True)
g.addEdge(g.searchNode("I"), g.searchNode("J"), 10, True)
g.addEdge(g.searchNode("J"), g.searchNode("A"), 7)

g.show()
print("======================================")
g.bfs("A", "J")
g.dfs("A", "J") 
g.dijkstra("A", "J") 
g.aStar("A", "J") 
