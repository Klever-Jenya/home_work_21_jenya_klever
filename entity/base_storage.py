from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items  # items название:количество
        self.__capacity = capacity  # вместимость

    # МЕТОД ОТ ПРОТИВНОГО
    # ДОБАВИТЬ-увеличивает запас items с учетом лимита capacity
    def add(self, title: str, quantity: int) -> None:  # None - ничего не возвращает
        # TODO: Проверить, что места достаточно
        if self.get_free_space() < quantity:
            raise NotEnoughSpace

        # TODO: Добавить товар
        if title in self.__items:
            self.__items[title] += quantity  # если есть, до добавляем только количество
        else:
            self.__items[title] = quantity  # если нет, до добавляем словарь

    def remove(self, title: str, quantity: int) -> None:  # УДАЛИТЬ - уменьшает запас items, но не ниже 0
        # TODO: Проверить, есть ли такой товар
        if title not in self.__items or self.__items[title] < quantity:  # такого товара нет/недостаточно
            raise NotEnoughProduct

        # TODO: Вычесть необходимое кол-во товара. Если товара станет 0 - удалить товар из списка
        self.__items[title] -= quantity
        if self.__items[title] == 0:
            self.__items.pop(title)

    def get_free_space(self) -> int:  # вернуть количество свободных мест на складе
        # TODO: Посчитать сумму значений в словаре __items. Вычесть ее из __capacity
        return self.__capacity - sum(self.__items.values())

    # def get_items(self) -> Dict[str, int]:  # возвращает содержание склада в словаре {товар: количество}
    #     return self.__items

    @property  # геттер
    def items(self):
        return self.__items

    @items.setter  # сеттер
    def items(self, new_data):
        self.__items = new_data

    def get_unique_items_count(self):  # возвращает количество уникальных товаров.
        return len(self.__items)
