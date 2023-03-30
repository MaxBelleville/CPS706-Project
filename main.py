import tkinter as tk
from tkinter import ttk
import math
from graphManger import GraphManager
from tkinter import filedialog as fd

class WindowController:
    #These should be treated as constants
    WIDTH = 800
    HEIGHT = 600
    graphManger = GraphManager(WIDTH,HEIGHT)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CPS706 Project Group 7')
        self.setSizeAtCenter()
        self.createWindow()
        self.root.mainloop()
    
    def move_window(self,event):
        self.root.geometry('+{0}+{1}'.format(event.x_root-(self.WIDTH//2), event.y_root-10))
    
    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./',
            filetypes=filetypes)
        
        self.graphManger.add_from_file(filename)

    def get_size(self):
        return self.WIDTH,self.HEIGHT

    def setSizeAtCenter(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.WIDTH / 2)
        center_y = int(screen_height/2 - self.HEIGHT / 2)
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT+100}+{center_x}+{center_y-50}')
        self.root.resizable(False, False)
    
    def createWindow(self):
        self.root.attributes('-topmost', 1)
        self.root.iconbitmap('./assets/main.ico')
        self.root.overrideredirect(True)
        self.root.configure(bg='black',bd=1, relief="ridge")
        title_font = ('Lucida Console',14)
        canvas = tk.Canvas(self.root,width=self.WIDTH,height=self.HEIGHT, bd=0, highlightthickness=0, bg='black')
        self.graphManger.add_canvas(canvas)

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
        canvas.pack()
        
        bottom_bar = tk.Frame(self.root, bg='black')
        bottom_bar.pack(fill=tk.X)

        open_file = tk.Button(bottom_bar, text='Open File', bg='#111',fg='white',font=title_font, command=self.select_file)
        open_file.bind('<Enter>', lambda e: open_file.configure(bg='darkblue'))
        open_file.bind('<Leave>', lambda e: open_file.configure(bg='#111'))
        open_file.pack(side=tk.LEFT,padx=150)

        step_button = tk.Button(bottom_bar, text='Next Step', bg='#111',fg='white',font=title_font, command=self.root.destroy)
        step_button.bind('<Enter>', lambda e: step_button.configure(bg='darkgreen'))
        step_button.bind('<Leave>', lambda e: step_button.configure(bg='#111'))
        step_button.pack(side=tk.LEFT,padx=50)

        reset_button = tk.Button(bottom_bar, text='Reset', bg='#111',fg='white',font=title_font, command=self.root.destroy)
        reset_button.bind('<Enter>', lambda e: reset_button.configure(bg='darkred'))
        reset_button.bind('<Leave>', lambda e: reset_button.configure(bg='#111'))
        reset_button.pack(side=tk.LEFT,padx=0)
        self.graphManger.add_from_file("./example.txt")

if __name__ == "__main__":
    WindowController()
