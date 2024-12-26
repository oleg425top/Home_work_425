class WinDoor:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = self.width * self.height

    def square_w_d(self):

        return self.square


class Room:
    def __init__(self, length_floor, width_floor, high_wall, obj_w_d: object = WinDoor):
        self.high_wall = high_wall
        self.length_floor = length_floor
        self.width_floor = width_floor
        self.obj_w_d = obj_w_d
        self.win_dor_square = []

    def square_room(self):
        return 2 * self.high_wall*(self.length_floor + self.width_floor)

    def add_w_d(self):
        self.win_dor_square.append(self.obj_w_d.square_w_d)
        return f'{self.win_dor_square}'

    def get_win_dor_square(self):
        return self.win_dor_square


    def polez_square(self):
        for square in self.win_dor_square:
            new_square = self.square_room() - square
        return f'dvcxvvvx{new_square}'


window = WinDoor(2, 3)
print(window.square_w_d())
door = WinDoor(1, 2)
print(door.square_w_d())
room =Room(15, 10,3)
# print(window.square_w_d(), door.square_w_d())

print(room.square_room())
print(room.polez_square())


