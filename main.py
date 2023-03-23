import tkinter as tk
from tkinter import ttk
import math
from nodeManager import NodeManager

class WindowController:
    #These should be treated as constants
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CPS706 Project Group 7')
        self.setSizeAtCenter()
        self.styleWindow()
        self.root.mainloop()
    
    def move_window(self,event):
        self.root.geometry('+{0}+{1}'.format(event.x_root-(self.WIDTH//2), event.y_root-10))


    def get_size(self):
        return self.WIDTH,self.HEIGHT

    def setSizeAtCenter(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.WIDTH / 2)
        center_y = int(screen_height/2 - self.HEIGHT / 2)
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT+50}+{center_x}+{center_y}')
        self.root.resizable(False, False)
    
    def styleWindow(self):
        self.root.attributes('-topmost', 1)
        self.root.iconbitmap('./assets/main.ico')
        self.root.overrideredirect(True)
        self.root.configure(bg='black',bd=1, relief="ridge")
        title_font = ('Consolas',14,'bold')
        canvas = tk.Canvas(self.root,width=self.WIDTH,height=self.HEIGHT, bg='black')

        title_bar = tk.Frame(self.root, bg='#111')
        title_bar.pack(fill=tk.X)
        title_bar.bind('<B1-Motion>', self.move_window)

        title_label = tk.Label(title_bar, bg='#111',fg='white',font=title_font, text=self.root.title())
        title_label.pack(side=tk.LEFT, pady=4, padx=8)

        close_button = tk.Button(title_bar, text='  X  ',pady=2, bg='#111',fg='white',font=title_font,borderwidth=0, command=self.root.destroy)
        close_button.bind('<Enter>', lambda e: close_button.configure(bg='darkred'))
        close_button.bind('<Leave>', lambda e: close_button.configure(bg='#111'))
        close_button.pack(side=tk.RIGHT)
        style = ttk.Style()
        style.configure('TSeparator',background='#010101')
        separator = ttk.Separator(self.root,orient='horizontal',  style='TSeparator')
        separator.pack(fill='x')
        nodeManager = NodeManager(self.WIDTH,self.HEIGHT)
        nodeManager.draw(canvas)        
        canvas.pack()


if __name__ == "__main__":
    WindowController()
