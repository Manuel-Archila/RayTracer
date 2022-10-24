from Intersect import *
from vector import *
class PlaneZ(object):
    def __init__(self, center, w, l, material, norm):
        self.center = center
        self.w = w
        self.l = l
        self.material = material
        self.nor = norm

    def ray_intersect(self, origin, direction):
        d = (self.center.z - origin.z) / direction.z
        impact = (direction * d) - origin

        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or \
            impact.y > (self.center.y + self.l/2) or impact.y < (self.center.y - self.l/2):
            return None
        
        return Intersect(distance = d, point = impact, normal = self.norm)