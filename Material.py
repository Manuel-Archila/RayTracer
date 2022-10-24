from Texture import *
class Material(object):
    def __init__(self, diffuse, albedo, spec, refractive_index=0, path=None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.path = path
        if self.path is not None:
            self.texture = Texture(self.path)
        else:
            self.texture = None