from abc import ABC, abstractmethod


class Home(ABC):
    def __init__(self, wall, floor, window, door):
        self.door = door
        self.window = window
        self.floor = floor
        self.wall = wall

    @abstractmethod
    def build_wall(self):
        print('Строим стены')

    @abstractmethod
    def build_floor(self):
        return print('Строим дверь')

    @abstractmethod
    def build_window(self):
        print('Строим окна')

    @abstractmethod
    def build_door(self):
        print('Строим двери')
    def __str__(self):
        return f'у дома {self.wall} стены\n{self.window}\n окна\n{self.door} дверь\nи есть {self.floor} пол'


class WoodHome(Home, ABC):
    def __init__(self, material='дерево'):
        super().__init__(wall=0, floor=0, window=0, door=0, )
        self.material = material

    def build_door(self):
        super().build_door()
        print(f'из  {self.material}')
        self.door += 1

    def build_floor(self):
        super().build_floor()
        print('из дерева')
        self.floor += 1

    def build_window(self):
        super().build_window()
        print('из дерева')
        self.window += 1

    def build_wall(self):
        Home.build_wall(WoodHome(self.material))
        print('из дерева')
        self.wall += 1

    def show_home(self):
        s = super().__str__()
        # return f'у дома {self.wall} стены из {self.material}\n{self.window}из {self.material} окна\n{self.door} из {self.material}дверь\nи есть {self.floor} из {self.material}пол'
        return s

home = WoodHome()
home.build_door()
home.build_wall()
home.build_wall()
home.build_wall()
home.build_wall()
home.build_window()
home.build_floor()
print(home.show_home())
