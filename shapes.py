try:
    from tkinter import Tk, Canvas, BOTH
except ImportError:
    raise Exception("Tkinter did not import correctly")


from _typeshed import SupportsReadline
import random

class Paper():
    tk = None
    
    def __init__(self, width=600, height=600):
        
        if Paper.tk is not None:
            raise Exception("Error : Paper has already been created , there can be only one paper")
        try:
            Paper.tk = Tk()
        except ValueError:
            raise Exception("Error : could not inistitiate tkinter object")
        Paper.tk.title("Drawing shapes")
        Paper.tk.geometry(str(width) + "x" + str(height) )
        Paper.tk.paper_width = width
        Paper.tk.paper_height = height
        
        Paper.tk.canvas = Canvas(Paper.tk)
        Paper.tk.canvas.pack(fill=BOTH, expand=1)
        
        
    def display(self):
        Paper.tk.mainloop()
        
    
    
    """
    Class Shape - parent to all shape classes 
    """
    
    class Shape():
        def __init__(self, width=50, height=50, x = None, y = None, color='Black'):
            if Paper.tk is None:
                raise Exception ("A paper object is needed to draw on - found no paper object")
            self.height = height
            self.width = width
            self.color = color 
            
            if x is None:
                self.x = (Paper.tk.paper_width/2) - (self.width /2)
            else :
                self.x = x
                
            if y is None:
                self.y = (Paper.tk.paper_height/2) - (self.height /2)
            else :
                self.y = y
                
        def _location(self):
            x1 = self.x
            y1 = self.y
            x2 = self.x + self.width
            y2 = self.y + self.height
            return [x1, y1, x2, y2]
        
        def randomize(self, smallest=20, largest=200):
            self.width = random.randint(smallest, largest)
            self.height = random.randint(smallest, largest)
            
            self.x = random.randint(0, Paper.tk.paper_width - self.width)
            self.y = random.randint(0, Paper.tk.paper_height - self.height)
            self.color = random.choice(["red", "yellow", "blue", "green", "grey", "white", "black"])
            
        def set_width(self, width):
            self.width = width
            
        def set_height(self, height):
            self.height = height
            
        def set_x(self, x):
            self.x = x
            
        def set_y(self, y):
            self.y = y
        def set_color(self, color):
            self.color = color 
        def get_color(self):
            return self.color
        
            

            
            
            
            

