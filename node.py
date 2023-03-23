import tkinter as tk
class Node:
    def __init__(self,name,iconPath,X,Y):
        self.name = name
        self.icon = tk.PhotoImage(file=iconPath)
        self.X = X
        self.Y = Y

    def get_x(self):
        return self.X
    
    def get_y(self):
        return self.Y
    
    def draw(self,canvas):
        canvas.create_image(self.X,self.Y, image = self.icon)