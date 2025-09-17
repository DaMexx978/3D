import timeit

from ursina import *

prilojenye = Ursina()

cubik_rubik = Entity(model = "cube", color = color.yellow, position = (0, 0, 0), texture = "klubnika.jpg")
peremenaya_cubik = "right"
sphere = Entity(model = "sphere", color = color.azure, position = (0, 1, 0))
peremenaya_sphere = "up"
def update():
    global peremenaya_cubik, peremenaya_sphere
    cubik_rubik.rotation_x += 50 *time.dt
    cubik_rubik.rotation_z += 70 *time.dt
    #cubik_rubik.position.x += 2
    if peremenaya_cubik == "right":
        cubik_rubik.x += 1 * time.dt
        if cubik_rubik.x > 5:
            peremenaya_cubik = "left"
    elif peremenaya_cubik == "left":
        cubik_rubik.x -= 1 * time.dt
        if cubik_rubik.x < -5:
            peremenaya_cubik = "right"


def input(key):
    if key == "space":
        sphere.color = color.random_color()

prilojenye.run()