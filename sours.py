from ursina import*

class GLEB_BOSHKA(Entity):
    def __init__(self, position, texture, radius, mass):
        super().__init__(
            model ="sphere",
            position = position,
            texture = texture,
            scale = radius,
            collider = "sphere"
        )
        self.na_zemle = False
        self.velocity = Vec3(0, 0, 0)
        self.angular_velocity = Vec3(0, 0, 0)
        self.mass = mass
        self.FRONT = False
        self.BACK = False
        self.RIGHT = False
        self.LEFT = False
        self.gravity = -9.81 * self.mass