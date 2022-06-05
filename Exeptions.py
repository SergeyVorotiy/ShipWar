class BordOutExeption:
    def __init__(self, textExeption):
        self.exeption_message = textExeption

    def __str__(self):
        return f"BordOutExeption: {self.exeption_message}"


class ShipPlacementExeption:
    @staticmethod
    def exeption_message():
        print("ShipPlacementExeption - Ошибка размещения корабля на игровом поле")

class DirectionExeption:
    def __init__(self, textExeption):
        self.exeption_message = textExeption

    def __str__(self):
        return f"DirectionExeption: {self.exeption_message}"