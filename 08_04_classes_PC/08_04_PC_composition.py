import time, datetime


class PowerUnit:
    def __init__(self, name, power):
        self.power = power
        self.name = name

    def submit_voltage(self):
        return f'Подано напряжение...'

    # def __str__(self):
    #     return f'  Блок питания {self.name} мощностью {self.power} ватт {self.submit_voltage()}- готов к работе...'


class Motherboard:
    def __init__(self, chipset):
        self.chipset = chipset

    def redistribute_voltage(self):
        return f'Загрузка компонентов...'

    # def __str__(self):
    #     return f'  Chipset:{self.chipset}...\n{self.redistribute_voltage()}'


class CP:
    def __init__(self, clock_frequency, number_of_cores):
        self.clock_frequency = clock_frequency
        self.number_of_cores = number_of_cores

    def activate_turbo_mode(self):
        return f'  Активирован турбо режим...'

    # def __str__(self):
    #     return f"Частота: {self.clock_frequency}\n  Количество ядер: {self.number_of_cores}\n{self.activate_turbo_mode()}"


class RAM:
    def __init__(self, memory_capacity, frequency_memory):
        self.memory_capacity = memory_capacity
        self.frequency_memory = frequency_memory

    def load_data(self):
        return f'DATA LOADING.....'

    def upload_data(self):
        return f'UPLOADING DATA...'

    # def __str__(self):
    #     return f'RAM: {self.memory_capacity} GHZ\n  Frequency: {self.frequency_memory}\n  {self.load_data()}\n  {self.upload_data()}'


class SSD:
    def __init__(self, volume):
        self.volume = volume

    def safe_data(self):
        return f'DATA SAVING....'

    def delete_data(self):
        return f'DATA IS DELETING....'

    # def __str__(self):
    #     return f'SSD: {self.volume} TB\n  {self.safe_data()}\n  {self.delete_data()}'


class VideoCard:
    def __init__(self, model, memory_capacity):
        self.model = model
        self.memory_capacity = memory_capacity

    def display_on_screen(self):
        return f'Загрузка изображения....\n        HELLO WORLD!!!!'

    # def __str__(self):
    #     return f'VideoCard: {self.model}\n  Memory: {self.memory_capacity} GB\n  {self.display_on_screen()}'


class Computer:
    def __init__(self):
        self.power_unit = PowerUnit
        self.mother_board = Motherboard()
        self.cp = CP()
        self.ram = RAM()
        self.ssd = SSD()
        self.video_card = VideoCard()

    def start_computer(self):
        self.power_unit.submit_voltage()
        self.mother_board.redistribute_voltage()
        self.cp.activate_turbo_mode()
        self.ram.load_data()
        self.ram.upload_data()
        self.ssd.safe_data()
        self.ssd.delete_data()
        self.video_card.display_on_screen()




    # def __str__(self):
    #     return f'{PowerUnit.__str__()}\n{Motherboard.__str__(self)}\n{CP.__str__(self)}\n{RAM.__str__(self)}\n{SSD.__str__(self)}\n{VideoCard.__str__(self)}'

power_unit = PowerUnit('Set_com', 1600)
mother = Motherboard('BroadWater(GC)')
cp = CP(2400, 16)
ram = RAM(128, 2400)
ssd = SSD(5)
video_card = VideoCard('Radeon 9200-SE', 128)
comp = Computer()
for l in 'Loading...':
    print(l, end='')
    time.sleep(0.22)
print()
print(comp.start_computer())

