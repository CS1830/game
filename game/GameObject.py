import vecmath.Vector2f as Vector2f

class GameObject:

    def __init__(self, pos = Vector2f.Vector2f()):
        self.pos = pos

    def draw(self): pass

    def update(self, dt): pass

    def imput(self, dt): pass