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
    

    
    def is_connected(self,selectedNode):
        selected=False
        for i in range(1,len(selectedNode)):
            if(self.nodeA==selectedNode[i-1] and self.nodeB==selectedNode[i]):
                selected=True
                break
            if(self.nodeB==selectedNode[i-1] and self.nodeA==selectedNode[i]):
                selected=True
                break
        return selected

    def draw(self,canvas,selectedNode):
        if (self.is_connected(selectedNode)): canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='blue')
        else: canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='white')

    def draw_weight(self,canvas):
        if self.value>0:
            MidX = (self.X+self.X2)/2
            MidY = (self.Y+self.Y2)/2
            canvas.create_oval(MidX-10,MidY-10,MidX+8,MidY+8,fill='white')    
            canvas.create_text(MidX,MidY,text=self.value, fill='black', font = ('Lucida Console',9))