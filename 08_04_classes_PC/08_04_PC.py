import time, datetime


class PowerUnit:
    def __init__(self, name, power):
        self.power = power
        self.name = name

    def __str__(self):
        return f'  Блок питания {self.name} мощностью {self.power} ватт - готов к работе...'

    def submit_voltage(self):
        sub_power = False
        if self.power > 0:
            sub_power = True
            return sub_power
        else:
            return sub_power


class Motherboard(PowerUnit):
    def __init__(self, chipset, name, power):
        super().__init__(name, power)
        self.chipset = chipset

    def redistribute_voltage(self):
        if super().submit_voltage():
            return f'  Chipset:{self.chipset}...\n  Блок питания:{self.name}...\n  Мощность: {self.power} Ватт...\n  Загрузка компонентов...'
        else:
            return f'нет питания '

class CP(PowerUnit):
    def __init__(self, clock_frequency, number_of_cores, name, power):
        super().__init__(name, power)
        self.clock_frequency =clock_frequency
        self.number_of_cores = number_of_cores

    def __str__(self):
        return f"  Материнская плата: {self.name}\n  Частота: {self.clock_frequency}\n  Количество ядер: {self.number_of_cores}"

    def activate_turbo_mode(self):
        if super().submit_voltage():
            return f'  Активирован турбо режим...'
        else:
            return f'не достаточно питания...'

class RAM:
    def __init__(self, memory_capacity, frequency_memory):
        self.memory_capacity = memory_capacity
        self.frequency_memory = frequency_memory

    def load_data(self):
        return f'DATA LOADING.....'

    def upload_data(self):
        return f'UPLOADING DATA...'

    def __str__(self):
        return f'RAM: {self.memory_capacity} GHZ\nFrequency: {self.frequency_memory}\n{self.load_data()}\n{self.upload_data()}'

print(datetime.date.today())
for l in 'Загрузка...':
    print(l, end='')
    time.sleep(0.22)
time.sleep(2)
print()
bloc = PowerUnit('SuperBlock', 300)
print(bloc)
time.sleep(2)
for l in 'Загрузка...':
    print(l, end='')
    time.sleep(0.22)
time.sleep(2)
print()
mother = Motherboard('Dazzle_CX', 'SuperBlock', 300)
print(mother.redistribute_voltage())
time.sleep(2)
for l in 'Загрузка...':
    print(l, end='')
    time.sleep(0.22)
time.sleep(2)
print()
cp = CP(1400, 8, 'AMD', 400 )
print(cp)
time.sleep(2)
print(cp.activate_turbo_mode())
for l in 'Загрузка...':
    print(l, end='')
    time.sleep(0.22)
time.sleep(2)
print()
ram = RAM(8, 2400)
print(ram)

