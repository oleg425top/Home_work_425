import time, datetime


class PowerUnit:
    def __init__(self, name, power):
        self.power = power
        self.name = name

    def __str__(self):
        return f'Блок питания {self.name} мощностью {self.power} ватт - готов к работе...'

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
            return f'Chipset:{self.chipset}...\nБлок питания:{self.name}...\nМощность: {self.power} Ватт...\nЗагрузка компонентов...'
        else:
            return f'нет питания '


print(datetime.date.today(), 'Загрузка....')
time.sleep(2)
bloc = PowerUnit('SuperBlock', 300)
print(bloc)
time.sleep(2)
mother = Motherboard('Dazzle_CX', 'SuperBlock', 300)
print(mother.redistribute_voltage())

