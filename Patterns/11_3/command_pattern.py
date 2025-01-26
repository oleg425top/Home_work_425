from __future__ import annotations
from abc import ABC, abstractmethod

"""Взял задачу из книги про паттерны про ресторан"""


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class PayForOrder(Command):
    def __init__(self, get_pay):
        self._get_pay = get_pay

    def execute(self):
        print(f'Спасибо за заказ. Оплачено {self._get_pay} рублей\nПриходите снова')


class SimpleFood(Command):
    def __init__(self, payload:str) -> None:
        self._payload = payload

    def execute(self):
        print(f'Официант:Пока вы ждете я могу вам предложить:( {self._payload}) ')


class ComplexFood(Command):

    def __init__(self, cook: CookReceiver, a: str, b: str) -> None:
        self._a = a
        self._b = b
        self._cook = cook

    def execute(self) -> None:
        print('Повар получил заказ и приступил к приготовлению блюд...')
        self._cook.cooking_first_course(self._a)
        self._cook.cooking_second_course(self._b)


class CookReceiver:

    def cooking_first_course(self, a: str) -> None:
        print(f'готовлю  ({a})....')

    def cooking_second_course(self, b: str) -> None:
        print(f'готовлю ({b}).....')


class WaiterInvoker:
    _get_order = None
    _wait = None
    _get_pay = None

    def wait_order(self, command: Command):
        self._wait = command
        self._wait.execute()

    def pay_for_order(self, command: Command):
        self._get_pay = command
        if isinstance(self._get_pay, Command):
            self._get_pay.execute()

    def get_order(self, command: Command):
        self._get_order = command
        print('Повар: вы бы хотели что нибудь добавить к заказу, прежде чем я начну')
        if isinstance(self._get_order, Command):
            self._get_order.execute()
        print('Повар: может десерт?')


if __name__ == '__main__':
    waiter = WaiterInvoker()
    waiter.wait_order(SimpleFood('Закуска'))
    cook1 = CookReceiver()
    waiter.get_order(ComplexFood(cook1, 'суп', 'пюре'))
    waiter.pay_for_order(PayForOrder(1200))