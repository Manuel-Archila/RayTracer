class V3(object):
    def __init__(self, x, y, z = 0, w = 1):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "V3(%s, %s, %s)"%(self.x, self.y, self.z)
    
    def __add__(self, other):
        return V3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return V3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return V3(self.x * other, self.y * other, self.z * other)
        else:
            return V3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def __matmul__(self, other):
    # 1 Estan en la misma direccion, 0 son perpendiculares, -1 estan en direcciones opuestas
        '''if (self.x * other.x + self.y * other.y + self.z * other.z) > 0:
            return 1
        elif (self.x * other.x + self.y * other.y + self.z * other.z) < 0:
            return -1
        else:
            return 0'''
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def norm(self):
        if self.length() == 0:
            return V3(0, 0, 0)
        return self * (1 / self.length())
    
    def __round__(self):
        return V3(round(self.x), round(self.y), round(self.z))
