from rocket import RocketBoard

board = RocketBoard(4)

board.rockets[0].altitude = 40
print(board.rockets[0].altitude)