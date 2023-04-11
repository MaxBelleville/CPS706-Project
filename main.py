import tkinter as tk
from tkinter import ttk
from graphManager import GraphManager
from tkinter import filedialog as fd
from enum import Enum
from tkinter import messagebox

class State(Enum):
    START=1
    END=2
    STEP=3

class WindowController:
    #These should be treated as constants
    WIDTH = 800
    HEIGHT = 600
    graphManger = GraphManager(WIDTH,HEIGHT)
    state = State.START
    options = [
    "Dijkstra",
    "Bellman-Ford",
    ]
    font = ('Lucida Console',14)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CPS706 Project Group 7')
        self.setSizeAtCenter()
        self.createWindow()
        self.root.mainloop()
    
    def move_window(self,event):
        self.root.geometry('+{0}+{1}'.format(event.x_root-(self.WIDTH//2), event.y_root-10))
    
    def select(self,event):
        if(self.state==State.START): self.graphManger.set_start(event.x,event.y)
        if(self.state==State.END): self.graphManger.set_end(event.x,event.y)

    def step(self):
        if(self.state==State.START):
            if(not self.graphManger.check_start()): messagebox.showerror("Failed to place start", "Please click on one of the nodes first.")
            else: 
                self.state = State.END
                self.step_button.configure(text="Place End")
        elif(self.state==State.END):
            if(not self.graphManger.check_end()): messagebox.showerror("Failed to place end", "Please click on one of the nodes first.")
            else: 
                self.state = State.STEP
                self.step_button.configure(text="Next Step")
                self.graphManger.initialize()
                self.distance_label.configure(text="Cost: ∞")
                self.iteration_label.configure(text="")
        else:
            dist,iter= self.graphManger.step()
            if (dist!=float("inf")): self.distance_label.configure(text="Cost: "+ str(dist))
            if(iter>0): self.iteration_label.configure(text="Iter: "+ str(iter))

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
        self.root.geometry(f'{self.WIDTH+50}x{self.HEIGHT+100}+{center_x}+{center_y-50}')
        self.root.resizable(False, False)
    
    def reset(self):
        self.step_button.configure(text="Place Start")
        self.distance_label.configure(text="")
        self.iteration_label.configure(text="")
        self.state = State.START
        self.graphManger.reset()

    def option_changed(self,selected):
        self.reset()
        self.graphManger.set_algorithm(selected)

    def createWindow(self):
        self.root.attributes('-topmost', 1)
        self.root.iconbitmap('./assets/main.ico')
        self.root.overrideredirect(True)
        self.root.configure(bg='black',bd=1, relief="ridge")
  
        canvas = tk.Canvas(self.root,width=self.WIDTH,height=self.HEIGHT, bd=0, highlightthickness=0, bg='black')
        canvas.bind("<Button-1>", self.select)
        self.graphManger.add_canvas(canvas)

        title_bar = tk.Frame(self.root, bg='#111')
        title_bar.pack(fill=tk.X)
        title_bar.bind('<B1-Motion>', self.move_window)

        title_label = tk.Label(title_bar, bg='#111',fg='white',font=self.font, text=self.root.title())
        title_label.pack(side=tk.LEFT, pady=4, padx=8)

        close_button = tk.Button(title_bar, text='  X  ',pady=2, bg='#111',fg='white',font=self.font,borderwidth=0, command=self.root.destroy)
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
        self.interactables(bottom_bar)
        self.graphManger.add_from_file("./example.txt")

    def interactables(self,bottom_bar):
        clicked = tk.StringVar(self.root)
        clicked.set( "Dijkstra" )

        # Create Dropdown menu
        drop = tk.OptionMenu(bottom_bar, clicked, *self.options,command=self.option_changed )
        drop.configure(fg="white", bg="#111",font=self.font,activebackground="#111",activeforeground="white" )
        drop['menu'].configure(fg='white',bg="#111")
        drop.pack(side=tk.LEFT,padx=20)

        
        reset_button = tk.Button(bottom_bar, text='Reset', bg='#111',fg='white',font=self.font, command=self.reset)
        reset_button.bind('<Enter>', lambda e: reset_button.configure(bg='darkred'))
        reset_button.bind('<Leave>', lambda e: reset_button.configure(bg='#111'))
        reset_button.pack(side=tk.RIGHT,padx=15)

        self.step_button = tk.Button(bottom_bar, text='Place Start', bg='#111',fg='white',font=self.font, command=self.step)
        self.step_button.bind('<Enter>', lambda e: self.step_button.configure(bg='darkgreen'))
        self.step_button.bind('<Leave>', lambda e: self.step_button.configure(bg='#111'))
        self.step_button.pack(side=tk.RIGHT,padx=15)   

        open_file = tk.Button(bottom_bar, text='Open File', bg='#111',fg='white',font=self.font, command=self.select_file)
        open_file.bind('<Enter>', lambda e: open_file.configure(bg='darkblue'))
        open_file.bind('<Leave>', lambda e: open_file.configure(bg='#111'))
        open_file.pack(side=tk.RIGHT,padx=15)

        self.distance_label = tk.Label(bottom_bar, bg='black',fg='white',font=self.font, text="")
        self.distance_label.pack(side=tk.RIGHT, padx=15)

        self.iteration_label = tk.Label(bottom_bar, bg='black',fg='white',font=self.font, text="")
        self.iteration_label.pack(side=tk.RIGHT, padx=15)


if __name__ == "__main__":
    WindowController()
