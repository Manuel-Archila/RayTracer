from Material import *
from ray import *
from Sphere import *
from light import *
from Color import *
spruce = Material(diffuse=color(160, 82, 45), albedo=[0.85, 0.25], spec=4)
oak = Material(diffuse=color(255, 204, 153), albedo=[0.4, 0.6], spec=10)
ivory = Material(diffuse=color(255, 0, 0), albedo=[0.6, 0.3], spec=50)
glass = Material(diffuse=color(0, 0, 0), albedo=[0.895, 0.8], spec=50)

r = Raytracer(800, 600)
r.light = Light(position=V3(0, 0, 0), intensity=1, color=color(255, 255, 255))
r.scene = [
    # Cuerpo
    Sphere(V3(0, 0, -15), 3, ivory),
    # Cabeza
    Sphere(V3(0, -4, -15), 2, spruce),
    # Patas
    Sphere(V3(-2, 2.5, -13), 1, oak),
    Sphere(V3(2, 2.5, -13), 1, oak),
    # Brazos
    Sphere(V3(-2.8, -1.5, -13), 1, spruce),
    Sphere(V3(2.8, -1.5, -13), 1, spruce),
    # Orejas
    Sphere(V3(-1.6, -5, -13), 0.6, oak),
    Sphere(V3(1.6, -5, -13), 0.6, oak),
    # Ojos
    Sphere(V3(-0.5, -4, -13), 0.2, glass),
    Sphere(V3(0.5, -4, -13), 0.2, glass),
    # Nariz
    Sphere(V3(0, -3.25, -13), 0.5, oak),
    Sphere(V3(0, -2, -8), 0.1, glass),
]
r.render()
r.write('RT2.bmp')