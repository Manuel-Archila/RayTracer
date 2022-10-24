from Intersect import *
from vector import *
class PlaneY(object):
    def __init__(self, center, w, l, material, norm):
        self.center = center
        self.w = w
        self.l = l
        self.material = material
        self.nor = norm

    def ray_intersect(self, origin, direction):
        d = (self.center.x - origin.x) / direction.x
        impact = (direction * d) - origin

        if d <= 0 or \
            impact.y > (self.center.y + self.w/2) or impact.y < (self.center.y - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2):
            return None
        
        return Intersect(distance = d, point = impact, normal = self.norm)