class Ship:
    def __init__(self, number_of_masts, first_coordinates_x, first_coordinates_y, direction):
        self.masts = number_of_masts
        if direction != "R" and direction != "D":
            self.direction = "R"
        else:
            self.direction = direction
        if direction == "R" and first_coordinates_y > 6 - number_of_masts:
            first_coordinates_y = first_coordinates_y = number_of_masts-1
        elif direction == "D" and first_coordinates_x > 6 - number_of_masts:
            first_coordinates_x = first_coordinates_x - number_of_masts-1
        point = (first_coordinates_x, first_coordinates_y)
        self.start_point = point
        self._ship = self.set_ship()




    def get_ship(self):
        self._ship = self.set_ship()
        return self._ship


    def set_ship(self):
        self._ship = []
        for i in range(self.masts):
            if self.direction == "R":
                point = (self.start_point[0], self.start_point[1]+i)
                self._ship.append(point)
            elif self.direction == "D":
                point = (self.start_point[0]+i, self.start_point[1])
                self._ship.append(point)

        return self._ship

    def clozed_point(self):
        _clozed_point = []

        for row in range(self._ship[0][0]-1, self._ship[-1][0]+2):
            for i in range(self._ship[0][1]-1, self._ship[-1][1]+2):
                point = (row, i)
                _clozed_point.append(point)
        return _clozed_point

ship = Ship(3, 2, 2, "D")

print(ship.get_ship())
print(ship.clozed_point())