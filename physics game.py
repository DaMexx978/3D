from ursina import *
from sours import GLEB_BOSHKA

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

sphere_main_char = GLEB_BOSHKA(
    (0, 3, 0),"TIKVA_STOL", 2, 3
)



camera_dvigat = EditorCamera()
camera_dvigat.position = (0, 10, -20)
camera_dvigat.rotation_x = 20

nebo_sky = Sky(texture = "HALLOWEEN_SKY.jpg")








app.run()
















