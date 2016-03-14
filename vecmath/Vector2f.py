import math

class Vector2f:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.length = 0
        self.calcLength = True

    def setX(self, x):
        self.calcLength = True
        self.x = x

    def setY(self, y):
        self.calcLength = True
        self.y = y

    # to str
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # add
    def __add__(self, other):
        return Vector2f(self.x + other.x, self.y + other.y)

    # sub
    def __sub__(self, other):
        return Vector2f(self.x - other.x, self.y - other.y)

    # dot
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # scale by float
    def __div__(self, other):
        return Vector2f(self.x / other, self.y / other)

    # get normalized
    def normalized(self):
        return self / self.getLength()

    # get length
    def getLength(self):
        if self.calcLength:
            self.calcLength = False
            self.calc_length()
        return self.length

    # calc length
    def calc_length(self):
        self.length = math.sqrt(self.x * self.x + self.y * self.y)

    # get as tupple
    def tuple(self):
        return self.x, self.y

    # get as array
    def array(self):
        return [self.x, self.y]

    # componentwise multiplication
    def mulv(self, otherv):
        return Vector2f(self.x * otherv.x, self.y * otherv.y)

    # scalar componentwise multiplication
    def scale(self, other):
        return Vector2f(self.x * other, self.y * other)

    # distance squared (cheaper than distance because -sqrt)
    def dist2(self, other):
        return (other.x - self.x) * (other.x - self.x) + (other.y - self.y) * (other.y - self.y)

    # distance in 2d space of 2 vectors ( == sqrt(dist2(vec))
    def dist(self, other):
        return math.sqrt(self.dist2(other))
