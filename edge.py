class Edge:
    def __init__(self,nodeA,nodeB,value):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.X = nodeA.get_x()
        self.Y = nodeA.get_y()
        self.X2 = nodeB.get_x()
        self.Y2 = nodeB.get_y()
        self.value = value
        self.isSelected=False
        self.isHighlighted=False
    
    def set_value(self,value):
        self.value = value

    def set_selected(self,isSelected):
        self.isSelected = isSelected
    
    def set_highlighted(self,isHighlighted):
        self.isHighlighted = isHighlighted
    
    def get_value(self):
        return self.value
    
    def draw(self,canvas):
        if (self.isHighlighted): canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='yellow')
        elif(self.isSelected): canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='#0066ff')
        else: canvas.create_line(self.X,self.Y,self.X2,self.Y2,width=2,fill='white')

    def draw_weight(self,canvas):
        if self.value>0:
            MidX = (self.X+self.X2)/2
            MidY = (self.Y+self.Y2)/2
            canvas.create_rectangle(MidX-10,MidY-10,MidX+8,MidY+8,fill='white')    
            canvas.create_text(MidX,MidY,text=self.value, fill='black', font = ('Lucida Console',9))
