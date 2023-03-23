class Edge:
    def __init__(self,nodeA,nodeB,value):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.X = nodeA.get_x()
        self.Y = nodeA.get_y()
        self.X2 = nodeB.get_x()
        self.Y2 = nodeB.get_y()
        self.value = value
    
    def set_value(self,value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def get_connected(self,selected):
        if(selected==self.nodeA):
            return self.nodeB
        elif(selected==self.nodeB):
            return self.nodeA
        return

    def draw(self,canvas):
        canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='white')