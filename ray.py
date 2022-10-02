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
        self.current_color = color(0, 0, 0).to_bytes()
        self.clear_color = color(255, 255, 255).to_bytes()
        self.ar = self.width/self.height
        self.density = 0
        self.scene = []
        self.light = None
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
        material, intersect = self.scene_intersect(origin, direction)
        if material is None:
            return self.clear_color
            
        light_dir = (self.light.position - intersect.point).norm()
        diffuse_intensity = light_dir @ intersect.normal
        diffuse = material.diffuse * diffuse_intensity * material.albedo[0]
        light_reflextion = reflect(light_dir, intersect.normal)
        reflection_intesity = max(0, (light_reflextion @ direction))
        specular_intensity = self.light.intensity * reflection_intesity ** material.spec
        specular = self.light.color * specular_intensity * material.albedo[1]
        color = diffuse + specular
        return color.to_bytes()
    
    def scene_intersect(self, origin, direction):
        zbuffer = 9999999
        material = None
        intersect = None
        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect
        return material, intersect
    

