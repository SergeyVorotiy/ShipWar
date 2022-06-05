from ship import Ship
from Exeptions import BordOutExeption
from Dot import Dot
class Board:
    def __init__(self, hid):
        self.hid = hid
        self.field = [["o"for row in range(6)] for column in range(6)]
        self.ships = []
        self.live_ships = 0
        self._contour_points = []

    def add_ship(self, ship):
        self.ships.append(ship)
        self.live_ships += 1
        if self.hid:
            for dot in ship.dots:
                self.field[dot[0]][dot[1]] = "■"
            self.contour(ship)

    def contour(self, ship):
        for row in range(ship.dots[0][0] - 1, ship.dots[-1][0] + 2):
            for i in range(ship.dots[0][1]-1, ship.dots[-1][1]+2):
                dot = Dot(row, i)
                if dot not in ship.dots:
                    self._contour_points.append(dot)
        for dot in self._contour_points:
            self.field[dot[0]][dot[1]] = "/"
    def get_board(self):
        printed_field = '|-----|-----|-----|-----|-----|-----|-----|\n|     |  1  |  2  |  3  |  4  |  5  |  6  |\n|-----|-----|-----|-----|-----|-----|-----|\n'
        k = 1
        for row in self.field:
            printed_field += f"|  {k}  |"
            for column in row:
                if self.hid:
                    if column != "x" and column != "/":
                        printed_field += f"  o  |"
                    else:
                        printed_field += f"  {column}  |"
                else:
                    printed_field += f"  {column}  |"
            printed_field += "\n|-----|-----|-----|-----|-----|-----|-----|\n"
            k += 1
        print(printed_field)
    def out(self,dot):
        if 0 < dot[0] < 7 and 0 < dot[1] < 7:
            return False
        else:
            return True
    def shot(self, dot):
        _its_hit_shot = False
        if not self.out(dot):
            for ship in self.ships:
                if dot in ship.dots:
                    self.field[dot[0]][dot[1]] = "x"
                    ship.hit()
                    if ship.lives == 0:
                        print("Убил")
                        self.live_ships -= 1
                    else:
                        print("Ранил")
                    _its_hit_shot = True
                else:
                    self.field[dot[0]][dot[1]] = "/"
                    print("Мимо")
                    _its_hit_shot = False
        else:
            raise BordOutExeption("Выстрел за пределы поля")
        return _its_hit_shot