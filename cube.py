from vector import *
from PlaneX import *
from PlaneY import *
from PlaneZ import *

class Cube(object):
    def __init__(self, center, size, material):
        self.center = center
        self.size = size
        self.material = material
    
    def ray_intersect(self, origin, direction):

        min = V3((self.center.x - self.size/2), (self.center.y - self.size/2), (self.center.z - self.size/2))
        max = V3((self.center.x + self.size/2), (self.center.y + self.size/2), (self.center.z + self.size/2))
        
        tmin = ((self.center.x - self.size/2) - origin.x) / direction.x
        tmax = ((self.center.x + self.size/2) - origin.x) / direction.x

        if tmin > tmax:
            tmin, tmax = tmax, tmin
        
        tymin = ((self.center.y - self.size/2) - origin.y) / direction.y
        tymax = ((self.center.y + self.size/2) - origin.y) / direction.y

        if tymin > tymax:
            tymin, tymax = tymax, tymin
        
        if tmin > tymax or tymin > tmax:
            return False
        
        if tymin > tmin:
            tmin = tymin
        
        if tymax < tmax:
            tmax = tymax

        tzmin = ((self.center.z - self.size/2) - origin.z) / direction.z
        tzmax = ((self.center.z + self.size/2) - origin.z) / direction.z

        if tzmin > tzmax:
            tzmin, tzmax = tzmax, tzmin
        
        if tmin > tzmax or tzmin > tmax:
            return False
        
        if tzmin > tmin:
            tmin = tzmin
        
        if tzmax < tmax:
            tmax = tzmax

        normal = V3(0, 0, 0)
        impact = origin + (direction * tmin)

        impact = V3(round(impact.x, 3), round(impact.y, 3), round(impact.z, 3))

        if impact.x >= min.x and impact.y >= min.y and impact.z == min.z:
            normal = V3(0, 0, -1)
            x = (impact.x - min.x)/self.size
            y = (impact.y - min.y)/self.size
            iposition = [x, y]
        
        elif impact.x >= min.x and impact.y >= min.y and impact.z == max.z:
            normal = V3(0, 0, 1)
            x = (impact.x - min.x)/self.size 
            y = (impact.y - min.y)/self.size
            iposition = [x, y]

        elif impact.x >= min.x and impact.y == min.y and impact.z >= min.z:
            normal = V3(0, -1, 0)
            x = (impact.x - min.x)/self.size 
            z = (impact.z - min.z)/self.size
            iposition = [x, z]

        elif impact.x >= min.x and impact.y == max.y and impact.z >= min.z:
            normal = V3(0, 1, 0)
            x = (impact.x - min.x)/self.size 
            z = (impact.z - min.z)/self.size
            iposition = [x, z]

        elif impact.x == min.x and impact.y >= min.y and impact.z >= min.z:
            normal = V3(-1, 0, 0)
            y = (impact.y - min.y)/self.size 
            z = (impact.z - min.z)/self.size
            iposition = [z, y]
        
        elif impact.x == max.x and impact.y >= min.y and impact.z >= min.z:
            normal = V3(1, 0, 0)
            y = (impact.y - min.y)/self.size 
            z = (impact.z - min.z)/self.size
            iposition = [z, y]

        if normal == V3(0, 0, 0):
            return False

        if tmin < 0:
            return False

        return Intersect(
            distance = tmin,
            point = impact,
            normal = normal,
            iposition = iposition
        )