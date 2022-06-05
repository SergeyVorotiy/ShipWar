from field import Board
from Dot import Dot
import random
from Exeptions import BordOutExeption

class Player:
    def __init__(self, player_board, opponent_board):
        self.player_board = player_board
        self.opponent_board = opponent_board

    def ask(self):
        pass

    def move(self):
        dot = self.ask()
        try:
            _it_hit = self.player_board.shot(dot)
        except BordOutExeption("Ход за пределы поля") as e:
            print("Не туда")
            return True
        else:
            return _it_hit

class User (Player):
    def ask(self):
        print("Введите координаты выстрела")
        point = input("x y: - ").split()
        dot = Dot(point[0], point[1])
        return dot

class AI(Player):
    _dots = []
    def ask(self):
        is_correct = True
        while is_correct:
            x = random.randrange(0,6)
            y = random.randrange(0,6)
            dot = Dot(x, y)
            if self._dots:
                if dot in self._dots:
                    is_correct = True
                else:
                    self._dots.append(dot)
                    return dot
            else:
                self._dots.append(dot)
                is_correct = False
                return dot
            