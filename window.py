import taichi as ti

black = 0.0
gray = 0.5
white = 1.0

# line widh 
line_width = 10

@ti.data_oriented
class Window(object):
    def __init__(self, title="window", w=1000, h=500, arch=ti.gpu):
        self.title = title
        self.w = w
        self.h = h
        ti.init(arch=arch)
        self.line_pixels = self.line_coordinates(10, 10, 100, 100)
        self.pixels = ti.var(dt=ti.f32, shape=(w, h))
        self.gui = ti.GUI(self.title, (self.w, self.h))
        

    def draw(self, frames):
        for i in range(frames):
            self.paint(i * .03)
            self.gui.set_image(self.pixels)
            self.gui.show()
            
    @ti.kernel
    def paint(self, t: ti.f32):
        for i, j in self.pixels: # Parallized over all pixels
            if self.in_tuple_list(i, j):
                self.pixels[i, j] = 0
            else:
                self.pixels[i, j] = 1
    
    def in_tuple_list(self, x, y):
                
        if x >= self.line_pixels[0][0] and x <= self.line_pixels[len(self.line_pixels) - 1][0]:
                if y >= self.line_pixels[0][1] and y <= self.line_pixels[len(self.line_pixels) - 1][1]:
                    return True
        return False


    def line_coordinates(self, x1, y1, x2, y2):
        """generates line coordinates from starting position to end

        args:
            x1: start x position - int
            y1: start y position - int
            x2: end x position - int
            y2: end y position - int

        returns:
            list of x and y coordinates representing line
        """
        m = (y2 - y1) / (x2 - x1)
        err = 0
        y_curr = y1

        line_pixels = []

        for x in range(x1, x2+1):
            line_pixels.append((x, y_curr))
            err += m
            if err > 0.5:
                y_curr += 1
                err -= 1
            
"""
    def axis(self, x_axis, y_axis, x_range, y_range):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_range = x_range
        self.y_range = y_range

@ti.func
def complex_sqr(z):
  return ti.Vector([z[0] ** 2 - z[1] ** 2, z[1] * z[0] * 2])
"""

w = Window()
w.draw(100)
