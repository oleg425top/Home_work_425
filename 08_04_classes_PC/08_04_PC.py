import time


class PowerUnit:
    def __int__(self, power):
        self.power = power

    def submit_voltage(self, sub_power:bool):
        if self.power > 0 :
            sub_power = True
            return f'блок питания мощностью {self.power} готов к работе... {time.sleep(2)}...'
