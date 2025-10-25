from ursina import *

app = Ursina()
window.title = "BALLS CONTROLLER"
window.borderless = False
window.fullscreen = True
table = Entity(
    model = "cube",
    scale = (10, 0.5, 10),
    color = color.rgb(200, 200, 0),
    #texture="TIKVA_STOL.png",
    collider = "box"
)

sphere_main_char = Entity(
    model = "sphere",
    scale = (2, 2, 2),
    texture="TIKVA_STOL.png",
    collider = "sphere",
    position = (0, 3, 0)
)



camera_dvigat = EditorCamera()
camera_dvigat.position = (0, 10, -20)
camera_dvigat.rotation_x = 20

nebo_sky = Sky(texture = "HALLOWEEN_SKY.jpg")








app.run()
















