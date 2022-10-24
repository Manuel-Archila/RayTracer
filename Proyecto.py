from ray import *
from Material import *
from Color import *
from light import *
from Sphere import * 
from PlaneX import *
from envmap import *
from cube import *

r = Raytracer(1200, 636)
r.envmap = Envmap('./fondomc.bmp')
r.light = Light(V3(0, -20, 20), 2, color(255, 255, 255))
r.background_color = color(0, 0, 100)

slime = Material(diffuse = color(80, 0, 0), albedo=[0.7, 0.3, 0, 0], spec=11, refractive_index=0, path='./slime.bmp')
wood = Material(diffuse = color(80, 0, 0), albedo=[0.8, 0.2, 0, 0], spec=9, refractive_index=0, path='./wood.bmp')
leaves = Material(diffuse = color(80, 0, 0), albedo=[0.6, 0.4, 0, 0], spec=13, refractive_index=0, path='./leaves.bmp')
sbricks = Material(diffuse = color(80, 0, 0), albedo=[0.6, 0.4, 0, 0], spec=13, refractive_index=0, path='./sbricks.bmp')
mossy = Material(diffuse = color(80, 0, 0), albedo=[0.6, 0.4, 0, 0], spec=13, refractive_index=0, path='./mossy.bmp')
top = Material(diffuse = color(80, 0, 0), albedo=[0.6, 0.4, 0, 0], spec=13, refractive_index=0, path='./top.bmp')
bottom = Material(diffuse = color(80, 0, 0), albedo=[0.6, 0.4, 0, 0], spec=13, refractive_index=0, path='./bottom.bmp')
rubber = Material(diffuse = color(80, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10, refractive_index=0)
ivory = Material(diffuse = color(100, 100, 80), albedo=[0.695, 0.305, 0, 0], spec=50)
mirror = Material(diffuse = color(255, 255, 255), albedo=[0, 1, 0.8, 0], spec=1425)
glass = Material(diffuse = color(150, 180, 200), albedo=[0, 0.5, 0.1, 0.8], spec=125, refractive_index=1.5)
water = Material(diffuse=color(0,0,200),albedo=[0, 0.5, 0.35, 0.8],spec=90, refractive_index=1)

r.scene = [
    
    #Arbol
    Cube(V3(-8, 0, -11), 1, wood),
    Cube(V3(-8, 1, -11), 1, wood),
    Cube(V3(-8, 2, -11), 1, wood),
    Cube(V3(-8, -1, -11), 1, leaves),
    Cube(V3(-9, -1, -11), 1, leaves),
    Cube(V3(-7, -1, -11), 1, leaves),
    Cube(V3(-7, -2, -11), 1, leaves),
    Cube(V3(-8, -2, -11), 1, leaves),
    Cube(V3(-9, -2, -11), 1, leaves),
    Cube(V3(-6, -1, -11), 1, leaves),
    Cube(V3(-8, -1, -10), 1, leaves),
    Cube(V3(-9, -1, -10), 1, leaves),
    
    #Slime
    Cube(V3(6, 3, -9), 2, slime),
    
    #House
    Cube(V3(-3, 3, -15), 1, sbricks),
    Cube(V3(-2, 3, -15), 1, sbricks),
    Cube(V3(-1, 3, -15), 1, sbricks),
    Cube(V3(0, 3, -15), 1, sbricks),
    Cube(V3(1, 3, -15), 1, sbricks),
    Cube(V3(2, 3, -15), 1, sbricks),
    Cube(V3(3, 3, -15), 1, sbricks),

    Cube(V3(-3, 3, -14), 1, sbricks),
    Cube(V3(-2, 3, -14), 1, sbricks),
    Cube(V3(-1, 3, -14), 1, sbricks),
    Cube(V3(0, 3, -14), 1, sbricks),
    Cube(V3(1, 3, -14), 1, sbricks),
    Cube(V3(2, 3, -14), 1, sbricks),
    Cube(V3(3, 3, -14), 1, sbricks),

    Cube(V3(-3, 3, -13), 1, sbricks),
    Cube(V3(-2, 3, -13), 1, sbricks),
    Cube(V3(-1, 3, -13), 1, sbricks),
    Cube(V3(0, 3, -13), 1, sbricks),
    Cube(V3(1, 3, -13), 1, sbricks),
    Cube(V3(2, 3, -13), 1, sbricks),
    Cube(V3(3, 3, -13), 1, sbricks),

    Cube(V3(-3, 3, -12), 1, sbricks),
    Cube(V3(-2, 3, -12), 1, sbricks),
    Cube(V3(-1, 3, -12), 1, sbricks),
    Cube(V3(0, 3, -12), 1, sbricks),
    Cube(V3(1, 3, -12), 1, sbricks),
    Cube(V3(2, 3, -12), 1, sbricks),
    Cube(V3(3, 3, -12), 1, sbricks),

    Cube(V3(-3, 3, -11), 1, sbricks),
    Cube(V3(-2, 3, -11), 1, sbricks),
    Cube(V3(-1, 3, -11), 1, sbricks),
    Cube(V3(0, 3, -11), 1, sbricks),
    Cube(V3(1, 3, -11), 1, sbricks),
    Cube(V3(2, 3, -11), 1, sbricks),
    Cube(V3(3, 3, -11), 1, sbricks),

    Cube(V3(-3, 4, -15), 1, sbricks),
    Cube(V3(3, 4, -15), 1, sbricks),

    Cube(V3(-2, 2, -15), 1, sbricks),
    Cube(V3(-1, 2, -15), 1, sbricks),
    Cube(V3(-0, 2, -15), 1, sbricks),
    Cube(V3(1, 2, -15), 1, sbricks),
    Cube(V3(2, 2, -15), 1, sbricks),

    Cube(V3(-2, 1, -15), 1, sbricks),
    Cube(V3(-1, 1, -15), 1, sbricks),
    Cube(V3(0, 1, -15), 1, sbricks),
    Cube(V3(1, 1, -15), 1, sbricks),
    Cube(V3(2, 1, -15), 1, sbricks),

    Cube(V3(-2, 0, -15), 1, sbricks),
    Cube(V3(-1, 0, -15), 1, sbricks),
    Cube(V3(0, 0, -15), 1, sbricks),
    Cube(V3(1, 0, -15), 1, sbricks),
    Cube(V3(2, 0, -15), 1, sbricks),

    Cube(V3(-2, -1, -15), 1, sbricks),
    Cube(V3(-1, -1, -15), 1, sbricks),
    Cube(V3(0, -1, -15), 1, sbricks),
    Cube(V3(1, -1, -15), 1, sbricks),
    Cube(V3(2, -1, -15), 1, sbricks),

    Cube(V3(-2, 2, -14), 1, sbricks),
    Cube(V3(-2, 2, -13), 1, sbricks),
    Cube(V3(-2, 2, -12), 1, sbricks),
    Cube(V3(-2, 2, -11), 1, sbricks),

    Cube(V3(2, 2, -14), 1, sbricks),
    Cube(V3(2, 2, -13), 1, sbricks),
    Cube(V3(2, 2, -12), 1, sbricks),
    Cube(V3(2, 2, -11), 1, sbricks),

    Cube(V3(2, 1, -14), 1, sbricks),
    Cube(V3(2, 1, -13), 1, sbricks),
    Cube(V3(2, 1, -12), 1, sbricks),
    Cube(V3(2, 1, -11), 1, sbricks),

    Cube(V3(-2, 1, -14), 1, sbricks),
    Cube(V3(-2, 1, -13), 1, sbricks),
    Cube(V3(-2, 1, -12), 1, sbricks),
    Cube(V3(-2, 1, -11), 1, sbricks),

    Cube(V3(2, 0, -14), 1, sbricks),
    Cube(V3(2, 0, -13), 1, sbricks),
    Cube(V3(2, 0, -12), 1, sbricks),
    Cube(V3(2, 0, -11), 1, sbricks),

    Cube(V3(-2, 0, -14), 1, sbricks),
    Cube(V3(-2, 0, -13), 1, sbricks),
    Cube(V3(-2, 0, -12), 1, sbricks),
    Cube(V3(-2, 0, -11), 1, sbricks),

    Cube(V3(2, -1, -14), 1, sbricks),
    Cube(V3(2, -1, -13), 1, sbricks),
    Cube(V3(2, -1, -12), 1, sbricks),
    Cube(V3(2, -1, -11), 1, sbricks),

    Cube(V3(-2, -1, -14), 1, sbricks),
    Cube(V3(-2, -1, -13), 1, sbricks),
    Cube(V3(-2, -1, -12), 1, sbricks),
    Cube(V3(-2, -1, -11), 1, sbricks),

    Cube(V3(2, -2, -14), 1, sbricks),
    Cube(V3(2, -2, -13), 1, sbricks),
    Cube(V3(2, -2, -12), 1, sbricks),
    Cube(V3(2, -2, -11), 1, sbricks),

    Cube(V3(-2, -2, -14), 1, sbricks),
    Cube(V3(-2, -2, -13), 1, sbricks),
    Cube(V3(-2, -2, -12), 1, sbricks),
    Cube(V3(-2, -2, -11), 1, sbricks),

    Cube(V3(-2, -2, -15), 1, sbricks),
    Cube(V3(-1, -2, -15), 1, sbricks),
    Cube(V3(0, -2, -15), 1, sbricks),
    Cube(V3(1, -2, -15), 1, sbricks),
    Cube(V3(2, -2, -15), 1, sbricks),

    Cube(V3(2, -3, -14), 1, sbricks),
    Cube(V3(2, -3, -13), 1, sbricks),
    Cube(V3(2, -3, -12), 1, sbricks),
    Cube(V3(2, -3, -11), 1, sbricks),

    Cube(V3(-2, -3, -14), 1, sbricks),
    Cube(V3(-2, -3, -13), 1, sbricks),
    Cube(V3(-2, -3, -12), 1, sbricks),
    Cube(V3(-2, -3, -11), 1, sbricks),

    Cube(V3(-2, -3, -15), 1, sbricks),
    Cube(V3(-1, -3, -15), 1, sbricks),
    Cube(V3(0, -3, -15), 1, sbricks),
    Cube(V3(1, -3, -15), 1, sbricks),
    Cube(V3(2, -3, -15), 1, sbricks),

    Cube(V3(-1, -3, -14), 1, sbricks),
    Cube(V3(0, -3, -14), 1, sbricks),
    Cube(V3(1, -3, -14), 1, sbricks),

    Cube(V3(-1, -3, -13), 1, sbricks),
    Cube(V3(0, -3, -13), 1, sbricks),
    Cube(V3(1, -3, -13), 1, sbricks),

    Cube(V3(-1, -3, -12), 1, sbricks),
    Cube(V3(0, -3, -12), 1, sbricks),
    Cube(V3(1, -3, -12), 1, sbricks),

    Cube(V3(-1, -3, -11), 1, sbricks),
    Cube(V3(0, -3, -11), 1, sbricks),
    Cube(V3(1, -3, -11), 1, sbricks),

    Cube(V3(-1, -2, -11), 1, sbricks),
    Cube(V3(0, -2, -11), 1, sbricks),
    Cube(V3(1, -2, -11), 1, sbricks),

    Cube(V3(-1, -1, -11), 1, glass),
    Cube(V3(0, -1, -11), 1, sbricks),
    Cube(V3(1, -1, -11), 1, glass),

    Cube(V3(-1, 0, -11), 1, sbricks),
    Cube(V3(0, 0, -11), 1, sbricks),
    Cube(V3(1, 0, -11), 1, sbricks),

    Cube(V3(-1, 1, -11), 1, sbricks),
    Cube(V3(0, 1, -11), 1, bottom),
    Cube(V3(1, 1, -11), 1, sbricks),

    Cube(V3(-1, 2, -11), 1, sbricks),
    Cube(V3(0, 2, -11), 1, bottom),
    Cube(V3(1, 2, -11), 1, sbricks),

    # Picos
    Cube(V3(-3, -3, -13), 1, sbricks),
    Cube(V3(3, -3, -13), 1, sbricks),
    Cube(V3(-3, -4, -13), 1, sbricks),
    Cube(V3(3, -4, -13), 1, sbricks),

    Cube(V3(-3, -3, -11), 1, sbricks),
    Cube(V3(3, -3, -11), 1, sbricks),
    Cube(V3(-3, -4, -11), 1, sbricks),
    Cube(V3(3, -4, -11), 1, sbricks),

    Cube(V3(-2, -3, -10), 1, sbricks),
    Cube(V3(2, -3, -10), 1, sbricks),
    Cube(V3(-2, -4, -10), 1, sbricks),
    Cube(V3(2, -4, -10), 1, sbricks),

    Cube(V3(0, -3, -10), 1, sbricks),
    Cube(V3(0, -4, -10), 1, sbricks),

    PlaneX(V3(0, 4, -9), 4, 3, water),
]

r.render()
r.write('prueba.bmp')