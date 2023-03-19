import tkinter as tk
import math

class WindowController:
    #These should be treated as constants
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CPS706 Project Group 7')
        self.setSizeAtCenter()
        self.root.resizable(False, False)
        self.root.attributes('-topmost', 1)
        self.root.iconbitmap('./assets/main.ico')
        self.root.mainloop()
    
    def setSizeAtCenter(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.WIDTH / 2)
        center_y = int(screen_height/2 - self.HEIGHT / 2)
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{center_x}+{center_y}')
       

if __name__ == "__main__":
    WindowController()
