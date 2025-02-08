class WinDoor:
    square_w_r = []
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = self.width * self.height
        self.square_w_r.append(self.square)

    def square_w_d(self):

        return self.square_w_r


class Room:
    def __init__(self, length_floor, width_floor, high_wall,):
        self.high_wall = high_wall
        self.length_floor = length_floor
        self.width_floor = width_floor


    def square_room(self):
        return (self.length_floor * self.high_wall * 2) + (self.width_floor * self.high_wall * 2)


    def polez_square(self):
        new_square = self.square_room() - sum(WinDoor.square_w_r)
        return f'Полезная площадь {new_square}'


window = WinDoor(2, 3)
print(window.square_w_d())
door = WinDoor(1, 2)
print(door.square_w_d())
door_2 = WinDoor(2, 2)
print(door.square_w_d())
window = WinDoor(2, 3)
print(window.square_w_d())

room =Room(15, 10,3)
# room_2 =Room(15, 10,3, door)
# print(window.square_w_d(), door.square_w_d())

print(room.square_room())
print(room.polez_square())


