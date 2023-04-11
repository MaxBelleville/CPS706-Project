from edge import Edge
from node import Node
import random
import re
import os
import ast
from collections import defaultdict
from tkinter import messagebox
from algorithms.dijkstra import dijkstra
from algorithms.bellmanFord import bellmanFord

class GraphManager:
    nodes=[]
    edges=[]
    adjMatrix=[]
    weightMatrix=[]
    selectedNodes=[]
    nodeCosts=[]
    startNode=-1
    endNode=-1
    isDijkstra=True
    selectEnd=1
    iter=-1
    nodeTypes={"computer":"./assets/computer.png","laptop":"./assets/laptop.png",
               "server":"./assets/server.png","router":"./assets/router.png"}

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def add_from_file(self,path):
        if os.access(path, os.R_OK):
            self.edges=[]
            self.nodes=[]
            f = open(path,"r")
            sections = re.split("-+",re.sub("#.*","",f.read(),re.MULTILINE)) #Get rid of comments in text file and split by -
            nodeLines=list(filter(None,sections[0].split("\n"))) #split the node section by lines and remove empty lines from list
        
            try:
                self.parse_nodes(nodeLines)
                self.adjMatrix=ast.literal_eval((sections[1].replace("\n","").replace(" ",""))) #remove new line and convert string of 2d array into array
                self.weightMatrix=ast.literal_eval((sections[2].replace("\n","").replace(" ",""))) #TODO: try catch and separate into own function.
                self.parse_matrices(self.adjMatrix,self.weightMatrix)
                self.draw()
            except Exception as ex:
                messagebox.showerror("Failed to load file", ex)
                self.edges=[]
                self.nodes=[]

    def parse_nodes(self,nodeLines):
        if len(nodeLines)>=2 and len(nodeLines)<=10: #ensure certain number of nodes then parse nodes
            for line in nodeLines:
                nodeInfo=line.split(',')
                if len(nodeInfo)==3:
                    type=nodeInfo[2].strip().lower()
                    name=nodeInfo[1].strip()
                    id=nodeInfo[0]
                    if type in self.nodeTypes and id.isdigit() and name!=None:
                        self.add_node(id,name,self.nodeTypes[type])
                    else: 
                        raise Exception("Incorrect information in node fields\nGot " + line + 
                                         " should be in form (id,name,type) where type is either laptop, router, server, computer and id is numeric")
                else: 
                    raise Exception("Missing information in node fields\nGot " + line + 
                                         " should be in form (id,name,type) where type is either laptop, router, server, computer and id is numeric")
            self.remove_overlap()
        else: 
            raise Exception("Too few or too many nodes\nDue to visual cluttering we restrict the number of nodes, minium being 2 and maximum being 10")

    def parse_matrices(self,a_mat,w_mat):
        if len(a_mat)>0 and len(w_mat)>0:
            if (len(a_mat) == len(w_mat) and len(a_mat[0]) == len(w_mat[0]) and 
                len(a_mat) ==  len(a_mat[0])): #ensure all are equal length
                a_list = defaultdict(list)
                for y in range(len(a_mat)):
                    for x in range(len(a_mat)):
                        if a_mat[x][y] == 0 and w_mat[x][y]>0: 
                            raise Exception("Weight missing edge connection", "The adjacency matrix at "+ str(x) + ","+ str(y) + 
                                            " is empty whereas weight matrix is has a value")
                        if w_mat[x][y]>9:
                            raise Exception("Weight is to large", "For simplicities sake on the input weights can only be 0 to 9")
                        if a_mat[x][y] != a_mat[y][x]: 
                            raise Exception("Adjacency Matrix Symmetry Error\nDifference between value at " + str(y) + ","+ str(x)+ ": "+str(a_mat[y][x])+
                                            " and " + str(x) + ","+ str(y)+ ": "+str(a_mat[x][y]))
                        if w_mat[x][y] != w_mat[y][x]: 
                            raise Exception("Weight Matrix Symmetry Error\nDifference between value at " + str(y) + ","+ str(x)+ ": "+str(w_mat[y][x])+
                                            " and " + str(x) + ","+ str(y)+ ": "+str(w_mat[x][y]))
                        if a_mat[y][x] != 0: #convert to adj list
                            a_list[y].append(x)
        for key in a_list:
            for val in a_list[key]:
                newEdge= Edge(self.nodes[key],self.nodes[val],w_mat[key][val]) #create new edge
                if not Edge(self.nodes[val],self.nodes[key],w_mat[key][val]) in self.edges: #check if edge already exists (removes duplicates)
                    self.edges.append(newEdge)

    def add_canvas(self,canvas):
        self.canvas = canvas

    def add_node(self,id,name,iconPath):
        x= random.randrange(Node.get_size(),self.width-Node.get_size())
        y= random.randrange(Node.get_size(),self.height-Node.get_size())
        self.nodes.append(Node(id,name,iconPath,x,y))
    
    def remove_overlap(self):
        for node in self.nodes:
            self.remove_all_overlap(node)
    
            
    def remove_all_overlap(self,node):
        noneOverlap = True
        for otherNode in self.nodes: #will loop through every node other then current node
                if node!=otherNode:     
                    if node.node_overlaps(otherNode):
                        noneOverlap = False
                        break
        if noneOverlap == False:
            x= random.randrange(Node.get_size(),self.width-Node.get_size())
            y= random.randrange(Node.get_size(),self.height-Node.get_size())
            node.set_pos(x,y)
            self.remove_all_overlap(node)

    def check_overlap(self,x,y):
        for i in range(len(self.nodes)):
            if(self.nodes[i].overlaps(x,y)):
                return i
        return -1
            
    def set_start(self,x,y):
        self.startNode = self.check_overlap(x,y)
        self.reset_node_value()
        if(self.startNode>-1 and not self.isDijkstra): self.nodes[self.startNode].set_value(0)
        if(self.startNode>-1): self.draw()
    
    def set_end(self,x,y):
        tmp = self.check_overlap(x,y)
        if(self.startNode!=tmp): self.endNode = tmp
        if(self.endNode>-1): self.draw()

    def initialize(self):
        if(self.isDijkstra):
            diklist = dijkstra(self.adjMatrix, self.weightMatrix, self.startNode, self.endNode)
            self.selectedNodes=[self.nodes[i] for i in diklist[1]]
        else:
            extra,output = bellmanFord(self.adjMatrix,self.weightMatrix,self.startNode,self.endNode)
            self.nodeCosts=output
            self.selectedNodes=[self.nodes[int(i)] for i in extra[1]]
        self.draw()

    def set_algorithm(self,option):
        if(option == "Dijkstra"): self.isDijkstra=True
        else:  self.isDijkstra=False
        self.draw()


    def step(self):
        if(self.isDijkstra):
            if(self.selectEnd<len(self.selectedNodes)):self.selectEnd+=1;
            if len(self.selectedNodes)==0: return float("inf"),0
            self.draw()
            cost=0
            for edge in self.edges:
                connected,isLast= self.is_dijkstra_connected(edge,self.selectedNodes[:self.selectEnd])
                if(connected):
                    cost+=edge.get_value()/2
            return int(cost),0
        else:
            cost = float('inf')
            if(self.iter<len(self.nodeCosts)-1): self.iter+=1
            if(self.iter>=len(self.nodeCosts)-1):
                self.selectEnd=len(self.selectedNodes)
                self.draw()
                if(self.check_end()):
                    cost= self.nodes[self.endNode].get_value()
            for i,val in enumerate(self.nodeCosts[self.iter]):
                self.nodes[i].set_value(val)
                if(self.iter>=len(self.nodeCosts)-1):self.nodes[i].set_highlighted(False)
                elif(val!=float('inf') and i!=self.startNode and i!=self.endNode): self.nodes[i].set_highlighted(True)
           
            self.draw()
            return cost,self.iter+1
            


    def reset_node_value(self):
        for node in self.nodes:
             node.set_selected(False)
             node.set_highlighted(False)
             if (not self.isDijkstra):
                node.set_value(float("inf"))

    def reset(self):
        self.endNode = -1
        self.reset_node_value()
        for edge in self.edges:
             edge.set_selected(False)
             edge.set_highlighted(False)
        self.startNode = -1
        self.iter=-1
        self.selectEnd=1
       
        self.draw()

    def check_start(self):
        return True if self.startNode>-1 else False
    
    def check_end(self):
        return True if self.endNode>-1 else False

    def is_dijkstra_connected(self,edge,selectedNode):
        connected=False
        isLast=False
        for i in range(1,len(selectedNode)):
            if(i==len(selectedNode)-1): isLast=True
            if(edge.nodeA==selectedNode[i-1] and edge.nodeB==selectedNode[i]):
                connected=True
                break
            if(edge.nodeB==selectedNode[i-1] and edge.nodeA==selectedNode[i]):
                connected=True
                break
        return  connected,isLast

    def draw(self):
        self.canvas.delete("all")
        if(self.check_start()):
            self.nodes[self.startNode].draw_start(self.canvas)
        if(self.check_end()):
            self.nodes[self.endNode].draw_end(self.canvas)

        for node in self.nodes:
            for selected in self.selectedNodes[1:self.selectEnd-1]:
                if(node == selected):
                    node.set_selected(True)
            node.draw(self.canvas)

        for edge in self.edges:
            connected,isLast = self.is_dijkstra_connected(edge,self.selectedNodes[:self.selectEnd])
            if(connected and isLast): edge.set_highlighted(True)
            elif(connected): 
                edge.set_selected(True)
                edge.set_highlighted(False)
            edge.draw(self.canvas)

        for node in self.nodes:
            node.draw_extras(self.canvas,self.isDijkstra)

        for edge in self.edges:
            edge.draw_weight(self.canvas)
