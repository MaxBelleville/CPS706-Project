import tkinter as tk
import math
class Node:
    NODE_SPACING=128
    NODE_ICON_SIZE=48
    def __init__(self, id, name,iconPath,X,Y):
        self.id = id
        self.name = name
        self.icon = tk.PhotoImage(file=iconPath)
        self.X = X
        self.Y = Y

    def get_x(self):
        return self.X
    
    def get_y(self):
        return self.Y
    
    @staticmethod
    def get_spacing():
        return Node.NODE_ICON_SIZE
    
    @staticmethod
    def get_size():
        return Node.NODE_ICON_SIZE


    def set_pos(self,x,y):
        self.X,self.Y=x,y

    def node_overlaps(self,node):
        space = self.NODE_SPACING
        X2,Y2 = node.get_x(),node.get_y()
        if (X2+space>=self.X and X2<=self.X+space) and (Y2+space>=self.Y and Y2<=self.Y+space):
            return True
        return False
    
    def overlaps(self,x,y):
        space = self.NODE_SPACING
        if (x+space>=self.X and x<=self.X+space) and (y+space>=self.Y and y<=self.Y+space):
            return True
        return False
    
    def get_angle(self,node):
        dotProduct = self.X*node.get_x() + self.Y*node.get_y()
         # for three dimensional simply add dotProduct = a*c + b*d  + e*f 
        vectorMod = math.sqrt(self.X*self.X + self.Y*self.Y)*math.sqrt(node.get_x()*node.get_x() + node.get_y()*node.get_y()) 
         # for three dimensional simply add modOfVector = math.sqrt( a*a + b*b + e*e)*math.sqrt(c*c + d*d +f*f) 
        angle = dotProduct/vectorMod
        return math.degrees(math.acos(angle))
        
    
    def draw(self,canvas,selectedNodes):
        for selected in selectedNodes:
            if (self == selected):
                self.draw_inbetween(canvas)
        canvas.create_image(self.X,self.Y, image = self.icon)

    def draw_start(self,canvas):
        space = self.NODE_ICON_SIZE
        canvas.create_oval(self.X-space,self.Y-space,self.X+space,self.Y+space, fill="darkgreen")

    def draw_inbetween(self,canvas):
        space = self.NODE_ICON_SIZE
        canvas.create_oval(self.X-space,self.Y-space,self.X+space,self.Y+space, fill="darkblue")
    
    def draw_end(self,canvas):
        space = self.NODE_ICON_SIZE
        canvas.create_oval(self.X-space,self.Y-space,self.X+space,self.Y+space, fill="darkred")

    def draw_name(self,canvas):
        canvas.create_text(self.X,self.Y+30,text=self.name, fill='pink', font = ('Lucida Console',9,'bold'))