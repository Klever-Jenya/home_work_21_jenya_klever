from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        # точка отправления и точка назначения существуют
        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]  # конкретный объект

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        # TODO: Забрать товар со склада отправления
        self.__from.remove(title=self.__request.product, quantity=self.__request.quantity)
        print(f"Курьер забрал {self.__request.quantity} {self.__request.product} из {self.__request.departure}")

        # TODO: Добавить товар на склад назначения
        self.__to.add(title=self.__request.product, quantity=self.__request.quantity)
        print(f"Курьер доставил {self.__request.quantity} {self.__request.product} в {self.__request.destination}")

    def cancel(self):
        pass
    # вернуть товары от туда где они были взяты
