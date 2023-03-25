from edge import Edge
from node import Node
import random
import os

class NodeManager:
    nodes=[]
    edges=[]

    NODE_SPACING=128
    NODE_ICON_SIZE=48
    def __init__(self,width,height):
        self.width = width
        self.height = height
        base= os.path.abspath(os.getcwd())
        self.add_init_node(0, 'Larrys Laptop','./assets/laptop.png')
        self.add_node(1, 'Larrys Router','./assets/router.png')
        self.add_node(2, 'Server 1','./assets/server.png')
        self.add_node(3, 'Server 2','./assets/server.png')
        self.add_node(4, 'Server 1 Router','./assets/router.png')
        self.add_node(5, 'Server 2 Router','./assets/router.png')
        self.add_node(6, 'Ravens Laptop','./assets/laptop.png')
        self.add_node(7, 'Caths Laptop','./assets/laptop.png')

        self.edges.append(Edge(self.nodes[0],self.nodes[1],0))
        self.edges.append(Edge(self.nodes[1],self.nodes[2],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[1],self.nodes[3],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[2],self.nodes[4],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[3],self.nodes[5],random.randrange(1,50)))
        self.edges.append(Edge(self.nodes[4],self.nodes[6],0))
        self.edges.append(Edge(self.nodes[4],self.nodes[7],0))
    
    def add_init_node(self,id,name,iconPath):
        size = self.NODE_ICON_SIZE
        x= random.randrange(24,self.width-size)
        y= random.randrange(24,self.height-size)
        self.nodes.append(Node(id,name,iconPath,x,y))
    
    def add_node(self,id,name,iconPath):
        space =self.NODE_SPACING
        size = self.NODE_ICON_SIZE
        
        x2= random.randrange(24,self.width-size)
        y2= random.randrange(24,self.height-size)
        for node in self.nodes:
            while (x2<=node.get_x()+space and x2>=node.get_x()-space) and (y2<=node.get_y()+space and y2>=node.get_y()-space): 
                x2= random.randrange(24,self.width-size)
                y2= random.randrange(24,self.height-size)
        self.nodes.append(Node(id,name,iconPath,x2,y2))
    
    def draw(self,canvas):
        for edge in self.edges:
            edge.draw(canvas)
        for node in self.nodes:
            node.draw(canvas)

    def convert_matrix(self):
        length = len(self.nodes)
        matrix = [[-1 for x in range(length)] for y in range(length)] 

        for edge in self.edges:
            matrix[edge.nodeA.id][edge.nodeB.id], matrix[edge.nodeB.id][edge.nodeA.id] = edge.value, edge.value

        return matrix