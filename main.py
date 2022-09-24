from ray import *
r = Raytracer(800, 600)

r.scene = [
    #Brillo ojos
    Sphere(V3(-0.45, -4.2, -14), 0.1, color(255, 255, 255)),
    Sphere(V3(0.55, -4.2, -14), 0.1, color(255, 255, 255)),
    #Nariz
    Sphere(V3(0, -3.8, -14), 0.2, color(255, 140, 0)),
    #Fondo ojos
    Sphere(V3(-0.5, -4.2, -14), 0.2, color(0, 0, 0)),
    Sphere(V3(0.5, -4.2, -14), 0.2, color(0, 0, 0)),
    #Boca
    Sphere(V3(0.75, -3.45, -14), 0.1, color(0, 0, 0)),
    Sphere(V3(0.35, -3.3, -14), 0.1, color(0, 0, 0)),
    Sphere(V3(0, -3.2, -14), 0.1, color(0, 0, 0)),
    Sphere(V3(-0.35, -3.3, -14), 0.1, color(0, 0, 0)),
    Sphere(V3(-0.75, -3.45, -14), 0.1, color(0, 0, 0)),
    #Botones
    Sphere(V3(0, 0, -14), 0.15, color(0, 0, 0)),
    Sphere(V3(0, -1, -14), 0.15, color(0, 0, 0)),
    Sphere(V3(0, -2, -14), 0.15, color(0, 0, 0)),
    #Cuerpo
    Sphere(V3(0, -4, -14), 1.5, color(255, 255, 255)),
    Sphere(V3(0, -2, -14), 2, color(255, 255, 255)), 
    Sphere(V3(0, 0, -14), 2.5, color(255, 255, 255))
]
r.point(100, 100)
r.render()
r.write("RT1.bmp")