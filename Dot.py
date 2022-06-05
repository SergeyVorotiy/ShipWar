class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def point(self):
        return (self.x, self.y)

    def __eq__(self, other):
        self.x = other[0]
        self.y = other[1]
        return self.point
    def __str__(self):
        return self.point
