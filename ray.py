from platform import java_ver
from Color import *
from lib import *
from math import *
from vector import *
from random import *
from Sphere import *
class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = None
        self.clear_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.ar = self.width/self.height
        self.density = 0
        self.scene = []
        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color
    
    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)
    
    def render(self):
        fov = int(pi / 2 )
        tana = tan(fov / 2)
        for y in range(self.height):
            for x in range(self.width):
                i = ((2 * (x + 0.5) / self.width) - 1) * self.ar * tana
                j = (1 - (2 * (y + 0.5) / self.height) ) * tana
                direction = V3(i, j, -1).norm()
                origin = V3(0, 0, 0)
                c = self.cast_ray(origin, direction)
                self.point(x, y, c)
    
    def cast_ray(self, origin, direction):
        for s in self.scene:
            if s.ray_intersect(origin, direction):
                return s.get_material()
        
        return self.clear_color

