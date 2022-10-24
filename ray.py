from Color import *
from lib import *
from math import *
from vector import *
from random import *
from Sphere import *

MAX_RECURSION_DEPTH = 3

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = None
        self.current_color = color(0, 0, 0)
        self.clear_color = color(255, 255, 255)
        self.ar = self.width/self.height
        self.density = 0
        self.scene = []
        self.light = None
        self.envmap = None
        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c.to_bytes() or self.current_color
    
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
    
    def cast_ray(self, origin, direction, recursion = 0):
        if recursion >= MAX_RECURSION_DEPTH:
            return self.get_background(direction)

        material, intersect = self.scene_intersect(origin, direction)
        
        if material is None:
            return self.get_background(direction)
        
        if material.texture:
            material.diffuse = material.texture.get_color(intersect.iposition[0], intersect.iposition[1])

        light_direction = (self.light.position - intersect.point).norm()

        # shadow
        shadow_bias = 1.1
        shadow_origin = intersect.point + (intersect.normal * shadow_bias)
        shadow_material, shadow_intersect = self.scene_intersect(shadow_origin, light_direction)

        shadow_intensity = 1
        if shadow_material:
            # en la sombra
            shadow_intensity = 0.3

        # diffuse component
        diffuse_intensity = light_direction @ intersect.normal
        try:
            diffuse = material.diffuse * diffuse_intensity * material.albedo[0] * shadow_intensity
        except:
            print(diffuse_intensity)
            print(material.diffuse)
            print(material.albedo[0])
            print(shadow_intensity)
            exit()

        # specular component
        light_reflection = reflect(light_direction, intersect.normal)
        reflection_intensity = max(0, (light_reflection @ direction))
        specular_intensity = reflection_intensity ** material.spec
        specular = self.light.color * specular_intensity * material.albedo[1] * self.light.intensity

        # reflection
        if material.albedo[2] > 0:
            reflect_direction = reflect(direction, intersect.normal)
            reflect_bias = -0.5 if reflect_direction @ intersect.normal < 0 else 0.5
            reflect_origin = intersect.point + (intersect.normal * reflect_bias)
            reflect_color = self.cast_ray(reflect_origin, reflect_direction, recursion + 1)
        else:
            reflect_color = color(0, 0, 0)
        
        reflection = reflect_color * material.albedo[2]

        # refraction
        if material.albedo[3] > 0:
            refract_direction = refract(direction, intersect.normal, material.refractive_index)
            refract_bias = -0.5 if refract_direction @ intersect.normal < 0 else 0.5
            refract_origin = intersect.point + (intersect.normal * refract_bias)
            refract_color = self.cast_ray(refract_origin, refract_direction, recursion + 1)
        else:
            refract_color = color(0, 0, 0)

        refraction = refract_color * material.albedo[3]

        return (diffuse + specular + reflection + refraction)
    
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
    
    def get_background(self, direction):
        if self.envmap:
            return self.envmap.get_color(direction)
        else:
            return self.background_color
