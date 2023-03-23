from edge import Edge
from node import Node
import random
import os

class NodeManager:
    nodes=[]
    edges=[]

    NODE_ICON_SIZE=48
    def __init__(self,width,height):
        self.width = width
        self.height = height
        base= os.path.abspath(os.getcwd())
        self.add_init_node('Larrys Laptop','./assets/laptop.png')
        self.add_node('Larrys Router','./assets/router.png')
        self.add_node('Server 1','./assets/server.png')
        self.add_node('Server 2','./assets/server.png')
        self.add_node('Server 1 Router','./assets/router.png')
        self.add_node('Server 2 Router','./assets/router.png')
        self.add_node('Ravens Laptop','./assets/laptop.png')
        self.add_node('Caths Laptop','./assets/laptop.png')
    


        self.edges.append(Edge(self.nodes[0],self.nodes[1],0))
        self.edges.append(Edge(self.nodes[1],self.nodes[2],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[1],self.nodes[3],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[2],self.nodes[4],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[3],self.nodes[5],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[4],self.nodes[6],0))
        self.edges.append(Edge(self.nodes[4],self.nodes[7],0))
    
    def add_init_node(self,name,iconPath):
        size =self.NODE_ICON_SIZE
        x= random.randrange(24,self.width-size)
        y= random.randrange(24,self.height-size)
        self.nodes.append(Node(name,iconPath,x,y))
    
    def add_node(self,name,iconPath):
        size =self.NODE_ICON_SIZE
        x2= random.randrange(24,self.width-size)
        y2= random.randrange(24,self.height-size)
        for node in self.nodes:
            while (x2<=node.get_x()+size and x2>=node.get_x()-size) and (y2<=node.get_y()+size and y2>=node.get_y()-size): 
                x2= random.randrange(24,self.width-size)
                y2= random.randrange(24,self.height-size)
        self.nodes.append(Node(name,iconPath,x2,y2))
    
    def draw(self,canvas):
        for edge in self.edges:
            edge.draw(canvas)
        for node in self.nodes:
            node.draw(canvas)