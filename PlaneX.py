from Intersect import *
from vector import *
class PlaneX(object):
    def __init__(self, center, w, l, material):
        self.center = center
        self.w = w
        self.l = l
        self.material = material
        self.norm = V3(0, -1, 0)

    def ray_intersect(self, origin, direction):
        d = (self.center.y - origin.y) / direction.y
        impact = (direction * d) - origin

        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2):
            return None
        
        return Intersect(distance = d, point = impact, normal = self.norm)