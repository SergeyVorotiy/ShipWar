from Dot import Dot
from Exeptions import DirectionExeption
class Ship:
    def __init__(self, masts, x, y, directions):
        self.masts = masts
        self.point = Dot(x, y)
        self.directions = directions
        self.lives = masts
    @property
    def dots(self):
        _dots = []
        for i in range(self.masts):
            if self.directions == "H":
                point = (self.point[0], self.point[1]+i)
                _dots.append(point)
            elif self.directions == "V":
                point = (self.point[0]+i, self.point[1])
                _dots.append(point)
            else:
                raise DirectionExeption("Такого направления не существует")
        return _dots
    def hit(self):
        self.lives -= 1