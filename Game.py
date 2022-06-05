from Player import User
from Player import AI
from field import Board
from Dot import Dot
import random
from ship import Ship
class Game:
    def __init__(self):
        self.user_board = Board(False)
        self.ai_board = Board(True)
        self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)

    def random_board(self):
        ships = 7
        p = 0
        while ships > 0 and p < 10000:
            p += 1
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            dir = random.randrange(0,1)
            dot = Dot(x, y)
            if self.ai_board.out(dot):
                continue
            else:
                if dir == 1:
                    self.ai_board.add_ship(Ship(3, x, y, "V"))
                else:
                    self.ai_board.add_ship(Ship(3, x, y, "H"))
                ships -= 1
        ships = 7
        p = 0
        while ships > 0 and p < 10000:
            p += 1
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            dir = random.randrange(0, 1)
            dot = Dot(x, y)
            if self.user_board.out(dot):
                continue
            else:
                if dir == 1:
                    self.user_board.add_ship(Ship(3, x, y, "V"))
                else:
                    self.user_board.add_ship(Ship(3, x, y, "H"))
                ships -= 1

    def greet(self):
        print("Привет!\nначнем игру в морской бой!\n для того чтобы сделать ход, тебе нужно вписать координаты точки, в которую ты хочешь выстрелить через пробел(x, y)")

    def loop(self):
        self.greet()
        self.random_board()
        while self.user_board.live_ships > 0 and self.ai_board.live_ships > 0:
            while self.user.move():
                print("ход окончен")
            while self.ai.move():
                print("ход окончен")
        if self.ai_board.live_ships == 0:
            print("Вы победили")
        else:
            print("Вы проиграли")
    def start(self):
        self.greet()
        self.loop()

game = Game()
game.start()