# from ship import Ship
# class Game_Field:
#     def __init__(self):
#         self.player_field = [["o"for row in range(6)] for column in range(6)]
#         self.game_field = [["o"for row in range(6)] for column in range(6)]
#
#     def __str__(self):
#         def printed_field(field):
#             printed_field = '|-----|-----|-----|-----|-----|-----|-----|\n|     |  1  |  2  |  3  |  4  |  5  |  6  |\n|-----|-----|-----|-----|-----|-----|-----|\n'
#             k = 1
#             for row in field:
#                 printed_field += f"|  {k}  |"
#                 for column in row:
#                     printed_field += f"  {column}  |"
#                 printed_field += "\n|-----|-----|-----|-----|-----|-----|-----|\n"
#                 k += 1
#             return printed_field
#
#         return f"Поле соперника\n{printed_field(self.game_field)}Поле игрока\n{printed_field(self.player_field)}"
#     def game_lavel_complation(self):
#         self.game_ships = []
#         random_direction = random(2);
#
#     def player_lavel_complation(self):
#         print("Нужно расставить ваши корабли")
#         self.player_ships = []
#         print("У вас есть 7 кораблей. 1 на 3 клетки, 2 на 2 клетки и 4 на 1 клетку.")
#         print("Начнем с коробля на 3 клетки")
#         def set_ship_with_mast(masts):
#             ship_is_not_correct = True
#             while ship_is_not_correct:
#                 ship_data = input("Введите координаты носа корабля в формате 'X Y' и расположение в формате 'R' - по горизонтали или 'D' - по вертикали(1 1 R)").split()
#                 if len(ship_data) == 2:
#                     ship_data.append("R")
#                 if ship_data:
#                     point = (int(ship_data[0]) - 1, int(ship_data[1]) - 1)
#                     if 0 <= point[0] < 7 and 0 <= point[1] < 7:
#                         if not self.player_ships:
#                             ship = Ship(masts, point[0], point[1], ship_data[2])
#                             self.player_ships.append(ship)
#                             ship_is_not_correct = False
#                         else:
#                             is_correct = True
#                             for ship in self.player_ships:
#
#                                 if point in ship.clozed_point():
#                                     print("Между короблями должна быть минимум 1 клетка")
#                                     is_correct = False
#                                     break
#                             if is_correct:
#                                 ship = Ship(masts, point[0], point[1], ship_data[2])
#                                 self.player_ships.append(ship)
#                                 ship_is_not_correct = False
#
#                     else:
#                         print("координаты должны быть от 1 до 6")
#         set_ship_with_mast(3)
#         print("Теперь 2 корабля на 2 клетки, между короблями должна быть минимум 1 пустая клетка с каждой стороны")
#         set_ship_with_mast(2)
#         set_ship_with_mast(2)
#         print("Теперь 4 корабля на 1 клетку")
#         set_ship_with_mast(1)
#         set_ship_with_mast(1)
#         set_ship_with_mast(1)
#         set_ship_with_mast(1)
#         for ships in self.player_ships:
#             for point in ships.get_ship():
#                 self.player_field[point[0]][point[1]] = "■"
#
#
#
#
#
#
# game = Game_Field()
# game.player_lavel_complation()
# print(game)