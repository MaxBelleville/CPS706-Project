from edge import Edge
from node import Node
import random
import re
import ast
from collections import defaultdict
from tkinter import messagebox
from algorithms.dijkstra import dijkstra

class GraphManager:
    nodes=[]
    edges=[]
    nodeTypes={"computer":"./assets/computer.png","laptop":"./assets/laptop.png",
               "server":"./assets/server.png","router":"./assets/router.png"}

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def add_from_file(self,path):
        f = open(path,"r")
        sections = re.split("-+",re.sub("#.*","",f.read(),re.MULTILINE)) #Get rid of comments in text file and split by -
        nodeLines=list(filter(None,sections[0].split("\n"))) #split the node section by lines and remove empty lines from list
       
        try:
            self.parse_nodes(nodeLines) 
            adj_matrix=ast.literal_eval((sections[1].replace("\n",""))) #remove new line and convert string of 2d array into array
            weight_matrix=ast.literal_eval((sections[2].replace("\n",""))) #TODO: try catch and separate into own function.
            self.parse_matrices(adj_matrix,weight_matrix)
            dijkstra(adj_matrix, weight_matrix, 0)
            for line in weight_matrix:
                print(line)
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
            self.check_all_overlap(node)
    
            
    def check_all_overlap(self,node):
        noneOverlap = True
        overlapObj = self.nodes[0]
        for otherNode in self.nodes: #will loop through every node other then current node
                if node!=otherNode:     
                    if node.overlaps(otherNode):
                        noneOverlap = False
                        overlapObj = otherNode
                        break
        if noneOverlap == False:
            x= random.randrange(Node.get_size(),self.width-Node.get_size())
            y= random.randrange(Node.get_size(),self.height-Node.get_size())
            node.set_pos(x,y)
            self.check_all_overlap(node)

    def draw(self):
        self.canvas.delete("all")
        for node in self.nodes:
            node.draw(self.canvas)

        for edge in self.edges:
            edge.draw(self.canvas)

        for node in self.nodes:
            node.draw_name(self.canvas)

        for edge in self.edges:
            edge.draw_weight(self.canvas)
